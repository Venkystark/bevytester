import uuid
import requests

def login():
    session=requests.Session()
    print("before login")
    br=session.get("https://publicmqtt.bevywise.com/bwiot/api/v1/admin/getUserPermission")
    if br.ok:
        print(br.json())
    else:
        print("nope")
    login_res=session.post("https://publicmqtt.bevywise.com/login/",data={"username":"venkat7venkatesh77@gmail.com","password":"@Venkystark77"},headers={'Referer':'https://publicmqtt.bevywise.com/'})
    if login_res.ok:
        print(login_res.status_code)
        print("After login")
        print("csrf:",session.cookies.get('csrftoken'))
        csrf_res=session.get("https://publicmqtt.bevywise.com/bwiot/api/v1/admin/getUserPermission")
        if csrf_res.ok:
            print(csrf_res.json())
    else:
        print(login_res.status_code)
        print(login_res.text)
    return session
def get_session():
    return login()