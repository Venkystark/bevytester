import requests
from mes.otheruser import *
#from mqtt.test import get_session
import json
from bs4 import BeautifulSoup
#main
session=get_other_user_session()
# post_res=session.post("http://192.168.0.178:8080/parts",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),
# "part_no":"wilogin","part_cost":5
# },headers={'Referer':'http://192.168.0.178:8080/'})
# 
brokentext=""
usertext=""
post_res=session.get("http://192.168.0.178:8080/parts_page")
print(post_res)
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
login_csrf_response=sessionuser.get("http://192.168.0.178:8080/login")
login_csrf=login_csrf_response.cookies.get('csrftoken')
login_data={
# "username": "venkat7venkatesh77@gmail.com",
# "password": "@Venkystark77",
"username": "vstore-viewer@gmail.com",
"password": "123",
"req_id": generate_uuid(),
"csrfmiddlewaretoken": login_csrf
}
login_response=sessionuser.post("http://192.168.0.178:8080/entry/login_check",data=login_data)
if login_response.ok:
    print("login_res before",login_response.status_code)
    print("loggin success")
    print(login_response.text)
    login_response.status_code=400
print("after",login_response.status_code)
usertext=res=sessionuser.get("http://192.168.0.178:8080/parts_page").text
soup1 = BeautifulSoup(brokentext, 'html.parser')
soup2 = BeautifulSoup(usertext, 'html.parser')

# Extract body content
body_content1 = soup1.find('body').get_text().strip()
body_content2 = soup2.find('body').get_text().strip()

# Check if the body content is the same
if body_content1 == body_content2:
    print("The body content after text1 and text2 are the same.")
else:
    print("The body content after text1 and text2 are different.")