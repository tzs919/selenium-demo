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
from selenium.webdriver.common.proxy import *


class TestSpittrRemote():
    def setup_method(self, method):
        PROXY = "http://192.168.1.109:2802"
        proxy = Proxy({
            "httpProxy": PROXY,
            "ftpProxy": PROXY,
            "sslProxy": PROXY,
            "proxyType": "MANUAL",
        })
        self.driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
                                       desired_capabilities=DesiredCapabilities.CHROME
                                       )
        # self.driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
        #                                desired_capabilities=DesiredCapabilities.FIREFOX)

    def teardown_method(self, method):
        self.driver.quit()

    def test_add_spittle(self):
        self.driver.get("https://www.baidu.com/")

        print(self.driver.current_url)
        print(self.driver.title)

        # self.driver.close()  #firefox要删除
