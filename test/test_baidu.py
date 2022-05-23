#!/usr/bin/env python

# !coding:utf-8

# 基于pytest-selenium
# pytest -v -s test_baidu.py --driver Chrome
# pytest -v test_baidu.py --driver Chrome
# pytest -v -s test_baidu.py --driver Firefox
# pytest -v test_baidu.py --driver Firefox --html=report.html

import pytest


def test_baidu_title(selenium):
    selenium.get('http://www.baidu.com/')
    # print("=====", selenium.page_source)

    assert selenium.title == '百度一下，你就知道'

# def test_baidu_current_url(selenium):
#     selenium.get('http://www.baidu.com/')
#
#     assert selenium.current_url == 'https://www.baidu.com/'
#
#
# def test_baidu_so_getValue(selenium):
#     selenium.get('http://www.baidu.com/')
#
#     so = selenium.find_element_by_id('kw')
#
#     so.send_keys('伤心的辣条')
#     print("======================")
#     print(so.get_attribute('value'))
#
#     assert so.get_attribute('value') == '伤心的辣条'
