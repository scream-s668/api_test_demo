import requests
url='http://httpbin.org'
def get_requests(path,params=None):
    url1=url+path
    return requests.get(url1,params=params)