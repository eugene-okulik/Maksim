import requests


def all_data():
    response = requests.get('https://api.restful-api.dev/objects').json()
    print(response)
    assert len(response) == 13, 'Not all posts returned'


def data_by_id():
    data_id = 7
    response = requests.get(f'https://api.restful-api.dev/objects?id={data_id}').json()
    print(response)
    assert int(response[0]['id']) == data_id


def create_obj():
    body = {
        "name": "Apple MacBook Pro 16-500",
        "data": {
            "year": 20195,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )
    print(response)
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['data']['year'] == 20195, 'Year is incorrect'


def create_obj_id():
    body = {
        "name": "Apple MacBook Pro 16-500",
        "data": {
            "year": 20195,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )
    return response.json()['id']


def clear(post_id):
    requests.delete(f'https://api.restful-api.dev/objects{post_id}')


def put_data():
    post_id = create_obj_id()
    body = {
        "name": "Apple MacBook Pro 16-500_3700",
        "data": {
            "year": 201959868,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'https://api.restful-api.dev/objects/{post_id}',
        json=body,
        headers=headers
    ).json()
    assert response['data']['year'] == 201959868
    assert response['name'] == "Apple MacBook Pro 16-500_3700"
    clear(post_id)


def patch_data():
    post_id = create_obj_id()
    body = {
        "data": {
            "CPU model": "Intel Core i99999",
            "Hard disk size": "111111 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{post_id}',
        json=body,
        headers=headers
    ).json()
    print(response)
    clear(post_id)


def delete_data():
    post_id = create_obj_id()
    response = requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
    print(response.json())
    print(response.status_code)


delete_data()
