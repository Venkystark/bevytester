import requests

session=requests.Session()
# cookies={"Admin":"."}
# print(session)

# session.cookies.update(cookies)
# print(session.cookies)
# get_res=session.get("http://192.168.0.178:8080/bwiot/api/v1/mqttdashboard/")
# if get_res.ok:
#     print(get_res.status_code)
#     print(get_res.text) #Admin	"96202d614fda45a98050e573951d5f1f"   http://192.168.0.178:8080/bwiot/api/v1/login_check/
cookies={"sessionid":"zrtwuvmm6pe08vlq94q4rrwt9fw4lpg2","csrftoken":"e7ielphXu5Rgrd2doryyGQ6z5Qes1CKW3LfkB8ZbsYd67c0PkWTFa0TGHXfrTPmw"}
session.cookies.update(cookies)
login_res=session.post("https://publicmqtt.bevywise.com/bwiot/api/v1/admin/getDashboardList",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken')},headers={'Referer':'https://publicmqtt.bevywise.com/'})
if login_res.ok:
    print(login_res.json())
    print(login_res.status_code)
    print("login success")
    auth_res=session.get("https://publicmqtt.bevywise.com/bwiot/api/v1/admin/getUserPermission")
    if auth_res.ok:
        print(auth_res.json())
else:
    print(login_res.status_code)
    print(login_res.json)