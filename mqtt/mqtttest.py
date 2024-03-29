import json
import requests
import time
from mqtt.otheruser import *

#creating a theif session
def get_theif_session(cookies):
    session=requests.Session()
    session.cookies.update(cookies)
    session.get("https://publicmqtt.bevywise.com/")
    return session
#appending details
def append_details(payload,csrf,id=None):
    if(id!=None):
        payload['id']=id
    payload['csrfmiddlewaretoken']=csrf
    print(payload)
    return payload
#getting element id
def get_element(session,url):
    print("get element working")
    if(url=="https://publicmqtt.bevywise.com/bwiot/api/v1/graph/getReport/"):
        res=session.get(url)
    else:
        res=session.post(url,data={"csrfmiddlewaretoken":session.cookies.get('csrftoken')},headers={'Referer':'https://publicmqtt.bevywise.com/'})
    if res.ok:
        data=res.json()
        if(url=="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/getUsers"):
            id_values=[item['id'] for item in data['data']if item["id"]!=7 and item["id"]!=193 and item["id"]!=194]
        elif(url=="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/getDeviceGroup"):
            id_values=[item['id'] for item in data['data'] if item['id']!=123]
        elif(url=="https://publicmqtt.bevywise.com/bwiot/api/v1/rule_engine/get_rule_list"):
            id_values=[item['id'] for item in data['rules']]
        else:
            id_values=[item['id']for item in data['data']]
        print(id_values)
        return id_values[0]
    else:
        print(res.status_code)
        print(res.text)
#method for deleting elements in automation
def delete_elements(session,url,endpoint):
    if(url=="https://publicmqtt.bevywise.com/bwiot/api/v1/graph/getReport/"):
        res=session.get(url)
    else:
        res=session.post(url,data={"csrfmiddlewaretoken":session.cookies.get('csrftoken')},headers={'Referer':'https://publicmqtt.bevywise.com/'})
    if res.ok:
        data=res.json()
        if(url=="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/getUsers"):
            id_values=[item['id'] for item in data['data']if item["id"]!=7 and item["id"]!=193 and item["id"]!=194]
        elif(url=="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/getDeviceGroup"):
            id_values=[item['id'] for item in data['data'] if item['id']!=123]
        elif(url=="https://publicmqtt.bevywise.com/bwiot/api/v1/rule_engine/get_rule_list"):
            id_values=[item['id'] for item in data['rules']]
        else:
            id_values=[item['id']for item in data['data']]
        print("Ids in:",url,"are",id_values)
        print(endpoint)
        for id in id_values:
            if(endpoint=="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/removeUser"):
                payload={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"id":id}
            elif(endpoint=="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/removeDeviceGroup"):
                payload={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"group_id":id}
            elif(endpoint=="https://publicmqtt.bevywise.com/bwiot/api/v1/rule_engine/delete_rule"):
                payload={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"rule_id":id}
            elif(endpoint=="https://publicmqtt.bevywise.com/bwiot/api/v1/graph/deleteMainGraph/"):
                payload={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"report_id":id}
            else:
                payload={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"id":id}
            print(payload)
            del_res=session.post(endpoint,data=payload,headers={'Referer':'https://publicmqtt.bevywise.com/'})
            if del_res.ok:
                print("success")
            else:
                print('error in deleting in endpoint',endpoint)
                print(del_res.text)
    else:
        print("error in getting",url,"endpoint:",endpoint)
