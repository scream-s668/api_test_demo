import logging
import os
import pytest
import yaml

from ..utils.api_client import ApiClient

log_dir=os.path.join(os.path.dirname(os.path.realpath(__file__)), '../logs')
os.makedirs(log_dir, exist_ok=True)
log_file=os.path.join(log_dir, 'test.log')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=log_file,
    filemode='a',
    encoding='utf-8'
)
logger = logging.getLogger(__name__)

def load_config():
    a_dir=os.path.dirname(__file__)
    b_dir=os.path.join(a_dir, '../config', 'config.yaml')
    with open(b_dir, 'r',encoding='utf-8') as f:
        return yaml.safe_load(f)

@pytest.fixture(scope='session')
def config():
    return load_config()

@pytest.fixture(scope='session')
def api_client(config):
    base_url = config['base_url']
    timeout = config['timeout']
    retry = config.get('retry', {})
    auth = config.get('auth', {})
    return ApiClient(base_url, timeout, retry, auth)
