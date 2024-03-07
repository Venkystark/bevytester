import requests
import uuid
import json
from mes.otheruser import *
from mes.brokenacess import *

#comit check
def append_details(payload,csrf,id=None,data=None):
    if(id==None and data==None):
        payload["csrfmiddlewaretoken"]=csrf
    elif(id!=None and data==None):
        payload["id"]=id
        payload["csrfmiddlewaretoken"]=csrf
    else:
        for item in data['data']:
            if item['id']==id:
                payload['id']=id
                payload['csrfmiddlewaretoken']=csrf
                payload['email_id']=item['employee_no']
    return payload
def delete_elements(session,url,endpoint,payload):
    res=session.get(url)
    if res.ok:
        data=res.json()
        id_values=[item['id']for item in data['data']]
        print("Ids in:",url,"are",id_values)
        print(endpoint)
        for id in id_values:
            if(endpoint=="http://192.168.0.178:8080/emp_master_delete_emp"):
                payload=append_details(payload,session.cookies.get('csrftoken'),id,data)
            else:
                payload=append_details(payload,session.cookies.get('csrftoken'),id)
            print(payload)
            del_res=session.post(endpoint,data=payload,headers={'Referer':'http://192.168.0.178:8080'})
            if del_res.ok:
                print("success")
            else:
                print(del_res.text)
def get_element(session,url):
    res=session.get(url)
    if res.ok:
        data=res.json()
        if(url=="http://192.168.0.178:8080/process"):
            id_values=[item['id'] for item in data['data'] if item["process_name"] != "vmpprocess" and item["process_name"]!="process1" and item["process_name"]!="process2"]
        elif(url=="http://192.168.0.178:8080/machine"):
            id_values=[item['id'] for item in data['data'] if item["machine_id"] != "vmpmachine"]
        elif(url=="http://192.168.0.178:8080/parts"):
            id_values=[item['id'] for item in data['data'] if item["part_no"] != "part1" and item["part_no"]!="part2"]
        else:
            id_values=[item['id']for item in data['data']]
        return id_values[0]
    else:
        print("error getting endpoint")
def get_theif_session(cookies):
    session=requests.Session()
    session.cookies.update(cookies)
    session.get("http://192.168.0.178:8080/login")
    return session
def generate_uuid():
    return str(uuid.uuid4())
