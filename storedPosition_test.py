from django.test import TestCase

import requests
import json



url = "http://127.0.0.1:8000/ArmRestApi/loadProgram"
sess = requests.session()
res = sess.get(url)
print(json.loads(res.text))


# insert  teachingNewPosition

url = "http://127.0.0.1:8000/ArmRestApi/storedPosition"
csrftoken = sess.cookies['csrftoken']
# 
headers = {'Content-type': 'application/json',  "X-CSRFToken": csrftoken}
# 
prm = {"cmd":"foobar"}
# 
params = json.dumps(prm)
print(params)
# post test data
res = sess.get(url, data=params, headers=headers)


print(json.loads(res.text))



