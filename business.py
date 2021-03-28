from page import BaiduPage
from init import instance, assert_equal
import time


def page():
    return BaiduPage(instance.driver)


def search_text(text, result):
    page().get_element(BaiduPage.INPUT_BOX_XPATH).clear()
    page().get_element(BaiduPage.INPUT_BOX_XPATH).send_keys(text)
    page().search_button.click()
    # page().wait_for_text(BaiduPage.FIRST_RESULT_XPATH, result)
    time.sleep(3)
    assert_equal(page().get_element(page().FIRST_RESULT_XPATH).text, result)
    # assert page().get_element(page().FIRST_RESULT_XPATH).text == result


def open_baidu():
    page().open()


def search_css_selector(content):
    time.sleep(3)
    print(page().get_element_by_css_selector(content).get_property('value'))
    print(page().get_element(page().SEARCH_BUTTON_XPATH).get_attribute('value'))
