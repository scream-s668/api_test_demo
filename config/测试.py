from utils import *
def test_get_config():
    try:
        s={'name':'张三','age':18}
        p=get_url('/get',params=s)
        p.raise_for_status()
        assert p.status_code==200
        assert p.json()['args']=={'name':'张三','age':'20'}
        print('GET测试通过')
    except AssertionError :
        print('断言失败')
    except Exception as e:
        print(f'测试异常：{e}')
def test_post_config():
    try:
        s={'username':'zhang','password':'123456'}
        p=post_request('/post',json=s)
        p.raise_for_status()
        assert p.status_code==200
        assert p.json()['json']=={'username':'zhang','password':'456'}
        print("post测试完成！")
    except AssertionError:
        print('断言失败')
    except Exception as e:
        print(f'测试异常：{e}')
def test_put_config():
    try:
        s={'username':'zhang','password':'123456'}
        p=put_request('/put',json=s)
        p.raise_for_status()
        assert p.status_code==200
        assert p.json()['json']==s
        print("put测试通过！")
    except AssertionError:
        print('断言失败')
    except Exception as e:
        print(f'异常错误：{e}')
def test_delete_config():
    try:
        s={'username':'zhang'}
        p=delete_request('/delete',params=s)
        p.raise_for_status()
        assert p.status_code==200
        assert p.json()['args']==s
        print('测试通过！')
    except AssertionError:
        print('断言失败')
    except Exception as e:
        print(f"异常：{e}")