import requests
import pytest


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


def test_get_one_post(new_post_id, run, borders):
    print('test')
    response = requests.get(f'https://api.restful-api.dev/objects{new_post_id}').json()
    assert response['id'] == new_post_id


@pytest.mark.critical
def test_get_all_posts(borders):
    print('test')
    response = requests.get('https://api.restful-api.dev/objects').json()
    assert len(response) == 13


@pytest.mark.medium
def test_add_post(borders):
    print('test')
    body = {
        "title": "fsakj", "body": "barasdf", "userId": 1}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )

    assert response.status_code == 200
    # assert response.json()["title"] == "fsakj"


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