def mes_test():
    session=requests.Session()
    login_csrf_response=session.get("http://192.168.0.178:8080/login/")
    login_csrf=login_csrf_response.cookies.get('csrftoken')
    login_data={
        "username": "venkat7venkatesh77@gmail.com",
        "password": "@Venkystark77",
        "req_id": generate_uuid(),
        "csrfmiddlewaretoken": login_csrf
    }
    login_response=session.post("http://192.168.0.178:8080/entry/login_check",data=login_data)
    if login_response.ok:
        #importing the json file
        print(session)
        print("session cookies:",session.cookies)
        with open('mes\\urlfiles.json') as json_file:
            json_data = json.load(json_file)
        #deleting existing data in all pages
        for top_key in json_data:
            sub_json=json_data[top_key]
            for sub_key in sub_json:
                if(sub_key=="http://192.168.0.178:8080/master_delete" or sub_key=="http://192.168.0.178:8080/emp_master_delete_emp"):
                    inner_json=sub_json[sub_key]
                    delete_elements(session,url,sub_key,inner_json["from_other_user"])
                else:
                    url=sub_key
        #creating users in employee page
        create_elements(session)
        create_users(session)
        for top_key in json_data: #topKey refers to the top url,sub key is api,inner keys are attack payloads
            sub_json=json_data[top_key]
            for sub_key in sub_json:
                inner_json=sub_json[sub_key]
                for inner_key in inner_json:
                    if(sub_key!="http://192.168.0.178:8080/master_delete"):
                        url=sub_key
                    if(inner_key=="from_other_user"):
                        outsider_session=get_other_user_session()
                        if(sub_key=="http://192.168.0.178:8080/master_delete"):
                            id=get_element(session,url)
                            print("got id in other_user attack:",id)
                            inner_json[inner_key]=append_details(inner_json[inner_key],theif_session.cookies.get('csrftoken'),id)
                        else:
                            inner_json[inner_key]=append_details(inner_json[inner_key],session.cookies.get('csrftoken'))
                        attack_res=outsider_session.post(sub_key,data=inner_json[inner_key],headers={'Referer':'http://192.168.0.178:8080'})
                    elif(inner_key=="session_cookies_theft"):
                        theif_session=get_theif_session(session.cookies)
                        if(sub_key=="http://192.168.0.178:8080/master_delete"):
                            id=get_element(theif_session,url)
                            print("got id in theif sesseion attack:",id)
                            inner_json[inner_key]=append_details(inner_json[inner_key],theif_session.cookies.get('csrftoken'),id)
                        else:
                            inner_json[inner_key]=append_details(inner_json[inner_key],theif_session.cookies.get('csrftoken'))
                        attack_res=theif_session.post(sub_key,data=inner_json[inner_key],headers={'Referer':'http://192.168.0.178:8080'})
                    elif(inner_key=="BA_SE" or inner_key=="BA_SM" or inner_key=="BA_SV" or inner_key=="BA_ME" or inner_key=="BA_MM" or inner_key=="BA_PH" or inner_key=="BA_PS" or inner_key=="BA_PO"):
                        broken=get_ba_session(inner_key)
                        attack_res=broken.get(top_key)
                    else:
                        inner_json[inner_key]=append_details(inner_json[inner_key],session.cookies.get('csrftoken'))
                        print("in for loop",inner_json[inner_key])
                        attack_res=session.post(sub_key,data=inner_json[inner_key],headers={'Referer':'http://192.168.0.178:8080'})
                    if(sub_key!="http://192.168.0.178:8080/master_delete"):
                        if(inner_key=="xss_attack" or inner_key=="html_attack"):
                            if attack_res.text.__contains__("failed"):
                                s_code=250
                            else:
                                s_code=attack_res.status_code
                            report_res={
                            "Page":top_key,
                            "Attack":inner_key,
                            "Statuscode":s_code                      
                            }
                        else:
                            report_res={
                            "Page":top_key,
                            "Attack":inner_key,
                            "Statuscode":attack_res.status_code                     
                            }
                        try:
                            with open('mes\\mes_attack_report.json','r') as file:
                                data=json.load(file)
                        except FileNotFoundError:
                            data=[]
                        data.append(report_res)
                        with open('mes\\mes_attack_report.json','w') as file:
                            json.dump(data,file,indent=4)
                    if attack_res.ok:
                        print('success')
                        attack_result = {
                            "Page":top_key,
                            "Endpoint":sub_key,
                            "Attack":inner_key,
                            "Payload":inner_json[inner_key],
                            "Statuscode":attack_res.status_code,
                            "AttackResponse":attack_res.text
                        }
                        # Write the attack result to a JSON file
                        try:
                            with open('mes\\mes_success_attacks.json', 'r') as file:
                                data = json.load(file)
                        except FileNotFoundError:
                            data = []
                        data.append(attack_result)
                        with open('mes\\mes_success_attacks.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    else:
                        attack_result = {
                            "Page":top_key,
                            "Endpoint":sub_key,
                            "Attack":inner_key,
                            "Payload":inner_json[inner_key],
                            "Statuscode":attack_res.status_code,
                            "AttackResponse":attack_res.text
                        }
                        # Write the attack result to a JSON file
                        try:
                            with open('mes\\mes_failure_attacks.json', 'r') as file:
                                data = json.load(file)
                        except FileNotFoundError:
                            data = []
                        data.append(attack_result)
                        with open('mes\\mes_failure_attacks.json', 'w') as file:
                            json.dump(data, file, indent=4)