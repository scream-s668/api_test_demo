import pytest
from utils import load_test_data

@pytest.mark.parametrize('user',load_test_data())
class Testuser:
    @staticmethod
    def test_get(app,user):
        name=user['name']
        age=user['age']
        data={'name':name,'age':str(age)}
        s=app.get('/get',params=data)
        s.raise_for_status()
        assert s.status_code == 200
        assert s.json()['args'] == data
        print(f'GET测试通过：{name}')
    @staticmethod
    def test_post(app,user):
        name=user['name']
        age=user['age']
        data = {"name": name, "age": age}
        s = app.post('/post', json=data)
        s.raise_for_status()
        assert s.status_code == 200
        assert s.json()["json"] == data
        print(f'POST测试通过:{name}')
    @staticmethod
    def test_put(app,user):
        name=user['name']
        age=user['age']
        data = {"name": name, "age": age}
        s = app.put('/put', json=data)
        s.raise_for_status()
        assert s.status_code == 200
        assert s.json()["json"] == data
        print('PUT测试通过！')
    @staticmethod
    def test_delete(app, user):
        name=user['name']
        data = {"name": name}
        s = app.delete('/delete', json=data)
        s.raise_for_status()
        assert s.status_code == 200
        assert s.json()["json"] == data
        print('DELETE测试通过!')
