# 基于pytest
# pytest test_spittr_firefox.py

import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# @pytest.mark.firefox
class TestSpittrFirefox():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_add_spittle(self):
        self.driver.get("http://localhost:8080/spittr/login")

        self.driver.find_element(By.NAME, "username").send_keys("tzs919")
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.NAME, "submit").click()

        self.driver.find_element(By.LINK_TEXT, "Spittles").click()

        self.driver.find_element(By.NAME, "message").click()
        self.driver.find_element(By.NAME, "message").send_keys(
            "----" + time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime()) + "----")

        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        self.driver.find_element(By.LINK_TEXT, "Logout").click()

        assert self.driver.title == "Spitter"
        print(self.driver.title)
