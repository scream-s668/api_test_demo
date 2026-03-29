import logging

import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

logger=logging.getLogger(__name__)

class ApiClient:
    def __init__(self,base_url,timeout,a_config=None,b_config=None):
        self.base_url=base_url
        self.timeout=timeout
        self.session=requests.Session()

        if a_config:
            styx=Retry(
                total=a_config.get("total",3),
                backoff_factor=a_config.get("backoff_factor",1),
                status_forcelist=a_config.get("status_forcelist",[500, 502, 503, 504],),
                allowed_methods=['GET','POST','PUT','DELETE']
            )
            aste=HTTPAdapter(max_retries=styx)
            self.session.mount('http://',aste)
            self.session.mount('https://',aste)
        if b_config and 'token' in b_config:
            self.session.headers.update({'Authorization': 'Bearer {}'.format(b_config['token'])})

    def get(self,path,params=None,timeout=None):
        url=self.base_url+path
        logger.info(f'请求GET：{url},params={params},timeout={timeout}')
        res=self.session.get(url,params=params,timeout=timeout)
        logger.info(f'状态码:{res.status_code}')
        return res
    def post(self,path,data=None,json=None,params=None,timeout=None):
        url=self.base_url+path
        logger.info(f'请求POST：{url},data={data},json={json},timeout={timeout}')
        res=self.session.post(url,data=data,json=json,params=params,timeout=timeout)
        logger.info(f'状态码:{res.status_code}')
        return res
    def put(self,path,data=None,json=None,timeout=None):
        url = self.base_url + path
        logger.info(f'请求PUT：{url},data={data},json={json},timeout={timeout}')
        res = self.session.put(url, data=data, json=json, timeout=timeout)
        logger.info(f'状态码:{res.status_code}')
        return res
    def delete(self,path,params=None,timeout=None):
        url = self.base_url + path
        logger.info(f'请求GET：{url},params={params},timeout={timeout}')
        res = self.session.delete(url, params=params, timeout=timeout)
        logger.info(f'状态码:{res.status_code}')
        return res
