# 基于pytest
# pytest test_spittr_remote.py
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


class TestSpittrRemote():
    def setup_method(self, method):
        self.driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
                                       desired_capabilities=DesiredCapabilities.CHROME)
        # self.driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
        #                                desired_capabilities=DesiredCapabilities.FIREFOX)

    def teardown_method(self, method):
        self.driver.quit()

    def test_add_spittle(self):
        # self.driver.get("http://172.20.10.12:8080/spittr/login")
        self.driver.get("http://192.168.1.109:8080/spittr/login")
        # self.driver.get("http://172.20.10.12:8080/spittr/login")
        time.sleep(1)

        self.driver.find_element(By.NAME, "username").send_keys("tzs919")
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(1)

        self.driver.find_element(By.LINK_TEXT, "Spittles").click()
        time.sleep(1)

        self.driver.find_element(By.NAME, "message").click()
        time.time()
        self.driver.find_element(By.NAME, "message").send_keys(
            "----" + time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime()) + "----")

        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(1)

        self.driver.find_element(By.LINK_TEXT, "Logout").click()

        assert self.driver.title == "Spitter"
        print(self.driver.title)

        # self.driver.close()  #firefox要删除
