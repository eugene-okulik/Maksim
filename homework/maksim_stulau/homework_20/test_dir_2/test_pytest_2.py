import requests
import pytest


@pytest.fixture()
def num():
    return 3


def test_delete(new_post_id):
    requests.delete(f'https://api.restful-api.dev/objects{new_post_id}')


def test_num(num):
    print(num)

# pytest -vs -n auto (вместо auto можно указать кол-во ядер(потоков))
# pytest -v --alluredir=allure-results
# allure serve allure-results/
