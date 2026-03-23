import requests
from utils import get_requests
def get_data():
    try:
        s={'name':'张三','age':'20'}
        p=get_requests('/get',params=s)
        p.raise_for_status()
        assert p.status_code ==200
        assert p.json()['args']=={'name':'张三','age':'20'}
        print("测试通过！")
    except Exception as e:
        print(f'测试异常：{e}')
get_data()