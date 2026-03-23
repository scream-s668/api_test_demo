import pytest
import requests
def test_get_request(app):
    s={'name':'张三','age':'18'}
    p=app.get('/get',params=s)
    p.raise_for_status()
    assert p.status_code==200
    assert p.json()['args']==s
    print('get测试通过！')
def test_post_request(app):
    s={'username':'zhangsan','password':'123456'}
    p=app.post('/post',json=s)
    p.raise_for_status()
    assert p.status_code==200
    assert p.json()['json']=={'username':'zhangsan','password':'123456'}
    print("post测试通过！")
def test_put_request(app):
    s={'username':'zhangsan','password':'1346'}
    p=app.put('/put',json=s)
    p.raise_for_status()
    assert p.status_code==200
    assert p.json()['json']==s
    print('put测试通过！')
def test_delete_request(app):
    s={'username':'zhangsan'}
    p=app.delete('/delete',params=s)
    p.raise_for_status()
    assert p.status_code==200
    assert p.json()['args']==s
    print('delete测试通过！')
