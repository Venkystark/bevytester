import requests
import uuid

password="123"
def generate_uuid():
    return str(uuid.uuid4())

def create_elements(session):
    #process elements
    res=session.post("http://192.168.0.178:8080/process",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"process_name":"ADeleteProcess","quality_check":"Yes"},headers={'Referer':'http://192.168.0.178:8080/'})
    if res.ok:
        print("process for deletion created")
    else:
        print("error in creating process for deletion")
    res=session.post("http://192.168.0.178:8080/process",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"process_name":"process1","quality_check":"Yes"},headers={'Referer':'http://192.168.0.178:8080/'})
    if res.ok:
        print("proces1 created")
    else:
        print("error in creating process p1")
    res=session.post("http://192.168.0.178:8080/process",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"process_name":"process2","quality_check":"Yes"},headers={'Referer':'http://192.168.0.178:8080/'})
    if res.ok:
        print("process2 created")
    else:
        print("error in creating process p2") 
    #machine elements
    res=session.post("http://192.168.0.178:8080/machine",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"machine_id":"ADeleteMachine","process":"ADeleteProcess"},headers={'Referer':'http://192.168.0.178:8080/'})
    if res.ok:
        print("machine for deletion created")
    else:
        print("error in creating machine for deletion")
    #parts elements
    res=session.post("http://192.168.0.178:8080/parts",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"part_no":"ADeletePart"},headers={'Referer':'http://192.168.0.178:8080/'})
    if res.ok:
        print("part for deletion created")
    else:
        print("error in creating part for deletion")
    res=session.post("http://192.168.0.178:8080/parts",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"part_no":"part1"},headers={'Referer':'http://192.168.0.178:8080/'})
    if res.ok:
        print("part1 created")
    else:
        print("error in creating part1")
    res=session.post("http://192.168.0.178:8080/parts",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"part_no":"part2"},headers={'Referer':'http://192.168.0.178:8080/'})
    if res.ok:
        print("part2 created")
    else:
        print("error in creating part2")
    #tools elements
    res=session.post("http://192.168.0.178:8080/tools_page",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"tools_number": "ADeleteTool","process":"Delete"},headers={'Referer':'http://192.168.0.178:8080/'})
    if res.ok:
        print("tool for deletion created")
    else:
        print("error in creating tool for deletion")

def create_users(session):
    res=session.post("http://192.168.0.178:8080/process",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"process_name":"vmpprocess","quality_check":"Yes"},headers={'Referer':'http://192.168.0.178:8080/'})
    if res.ok:
        print("process for employee created successfully")
    else:
        print("error in creating process for employee")
    res=session.post("http://192.168.0.178:8080/machine",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"machine_id":"vmpmachine","process":"vmpprocess"},headers={'Referer':'http://192.168.0.178:8080/'})
    if res.ok:
        print("machine for employee created successfully")
    else:
        print("error in creating process for machine")
    res=session.post("http://192.168.0.178:8080/employee",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"department":"vmpprocess","employee_id":"process-operator@gmail.com","first_name":"process","last_name":"operator", "role":"operator","password":password,"role_id":1},headers={'Referer':'http://192.168.0.178:8080/'})
    if res.ok:
        print("process-operator created")
    else:
        print("error in creating process-operator")
    res=session.post("http://192.168.0.178:8080/employee",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"department":"vmpprocess","employee_id":"process-supervisor@gmail.com", "role":"supervisor","password":password,"role_id":3},headers={'Referer':'http://192.168.0.178:8080/'})
    if res.ok:
        print("process supervisor created")
        supsess=get_ba_session("BA_PS")
        op_res=supsess.post("http://192.168.0.178:8080/ppc/machine_list_op/",data={"csrfmiddlewaretoken":supsess.cookies.get('csrftoken'),"assign_operator":"process operator","assign_machine":"vmpmachine"},headers={'Referer':'http://192.168.0.178:8080/'})
        if op_res.ok:
            print("process-operator is assigned")
        else:
            print("trouble in assigning process-operator")
    else:
        print("error in creating process-supervisor")
    res=session.post("http://192.168.0.178:8080/employee",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"department":"store","employee_id":"store-executive@gmail.com", "role":"Executive","password":password,"role_id":11},headers={'Referer':'http://192.168.0.178:8080/'})
    if res.ok:
        print("store-executive created")
    else:
        print("error in creating store-executive")
    res=session.post("http://192.168.0.178:8080/employee",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"department":"store","employee_id":"store-manager@gmail.com", "role":"Manager","password":password,"role_id":12},headers={'Referer':'http://192.168.0.178:8080/'})
    if res.ok:
        print("store-manager created")
    else:
        print("error in creating store-manager")
    res=session.post("http://192.168.0.178:8080/employee",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"department":"store","employee_id":"store-viewer@gmail.com", "role":"Viewer","password":password,"role_id":13},headers={'Referer':'http://192.168.0.178:8080/'})
    if res.ok:
        print("store-viewer created")
    else:
        print("error in creating store-viewer")
    res=session.post("http://192.168.0.178:8080/employee",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"department":"maintenance","employee_id":"main-executive@gmail.com", "role":"Executive","password":password,"role_id":9},headers={'Referer':'http://192.168.0.178:8080/'})
    if res.ok:
        print("main-executive created")
    else:
        print("error in creating main-executive")
    res=session.post("http://192.168.0.178:8080/employee",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"department":"maintenance","employee_id":"main-manager@gmail.com", "role":"Manager","password":password,"role_id":10},headers={'Referer':'http://192.168.0.178:8080/'})
    if res.ok:
        print("main-manager created")
    else:
        print("error in creating main-manager")
    res=session.post("http://192.168.0.178:8080/employee",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"department":"vmpprocess","employee_id":"process-head@gmail.com", "role":"Department Head","password":password,"role_id":4},headers={'Referer':'http://192.168.0.178:8080/'})
    if res.ok:
        print("process head created")
    else:
        print("error in creating process-head")
def login(user):
    if(user=="BA_SE"):
        userId="store-executive@gmail.com"
    elif(user=="BA_SM"):
        userId="store-manager@gmail.com"
    elif(user=="BA_SV"):
        userId="store-viewer@gmail.com"
    elif(user=="BA_ME"):
        userId="main-executive@gmail.com"
    elif(user=="BA_MM"):
        userId="main-manager@gmail.com"
    elif(user=="BA_PH"):
        userId="process-head@gmail.com"
    elif(user=="BA_PS"):
        userId="process-supervisor@gmail.com"
    elif(user=="BA_PO"):
        userId="process-operator@gmail.com"  
    broken=requests.Session()
    login_csrf_response=broken.get("http://192.168.0.178:8080/login/")
    login_csrf=login_csrf_response.cookies.get('csrftoken')
    login_data={
    "username": userId,
    "password": password,
    "req_id": generate_uuid(),
    "csrfmiddlewaretoken": login_csrf
    }
    login_response=broken.post("http://192.168.0.178:8080/entry/login_check",data=login_data)
    if login_response.ok:
        print(userId,"user loggedin successfully")
        print(login_response.json())
        return broken   
    else:
        print("failed in user login")
def get_ba_session(user):
    return login(user)