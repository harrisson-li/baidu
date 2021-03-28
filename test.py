import pytest
from business import search_text, open_baidu, search_css_selector
from data import search_list
from init import TestBase


class TestBaidu(TestBase):

    def atest_open_baidu(self):
        open_baidu()

    def atest_baidu_search(self):
        open_baidu()
        for item in search_list:
            search_text(item['test_text'], item['result'])

    def test_css_selector(self):
        open_baidu()
        search_css_selector('#su')


if __name__ == '__main__':
    # unittest.main()
    pytest.main(['-rA', '--tb=line'])
