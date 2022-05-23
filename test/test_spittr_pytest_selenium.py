# 基于pytest-selenium
# pytest -v test_spittr_pytest_selenium.py --driver Chrome
# pytest -v test_spittr_pytest_selenium.py --driver Firefox

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


def test_add_spittle(selenium):
    selenium.get("http://localhost:8080/spittr/login")
    time.sleep(1)

    selenium.find_element(By.NAME, "username").send_keys("tzs919")
    selenium.find_element(By.NAME, "password").send_keys("123456")
    selenium.find_element(By.NAME, "submit").click()
    time.sleep(1)

    selenium.find_element(By.LINK_TEXT, "Spittles").click()
    time.sleep(1)

    selenium.find_element(By.NAME, "message").click()
    selenium.find_element(By.NAME, "message").send_keys(
        "----" + time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime()) + "----")

    selenium.find_element_by_xpath("//input[@type='submit']").click()
    time.sleep(1)

    selenium.find_element(By.LINK_TEXT, "Logout").click()
    # selenium.close()
