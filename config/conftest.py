import pytest
from utils import *

@pytest.fixture
def app():
    class App:
        @staticmethod
        def get(path,params=None):
            print(f'正在发送GET请求：{path}|params={params}')
            return get_url(path,params=params)
        @staticmethod
        def post(path,json=None,data=None):
            print(f'正在发送POST请求：{path}|json={json}|data={data}')
            return post_request(path,json=json,data=data)
        @staticmethod
        def put(path,json=None,data=None):
            print(f'正在发送PUT请求：{path}|json={json}|data={data}')
            return put_request(path, json=json, data=data)
        @staticmethod
        def delete(path,params=None,json=None,data=None):
            print(f'正在发送DELETE请求：{path}|params={params}|json={json}|data={data}')
            return delete_request(path,params=params,json=json,data=data)
    return App()