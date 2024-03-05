import requests
from mes.otheruser import get_other_user_session
#from mqtt.test import get_session
import json
#main
session=get_other_user_session()
# post_res=session.post("https://publicmqtt.bevywise.com/bwiot/api/v1/admin/createUser",data={"display_name":"from other user","username":"other_user@gmail.com",
# "mobile_no": 44444444444,
# "permission": 1,
# "csrfmiddlewaretoken":session.cookies.get('csrftoken')},headers={'Referer':'https://publicmqtt.bevywise.com/'})
#post_res=session.post("https://mes.bevywise.com/target",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"department":"<button>hello target</button>","availability": 5,"performance": 5,"quality":5},headers={'Referer':'https://mes.bevywise.com/'})
post_res=session.post("https://mes.bevywise.com/process",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"process_name":"broken","quality_check":"Yes"},headers={'Referer':'https://mes.bevywise.com/'})
if post_res.ok:
    print("posted successfully")
    #print(post_res)
    print(post_res.status_code)
    print(post_res.is_redirect)
    print(post_res.content)
    #print(post_res.text)
    if(post_res.text.__contains__("failed")):
        print("failed")
else:
    print(post_res.status_code)
    print(post_res.text)
    #print(post_res.text)