import requests
from mes.otheruser import get_other_user_session
#from mqtt.test import get_session
import json
#main
session=get_other_user_session()
# post_res=session.post("http://192.168.0.178:8080/parts",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),
# "part_no":"wilogin","part_cost":5
# },headers={'Referer':'http://192.168.0.178:8080/'})
post_res=session.get("http://192.168.0.178:8080/parts")
if post_res.ok:
    print("get successfully")
    #print(post_res)
    print(post_res.status_code)
    print(post_res.content)
    if(post_res.text.__contains__("failed")):
        print("failed")
else:
    print(post_res.status_code)
    print(post_res.text)
    #print(post_res.text)