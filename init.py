import unittest
from selenium import webdriver
from data import browser
import pytest
from functools import wraps


class Container:
    driver = None
    pass


instance = Container()


class TestBase(unittest.TestCase):

    def setUp(self):
        self.set_browser()

    def tearDown(self):
        instance.driver.close()

    def set_browser(self):
        if browser == 'Chrome':
            instance.driver = webdriver.Chrome()
        else:
            instance.driver = webdriver.Safari()


def print_func_aaa(function):
    def wrap(*args, **kwargs):
        print(function.__name__, function.__dict__, *args, **kwargs)
        function(*args, **kwargs)
        print('bbb')

    return wrap


@print_func_aaa
def assert_equal(result, expected):
    if result != expected:
        raise ValueError('\nExpected: {}\nActual: {}'.format(expected, result))



