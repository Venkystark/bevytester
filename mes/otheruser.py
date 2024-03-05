import uuid
import requests

def generate_uuid():
    return str(uuid.uuid4())
def other_user_login():
    session=requests.Session()
    login_csrf_response=session.get("https://mes.bevywise.com/login/")
    login_csrf=login_csrf_response.cookies.get('csrftoken')
    login_data={
    "username": "sivagurubalans@gmail.com",
    "password": "Admin@123",
    # "username": "store-executive@gmail.com",
    # "password": "123",
    "req_id": generate_uuid(),
    "csrfmiddlewaretoken": login_csrf
    }
    login_response=session.post("https://mes.bevywise.com/entry/login_check",data=login_data)
    if login_response.ok:
        print("loggin success")
        print(login_response.text)
        #print(login_response.json())
        return session
def get_other_user_session():
    return other_user_login()