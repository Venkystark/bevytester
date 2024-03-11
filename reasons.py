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
login_response=sessionuser.post("http://192.168.0.178:8080/entry/login_check",data=login_data)
if login_response.ok:
    print("loggin success")
    print(login_response.text)
    post_res=sessionuser.post("http://192.168.0.178:8080/store/transaction",data={"csrfmiddlewaretoken":sessionuser.cookies.get('csrftoken'),"req_date": "10-03-2024","from_dept": "vmpprocess","to_dept": "Store","wono": "Not Applicable","material_type": "Raw Material","material_name": "<script>console.log('hello')</script>","req_count": 5,"delivery_date": "24/05/2024","status": "pending","process_name": ""},headers={'Referer':'http://192.168.0.178:8080/'})
    if post_res.ok:
        print(post_res.status_code)
        print(post_res.text)