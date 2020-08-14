from django.test import TestCase

import requests
import json


url = "http://127.0.0.1:8000/ArmRestApi/loadProgram"
sess = requests.session()
res = sess.get(url)
print(json.loads(res.text))

csrftoken = sess.cookies['csrftoken']

# 
headers = {'Content-type': 'application/json',  "X-CSRFToken": csrftoken}

# 
prm = {"data":"hogegeho","param1": "ぎ　 ", "param2": "パラメータ２","progName" : "api robot arm"}

# 
params = json.dumps(prm)

print(params)
# post test data
res = sess.post(url, data=params, headers=headers)

#print 
print(json.loads(res.text))

