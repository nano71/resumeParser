import base64
import requests
import json
from .Signature import sign
from requests.packages import urllib3
      
class CMSSEcloudNlpClient(object):

    def __init__(self, ak, sk, url):
        self.accesskey = ak
        self.secretkey = sk
        self.httpmethod = 'POST'
        self.hostname = url
    
    def request_nlp_service(self, requestpath, items):
        
        urllib3.disable_warnings()
        querystring = sign('POST',self.accesskey, self.secretkey, requestpath)
        params = ''
        for(k,v) in querystring.items():
            params += str(k) + '=' + str(v) + '&'
        params = params[:-1]


        #请求为文件
        if requestpath == '/api/nlp/v1/convertdoc':
            url = self.hostname + requestpath + '?' + params
            try:
                files = {'auditFile':open(items, 'rb')}
                s = requests.session()
                s.keep_alive = False
                response = requests.post(url, files = files, timeout = 5, verify = False)
                return response
            except FileNotFoundError:
                print("Can Not Find File " + items)
                        
        else:
            url = self.hostname + requestpath + '?' + params
            s = requests.session()
            s.keep_alive = False
            response = requests.post(url, data = json.dumps(items), headers = {"Content-Type":"application/json"}, timeout = 5, verify = False)
            return response
