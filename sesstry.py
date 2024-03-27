import requests

session=requests.Session()
cookies={"Admin":"."}
print(session)

session.cookies.update(cookies)
print(session.cookies)
get_res=session.get("http://192.168.0.178:8080/bwiot/api/v1/mqttdashboard/")
if get_res.ok:
    print(get_res.status_code)
    print(get_res.text) #Admin	"96202d614fda45a98050e573951d5f1f"   http://192.168.0.178:8080/bwiot/api/v1/login_check/