def mqtt_test():
    session=requests.Session()
    login_res=session.post("https://publicmqtt.bevywise.com/login/",data={"username":"v000044444@gmail.com","password":"@Venkystark77"},headers={'Referer':'https://publicmqtt.bevywise.com/'})
    if login_res.ok:
        print(login_res.status_code)
        print("login success")
        auth_res=session.get("https://publicmqtt.bevywise.com/bwiot/api/v1/admin/getUserPermission")
        if auth_res.ok:
            print(auth_res.json())
        with open('mqtt\\mqtturls.json') as json_file:
            json_data = json.load(json_file)
        #deleting data in all pages
        for top_key in json_data:
            sub_json=json_data[top_key]
            for sub_key in sub_json:
                if(sub_key=="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/removeUser" or sub_key=="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/removeDeviceGroup" 
                or sub_key=="https://publicmqtt.bevywise.com/bwiot/api/v1/rule_engine/delete_rule" or sub_key=="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/deleteDashboard" or sub_key=="https://publicmqtt.bevywise.com/bwiot/api/v1/graph/deleteMainGraph/"):
                    if(sub_key=="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/removeUser"):
                        url="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/getUsers"
                    elif(sub_key=="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/removeDeviceGroup"):
                        url="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/getDeviceGroup"
                    elif(sub_key=="https://publicmqtt.bevywise.com/bwiot/api/v1/rule_engine/delete_rule"):
                        url="https://publicmqtt.bevywise.com/bwiot/api/v1/rule_engine/get_rule_list"
                    elif(sub_key=="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/deleteDashboard"):
                        url="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/getDashboardList"
                    elif(sub_key=="https://publicmqtt.bevywise.com/bwiot/api/v1/graph/deleteMainGraph/"):
                        url="https://publicmqtt.bevywise.com/bwiot/api/v1/graph/getReport/"
                    delete_elements(session,url,sub_key)
        #starting the test
        for top_key in json_data: #topKey refers to the top url,sub key is api,inner keys are attack payloads
            sub_json=json_data[top_key]
            for sub_key in sub_json:
                inner_json=sub_json[sub_key]
                for inner_key in inner_json:
                    if(sub_key!="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/removeUser" and sub_key!="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/removeDeviceGroup"
                    and sub_key!="https://publicmqtt.bevywise.com/bwiot/api/v1/rule_engine/delete_rule" and sub_key!="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/deleteDashboard" and sub_key!="https://publicmqtt.bevywise.com/bwiot/api/v1/graph/deleteMainGraph/"):
                        if(sub_key=="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/createUser"):
                            url="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/getUsers"
                        elif(sub_key=="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/createDeviceGroup"):
                            url="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/getDeviceGroup"
                        elif(sub_key=="https://publicmqtt.bevywise.com/bwiot/api/v1/rule_engine/create_event_rule/device_alert"):
                            url="https://publicmqtt.bevywise.com/bwiot/api/v1/rule_engine/get_rule_list"
                        elif(sub_key=="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/createDashboard"):
                            url="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/getDashboardList"
                        elif(sub_key=="https://publicmqtt.bevywise.com/bwiot/api/v1/graph/createReport/"):
                            url="https://publicmqtt.bevywise.com/bwiot/api/v1/graph/getReport/"
                    if(inner_key=="xss_attack" or inner_key=="html_attack"):
                        inner_json[inner_key]=append_details(inner_json[inner_key],session.cookies.get('csrftoken'))
                        attack_res=session.post(sub_key,data=inner_json[inner_key],headers={'Referer':'https://publicmqtt.bevywise.com/'})
                    elif(inner_key=="session_cookies_theft"):
                        theif_session=get_theif_session(session.cookies)
                        inner_json[inner_key]=append_details(inner_json[inner_key],theif_session.cookies.get('csrftoken'))
                        attack_res=theif_session.post(sub_key,data=inner_json[inner_key],headers={'Referer':'https://publicmqtt.bevywise.com/'})
                    elif(inner_key=="from_other_user"):
                        outsider_session=get_other_user_session(inner_key)
                        if(top_key=="https://publicmqtt.bevywise.com/#settings-user/Administrative_User" or top_key=="https://publicmqtt.bevywise.com/#settings-user/Standard_User"):
                            inner_json[inner_key]=append_details(inner_json[inner_key],outsider_session.cookies.get('csrftoken'))
                        else:
                            id=get_element(session,url)#we need to get the elements of our user so we are passing session here
                            # outsider_session=get_other_user_session(inner_key)
                            if(url=="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/getDeviceGroup"):
                                inner_json[inner_key]['group_id']=id
                                inner_json[inner_key]=append_details(inner_json[inner_key],outsider_session.cookies.get('csrftoken'))
                            elif(url=="https://publicmqtt.bevywise.com/bwiot/api/v1/rule_engine/get_rule_list"):
                                inner_json[inner_key]['rule_id']=id
                                inner_json[inner_key]=append_details(inner_json[inner_key],outsider_session.cookies.get('csrftoken'))
                            elif(url=="https://publicmqtt.bevywise.com/bwiot/api/v1/graph/getReport/"):
                                inner_json[inner_key]['report_id']=id
                                inner_json[inner_key]=append_details(inner_json[inner_key],outsider_session.cookies.get('csrftoken'))
                            else:
                                inner_json[inner_key]=append_details(inner_json[inner_key],outsider_session.cookies.get('csrftoken'),id)
                        attack_res=outsider_session.post(sub_key,inner_json[inner_key],headers={'Referer':'https://publicmqtt.bevywise.com/'})
                    elif(inner_key=="BA_ADMIN" or inner_key=="BA_STANDARD"):
                        print("In broken access section")
                        broken=get_other_user_session(inner_key)
                        if top_key=="https://publicmqtt.bevywise.com/#settings-user/Administrative_User" or top_key=="https://publicmqtt.bevywise.com/#settings-user/Standard_User":
                            inner_json[inner_key]=append_details(inner_json[inner_key],broken.cookies.get('csrftoken'))
                        else:
                            if url=="https://publicmqtt.bevywise.com/bwiot/api/v1/graph/getReport/":
                                time.sleep(1)
                            id=get_element(session,url)
                            # broken=get_other_user_session(inner_key)
                            if(url=="https://publicmqtt.bevywise.com/bwiot/api/v1/admin/getDeviceGroup"):
                                inner_json[inner_key]['group_id']=id
                                inner_json[inner_key]=append_details(inner_json[inner_key],broken.cookies.get('csrftoken'))
                            elif(url=="https://publicmqtt.bevywise.com/bwiot/api/v1/rule_engine/get_rule_list"):
                                inner_json[inner_key]['rule_id']=id
                                inner_json[inner_key]=append_details(inner_json[inner_key],broken.get('csrftoken'))
                            elif(url=="https://publicmqtt.bevywise.com/bwiot/api/v1/graph/getReport/"):
                                inner_json[inner_key]['report_id']=id
                                inner_json[inner_key]=append_details(inner_json[inner_key],broken.cookies.get('csrftoken'))
                            else:
                                inner_json[inner_key]=append_details(inner_json[inner_key],broken.cookies.get('csrftoken'),id)
                        attack_res=broken.post(sub_key,inner_json[inner_key],headers={'Referer':'https://publicmqtt.bevywise.com/'})
                    print(attack_res.status_code)
                    print(attack_res.text)
                    if(attack_res.text.__contains__("Failed")):
                        attack_res.status_code=250
                    report_res={
                        "Page":top_key,
                        "Attack":inner_key,
                        "Statuscode":attack_res.status_code
                    }
                    try:
                        with open('mqtt\\mqtt_attack_report.json','r') as file:
                            data=json.load(file)
                    except FileNotFoundError:
                        data=[]
                    data.append(report_res)
                    with open('mqtt\\mqtt_attack_report.json','w') as file:
                        json.dump(data,file,indent=4)
    else:       
        print("login failed")
        print(login_res.status_code)
        print(login_res.text)