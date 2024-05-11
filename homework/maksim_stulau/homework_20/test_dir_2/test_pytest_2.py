import requests
import pytest
import allure


@allure.story('Create posts')
@allure.feature('Posts')
@pytest.fixture()
def num():
    return 3


@allure.story('Manipulate posts')
@allure.feature('Example')
def test_delete(new_post_id):
    requests.delete(f'https://api.restful-api.dev/objects{new_post_id}')


@allure.story('Print')
def test_num(num):
    print(num)

# pytest -vs -n auto (вместо auto можно указать кол-во ядер(потоков))
# pytest -v --alluredir=allure-results
# allure serve allure-results/    - отчет локальный онлайн
#  allure generate -c allure-results/ -o allure-reports
