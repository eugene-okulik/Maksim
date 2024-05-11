import requests
import pytest
import allure


@pytest.fixture()
def new_post_id():
    body = {
        "title": "fsakj", "body": "barasdf", "userId": 1}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )
    post_id = response.json()['id']
    print(post_id)
    yield post_id
    print('deleting the post')
    requests.delete(f'https://api.restful-api.dev/objects{post_id}')


@pytest.fixture(scope='session')
def run():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def borders():
    print("before test")
    yield
    print("after test")


@allure.feature('Posts')
@allure.story('Get posts')
def test_get_one_post(new_post_id, run, borders):
    print('test')
    with allure.step(f'Run get request for post with id {new_post_id}'):
        response = requests.get(f'https://api.restful-api.dev/objects{new_post_id}').json()
    with allure.step(f'Check that post id is {new_post_id}'):
        assert response['id'] == new_post_id


@allure.feature('Posts')
@allure.story('Get posts')
@pytest.mark.critical
def test_get_all_posts(borders):
    print('test')
    response = requests.get('https://api.restful-api.dev/objects').json()
    assert len(response) == 13


@allure.feature('Posts')
@allure.story('Create posts')
@pytest.mark.medium
def test_add_post(borders):
    print('test')
    with allure.step('Prepare test data'):
        body = {
            "title": "fsakj", "body": "barasdf", "userId": 1}
        headers = {'Content-Type': 'application/json'}
    with allure.step('Run request to create a post'):
        response = requests.post(
            'https://api.restful-api.dev/objects',
            json=body,
            headers=headers
        )
    with allure.step('Check response code is 200'):
        assert response.status_code == 200
    # assert response.json()["title"] == "fsakj"


@allure.feature('Example')
@allure.story('Manipulate posts')
@pytest.mark.parametrize('body', [12345, '#$%^&', ''])
def test_patch_a_post(new_post_id, borders, body):
    print('test')
    body = {
        "body": "barasd",
        "userId": 7
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'https://api.restful-api.dev/objects{new_post_id}',
        json=body,
        headers=headers
    ).json()
    print(response)
    # assert response.json()["body"] == 12345
    # assert response.json()["body"] == '#$%^&'
    # assert response.json()["body"] == ''


def test_delete_a_post(new_post_id, borders):
    response = requests.delete(f'https://api.restful-api.dev/objects{new_post_id}')
    print(response.json())
    print(response.status_code)
    # assert response.status_code == 200


# pytest -vs
# pytest -vs "medium"
# pytest- vs test_pytest.py::test_test_name
