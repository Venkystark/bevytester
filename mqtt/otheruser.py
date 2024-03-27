import requests

def login(inner_key):
    session2=requests.Session()
    if(inner_key=="from_other_user"):
        login_res=session2.post("https://publicmqtt.bevywise.com/login/",data={"username":"venkat7venkatesh77@gmail.com","password":"@Venkystark77"},headers={'Referer':'https://publicmqtt.bevywise.com/'})
    elif(inner_key=="BA_ADMIN"):
        login_res=session2.post("https://publicmqtt.bevywise.com/login/",data={"username":"ssgbs92@gmail.com","password":"@Venkystark77"},headers={'Referer':'https://publicmqtt.bevywise.com/'})
    elif(inner_key=="BA_STANDARD"):
        login_res=session2.post("https://publicmqtt.bevywise.com/login/",data={"username":"ssgbs92@gmail.com","password":"@Venkystark77"},headers={'Referer':'https://publicmqtt.bevywise.com/'})
    if login_res.ok:
        print(inner_key,"logged in")
        print(login_res.status_code)
        auth_res=session2.get("https://publicmqtt.bevywise.com/bwiot/api/v1/admin/getUserPermission")
        if auth_res.ok:
            print(auth_res.json())
        return session2
    else:
        print(login_res.status_code)
        print(login_res.text)

def get_other_user_session(inner_key):
    return login(inner_key)