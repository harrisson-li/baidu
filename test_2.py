import pytest


@pytest.fixture()
def print_before():
    print('aaa')


@pytest.mark.usefixtures('print_before')
def test_print_main():
    print('\nbbb')


if __name__ == '__main__':
    pytest.main()
