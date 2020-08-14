from django.test import TestCase

import requests
import json



url = "http://127.0.0.1:8000/ArmRestApi/loadProgram"
sess = requests.session()
res = sess.get(url)
print(json.loads(res.text))


# insert  teachingNewPosition

url = "http://127.0.0.1:8000/ArmRestApi/teachingNewPosition"
csrftoken = sess.cookies['csrftoken']
# 
headers = {'Content-type': 'application/json',  "X-CSRFToken": csrftoken}
# 
prm = {"cmd":"foobar"}
# 
params = json.dumps(prm)
print(params)
# post test data
res = sess.post(url, data=params, headers=headers)


print(json.loads(res.text))



# update
url = "http://127.0.0.1:8000/ArmRestApi/runProgram"
csrftoken = sess.cookies['csrftoken']
# 
headers = {'Content-type': 'application/json',  "X-CSRFToken": csrftoken}

# 
prm = {"cmd":"hogegeho","rowNum": "0"}

# 
params = json.dumps(prm)

print(params)
# post test data
res = sess.post(url, data=params, headers=headers)

#print 
print(json.loads(res.text))

