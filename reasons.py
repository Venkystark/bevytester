import requests
from mes.otheruser import *
#from mqtt.test import get_session
import json
#main
session=get_other_user_session()
# post_res=session.post("http://192.168.0.178:8080/parts",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),
# "part_no":"wilogin","part_cost":5
# },headers={'Referer':'http://192.168.0.178:8080/'})
# 
brokentext=""
usertext=""
post_res=session.get("http://192.168.0.178:8080/process_page")
if post_res.ok:
    print("get successfully")
    #print(post_res)
    print(post_res.status_code)
    brokentext=post_res.text
    if(post_res.text.__contains__("failed")):
        print("failed")
else:
    print(post_res.status_code)
    print(post_res.text)
    #print(post_res.text)

sessionuser=requests.Session()
login_csrf_response=sessionuser.get("http://192.168.0.178:8080/login/")
login_csrf=login_csrf_response.cookies.get('csrftoken')
login_data={
"username": "venkat7venkatesh77@gmail.com",
"password": "@Venkystark77",
# "username": "vprocess-operator@gmail.com",
# "password": "123",
"req_id": generate_uuid(),
"csrfmiddlewaretoken": login_csrf
}
login_response=session.post("http://192.168.0.178:8080/entry/login_check",data=login_data)
if login_response.ok:
    print("loggin success")
    print(login_response.text)
    usertext=login_response.text
if(brokentext==usertext):
    print("matchfound")
else:
    print("nope")