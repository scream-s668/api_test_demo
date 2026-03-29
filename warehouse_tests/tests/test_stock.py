import pytest
import yaml
import os

def load_data():
    a_dir=os.path.dirname(__file__)
    b_dir=os.path.join(a_dir,'..','data','stock_data.yaml')
    with open(b_dir,'r',encoding='utf-8') as f:
        return yaml.safe_load(f)

@pytest.mark.parametrize('case',load_data()['stock_in_cases'])
def test_post_stock(api_client,case):
    params={}
    if 'stockId' in case:
        params['stockId']=case['stockId']
    if 'operateNum' in case:
        params['operateNum']=case['operateNum']
    if case.get('remark'):
        params['remark'] = case['remark']
    res=api_client.post('/stock/stockIn',params=params)
    expected_http_status = case.get('expected_http_status', 200)
    assert res.status_code == expected_http_status
    if expected_http_status == 200:
        data=res.json()
        assert data['code'] == case['expected_code']
        assert case['expected_msg'] in data['msg']
        print(f"入库测试 [{case['description']}] 通过")

@pytest.mark.parametrize('case', load_data()['stock_out_cases'])
def test_post_out(api_client, case):
    params = {}
    if 'stockId' in case:
        params['stockId'] = case['stockId']
    if 'operateNum' in case:
        params['operateNum'] = case['operateNum']
    if case.get('remark'):
        params['remark'] = case['remark']

    res = api_client.post('/stock/stockOut', params=params)
    expected_http_status = case.get('expected_http_status', 200)
    assert res.status_code == expected_http_status
    if expected_http_status == 200:
        data = res.json()
        assert data['code'] == case['expected_code']
        assert case['expected_msg'] in data['msg']
        print(f"入库测试 [{case['description']}] 通过")

