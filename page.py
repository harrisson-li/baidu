from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaiduPage:
    INPUT_BOX_XPATH = '//*[@id="kw"]'
    SEARCH_BUTTON_XPATH = '//*[@id="su"]'

    FIRST_RESULT_XPATH = '//*[@id="1"]/h3/a[1]'

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.baidu.com'

    def open(self):
        self.driver.get(self.url)

    def get_element(self, xpath, timeout=30):
        return WebDriverWait(self.driver, timeout).until(conditions.presence_of_element_located((By.XPATH, xpath)))

    def wait_for_text(self, xpath, text, timeout=30):
        return WebDriverWait(self.driver, timeout).until(conditions.text_to_be_present_in_element((By.XPATH, xpath), text))

    def get_element_by_css_selector(self, content):
        return self.driver.find_element_by_css_selector(content)

    @property
    def search_button(self):
        return self.get_element(self.SEARCH_BUTTON_XPATH)
