import re
from urllib import response
import requests

from modules.pj_config import ProjectConfig

BASEURL = ProjectConfig['baseURL']

def getAPI(url, headerRequest):
    url = BASEURL + url
    response = requests.get(url, headers=headerRequest)
    return response

def postAPI(url, headerRequest, bodyRequest):
     url = BASEURL + url
     response = requests.post(url,json=bodyRequest, headers=headerRequest )
     return response
 
def cleanhtml(raw_html):
    """Xóa HTML Tag"""
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext