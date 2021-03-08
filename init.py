import unittest
from selenium import webdriver


class Container:
    driver = None
    pass


instance = Container()


class TestBase(unittest.TestCase):

    def setUp(self):
        instance.driver = webdriver.Chrome()

    def tearDown(self):
        instance.driver.close()
