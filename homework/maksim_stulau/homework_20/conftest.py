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


@pytest.fixture()
def num():
    return 1
