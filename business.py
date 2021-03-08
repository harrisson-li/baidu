from page import BaiduPage
from init import instance


def page():
    return BaiduPage(instance.driver)


def search_text(text, result):
    page().get_element(BaiduPage.INPUT_BOX_XPATH).clear()
    page().get_element(BaiduPage.INPUT_BOX_XPATH).send_keys(text)
    page().get_element(BaiduPage.SEARCH_BUTTON_XPATH).click()
    page().wait_for_text(BaiduPage.FIRST_RESULT_XPATH, result)


def open_baidu():
    page().open()
    page().get_element(BaiduPage.INPUT_BOX_XPATH)
    page().get_element(BaiduPage.INPUT_BOX_XPATH)
