import pytest
from business import search_text, open_baidu
from data import search_list
from init import TestBase


class TestBaidu(TestBase):

    def test_open_baidu(self):
        open_baidu()

    def test_baidu_search(self):
        open_baidu()
        for item in search_list:
            search_text(item['test_text'], item['result'])


if __name__ == '__main__':
    # unittest.main()
    pytest.main(['-rA', '--tb=line'])
