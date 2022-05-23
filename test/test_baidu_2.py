#!/usr/bin/env python

# !coding:utf-8

# 基于pytest-selenium
# pytest -v test_baidu_2.py --driver Firefox
# pytest -v test_baidu_2.py --driver Chrome

import pytest


@pytest.fixture()
def init(selenium):
    selenium.get('http://www.baidu.com/')

    print("----before----")

    yield
    print("-----after-----")

    selenium.quit()


def test_baidu_title(init, selenium):
    assert selenium.title == '百度一下，你就知道'
    print("----middle1---")


def test_baidu_current_url(init, selenium):
    assert selenium.current_url == 'https://www.baidu.com/'
    print("----middle2---")


def test_baidu_so_getValue(init, selenium):
    so = selenium.find_element_by_id('kw')

    so.send_keys('伤心的辣条')

    assert so.get_attribute('value') == '伤心的辣条'
    print("----middle3---")