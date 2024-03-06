import requests
import uuid
import json

def generate_uuid():
    return str(uuid.uuid4())
session=requests.Session()
login_csrf_response=session.get("http://192.168.0.178:8080/login/")
login_csrf=login_csrf_response.cookies.get('csrftoken')
print("login_csrf:",login_csrf)
login_data={
    "username": "venkat7venkatesh77@gmail.com",
    "password": "@Venkystark77",
    "req_id": generate_uuid(),
    "csrfmiddlewaretoken": login_csrf
}
login_response=session.post("http://192.168.0.178:8080/entry/login_check",data=login_data)
if login_response.ok:
    print("login successs")
    print("session_after_login",session)
    print("login_response_csrf",login_response.cookies.get('csrftoken'))
    print("session_csrf.......",session.cookies.get('csrftoken'))
    page_csrf=session.get('http://192.168.0.178:8080/process_page').cookies.get('csrftoken')
    print("page url access:")
    print(session.get("http://192.168.0.178:8080/process_page").status_code)
    print("process_page_csrf..",page_csrf)
    csrftoken=session.cookies.get('csrftoken')
    input_data={
        "csrfmiddlewaretoken":csrftoken,
        "process_name":"from python3"
    }
    post_res=session.post("http://192.168.0.178:8080/process",data=input_data,headers={'Referer': 'http://192.168.0.178:8080'})
    if post_res.ok:
        print("success")
    else:
        print("failure")
        print(post_res.status_code)
        print(post_res.text)