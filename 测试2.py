import requests
url = 'http://httpbin.org'
#查询
def yi():
    p=requests.get(url+'/get')
    print('状态码：',p.status_code)
    print('响应头：',p.headers)
    #完整的响应体
    print('响应体：',p.text)
#新增请求(json段)
def er():
    s={'suername':'er','password':'123456'}
    p=requests.post(url+'/post',json=s)#json是请求参数
    print('状态码：',p.status_code)
    print('json:',p.json()['json'])
    print('Type:',p.json()['headers']['Content-Type'])
#查询
def san():
    s={'name':'张三','age':18}
    p=requests.get(url+'/get',params=s)#params是把数据放在URL查询字符串后
    print('URL:',p.url)
    print('args:',p.json()['args'])
#新增请求(文本data)
def si():
    s={'username':'si','password':'123465'}
    p=requests.post(url+'/post',data=s)
    print('Content-Type:',p.json()['headers']['Content-Type'])
    print('form:',p.json()['form'])
#断言
def wu():
    s={'name':'wu','age':18}
    p=requests.get(url+'/get',params=s)
    print('URL:',p.url)
    print('args:',p.json()['args'])
    assert p.status_code == 200,f'实践状态：{p.status_code}'
    assert p.json()['args']['name'] == 'wu',f'实际：{p.json()['args']['name']}'
    assert p.json()['args']['age'] == '18',f'实际：{p.json()['args']['age']}'
    print('测试完毕！')
#异常
def liu():
    s={'name':'liu','age':'18'}
    try:
        p=requests.get(url+'/get',params=s,timeout=5)#timeout是设置超时时间
        p.raise_for_status()#检查状态是不是4xx/5xx
        assert p.status_code==200
        assert p.json()['args']=={'age':'18','name':'5'},f'实际json：{p.json()['args']}'
        print('测试通过！')
    except requests.exceptions.Timeout:
        print('请求超时')
    except requests.exceptions.HTTPError as e:
        print(f'http其他错误：{e.response.status_code}')
    except AssertionError as e:
        print(f'断言失败！：{e}')
    except Exception as e:
        print(f'其他错误{e}')
def qi():
    s={'name':'qi','age':'18'}
    p=requests.put(url+'/put',json=s)
    print(f'更新:{p.json()['json']}')
qi()