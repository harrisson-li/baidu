import unittest
from selenium import webdriver
from data import browser


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
