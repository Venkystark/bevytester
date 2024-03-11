import requests
from mes.otheruser import *
#from mqtt.test import get_session
import json
from bs4 import BeautifulSoup
sessionuser=requests.Session()
login_csrf_response=sessionuser.get("http://192.168.0.178:8080/login")
login_csrf=login_csrf_response.cookies.get('csrftoken')
login_data={
"username": "venkat7venkatesh77@gmail.com",
"password": "@Venkystark77",
# "username": "vstore-viewer@gmail.com",
# "password": "123",
"req_id": generate_uuid(),
"csrfmiddlewaretoken": login_csrf
}
print("before login:",sessionuser.cookies)
login_response=sessionuser.post("http://192.168.0.178:8080/entry/login_check",data=login_data)
print("After login:",sessionuser.cookies)
if login_response.ok:
    print("loggin success")
    print(login_response.text)
    sessionuser.cookies.update({"role":"Admin"})
    print(sessionuser.cookies)