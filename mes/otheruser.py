import uuid
import requests

def generate_uuid():
    return str(uuid.uuid4())
def other_user_login():
    session=requests.Session()
    login_csrf_response=session.get("http://192.168.0.178:8080/login/")
    login_csrf=login_csrf_response.cookies.get('csrftoken')
    login_data={
    "username": "venkateshv2508@gmail.com",
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
        #print(login_response.json())
        return session
def get_other_user_session():
    return other_user_login()