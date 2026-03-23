import requests
url='http://httpbin.org'
def test_get_query():
    try:
        s = {'name': '张三', 'age': '20'}
        p = requests.get(url + '/get', params=s, timeout=5)
        p.raise_for_status()
        assert p.status_code==200
        assert p.json()['args']['name']=='张三'
        assert p.json()['args']['age']=='20'
        print('GET测试通过！')
    except requests.exceptions.Timeout:
        print('请求超时')
def test_post_json():
    try:
        s={'username':'testuser','password':'123456'}
        p=requests.post(url+'/post',json=s,timeout=5)
        p.raise_for_status()
        assert p.status_code==200
        assert p.json()['json']['username']=='testuser'
        assert p.json()['headers']['Content-Type']=='application/json'
        print('POST测试通过！')
    except requests.exceptions.Timeout:
        print('请求超时！')
if __name__ == '__main__':
    test_get_query()
    test_post_json()