import os
import requests
import yaml
import logging
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

star=Retry(#设置规则
    total=3,#重试次数
    backoff_factor=1,#间隔
    status_forcelist=[500,502,503,504],
    allowed_methods=["GET","POST","PUT","DELETE"]
)
session=requests.Session()#简化
adapter = HTTPAdapter(max_retries=star)#导入规则
session.mount('http://', adapter)#前缀
session.mount('https://', adapter)

#日志设置
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',#格式
    datefmt='%Y-%m-%d-%H-%M-%S',#时间
)
logger=logging.getLogger(__name__)#创建日志记录器

a_dir=os.path.dirname(__file__)#获取当前文件位置
a_path=os.path.join(a_dir,'.','config.yaml')#识别的文件位置
with open(a_path,'r',encoding='utf-8') as f:#读取文件内容
    config=yaml.safe_load(f)

BASE_URL=config['base_url']
TIMEOUT=config['timeout']
#数据返回
def load_test_data():
    return config['test_users']

def get_url(p,params=None):
    url=BASE_URL+p
    logger.info(f'发送GET请求： {url}，params={params}')
    try:
        s=session.get(url,params=params,timeout=TIMEOUT)
        logger.info(f'收到响应：{s.status_code}')
        return s
    except Exception as e:
        logger.error(f'GET请求错误：{e}')
        raise
def post_request(pl,json=None,data=None):
    url=BASE_URL+pl
    logger.info(f'发送POST请求： {url}，json={json},data={data}')
    try:
        s=session.post(url,json=json,data=data,timeout=TIMEOUT)
        logger.info(f'收到响应{s.status_code}')
        return s
    except Exception as e:
        logger.error(f'POST请求错误：{e}')
        raise
def put_request(pl,json=None,data=None):
    url=BASE_URL+pl
    logger.info(f'发送PUT请求： {url}，json={json},data={data}')
    try:
        s=session.put(url,json=json,data=data,timeout=TIMEOUT)
        logger.info(f'收到响应：{s.status_code}')
        return s
    except Exception as e:
        logger.error(f'PUT请求错误：{e}')
        raise
def delete_request(pl,params=None,json=None,data=None):
    url=BASE_URL+pl
    logger.info(f'发送DELETE请求： {url}，params={params}json={json},data={data}')
    try:
        s=session.delete(url,params=params,json=json,data=data,timeout=TIMEOUT)
        logger.info(f'收到响应：{s.status_code}')
        return s
    except Exception as e:
        logger.error(f'DELETE请求错误：{e}')
        raise
