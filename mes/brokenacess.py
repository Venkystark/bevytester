import requests
import uuid

password="123"
def generate_uuid():
    return str(uuid.uuid4())

def create_elements(session):
    #process elements
    res=session.post("https://smartfactory.bevywise.com/process",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"process_name":"ADeleteProcess","quality_check":"Yes"},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("processdelete created")
    else:
        print("error in creating processdelete")
    res=session.post("https://smartfactory.bevywise.com/process",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"process_name":"vmpprocess","quality_check":"Yes"},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("vmp process created")
    else:
        print("error in creating vmpprocess")
    res=session.post("https://smartfactory.bevywise.com/process",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"process_name":"process1","quality_check":"Yes"},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("proces1 created")
    else:
        print("error in creating process1")
    res=session.post("https://smartfactory.bevywise.com/process",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"process_name":"process2","quality_check":"Yes"},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("process2 created")
    else:
        print("error in creating process2") 
    #machine elements
    res=session.post("https://smartfactory.bevywise.com/machine",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"machine_id":"ADeleteMachine","process":"ADeleteProcess"},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("delete machine created")
    else:
        print("error in machinedelete")
    res=session.post("https://smartfactory.bevywise.com/machine",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"machine_id":"vmpmachine","process":"vmpprocess"},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("vmpmachine created")
    else:
        print("error in creating vmpmachine")
    #parts elements
    res=session.post("https://smartfactory.bevywise.com/parts",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"part_no":"ADeletePart","part_cost":5},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("part deletion created")
    else:
        print("error in creating part deletion")
    res=session.post("https://smartfactory.bevywise.com/parts",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"part_no":"part1","part_cost":5},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("part1 created")
    else:
        print("error in creating part1")
    res=session.post("https://smartfactory.bevywise.com/parts",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"part_no":"part2","part_cost":5},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("part2 created")
    else:
        print("error in creating part2")
    #cycle times
    res=res=session.post("https://smartfactory.bevywise.com/cycle_times",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"part_number":"part1",
                "process":"vmpprocess",
                "oporder":7,
                "part_ideal_cycle_time":5,
                "allowence":5,
                "part_per_cycle":5,
                "target_per_shift":"240",
                "quality_check":"sample",
                "parts_to_inspect":"",
                "inspect_interval":"1hr",
                "quality_parameter":'{"qty_parameter": {}, "min_value": {}, "max_value": {}}',
                "toolinfo_parameter":'{"tool_number": {}, "tool_name": {}, "tool_time": {}, "tool_contact_time": {}, "no_of_cycles": {}}'},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("cycle time for admin navigation created")
    else:
        print("error in creating cycle time for admin navigation")
    #rejection reasons
    res=session.post("https://smartfactory.bevywise.com/bad_quality_reason",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"department":"vmpprocess","reason":"admin navigation"},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("quality reason created for admin navigation")
    else:
        print("error in creating qualaity reason for admin navigation")
    #downtime reasons
    res=session.post("https://smartfactory.bevywise.com/downtime_reason",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"department": "vmpprocess","reason":"admin navigation","type":"availability","color":"#ffffff"},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("downtime reason created for admin navigation")
    else:
        print("error in creating downtime reason for admin navigation")
    #target
    res=session.post("https://smartfactory.bevywise.com/target",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"department":"vmpprocess","availability": 5,"performance": 5,"quality":5},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("target created for admin navigation")
    else:
        print("target for admin navigation")
    #consumables
    res=session.post("https://smartfactory.bevywise.com/consumable_page",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"consumable_number":"adminnavconsumable","consumable_cost":8},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print(res.text)
        print("consumable created for admin navigation")
    else:
        print(res.text)
        print("error in creating consumable for admin navigation")
    #customer
    res=session.post("https://smartfactory.bevywise.com/customer_page",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"customer_name":"adminnavcust","country":"adminnavcust"},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("customer created for admin navigation")
    else:
        print("error in creating customer for admin navigation")
    #vendor
    res=session.post("https://smartfactory.bevywise.com/vendor_page",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"vendor_name":"adminnavvendor"},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("vendor created for admin navigation")
    else:
        print("error in creating vendor for admin navigation")
    #raw material for mrp
    res=session.post("https://smartfactory.bevywise.com/rm_vs_parts_page",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"part_name":"part1","raw_material":"vmp raw material","part_rm_factor":1},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("raw material assigned for mrp created")
    else:
        print("error in assigning raw material for mrp")

def create_users(session):
    res=session.post("https://smartfactory.bevywise.com/employee",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"department":"vmpprocess","employee_id":"vprocess-operator1@gmail.com","first_name":"process","last_name":"operator1", "role":"operator","password":password,"role_id":1},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("process-operator created")
    else:
        print("error in creating process-operator")
    res=session.post("https://smartfactory.bevywise.com/employee",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"department":"vmpprocess","employee_id":"vprocess-supervisor1@gmail.com", "role":"supervisor","password":password,"role_id":2},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print(res.json())
        print("process supervisor created")
        print(res.status_code)
        print(res.text)
        supsess=get_ba_session("BA_PS")
        op_res=supsess.post("https://smartfactory.bevywise.com/ppc/machine_list_op/",data={"csrfmiddlewaretoken":supsess.cookies.get('csrftoken'),"assign_operator":"process operator1","assign_machine":"vmpmachine","line_no":"vmpprocess","op_list":'["process_operator1"]'},headers={'Referer':'https://smartfactory.bevywise.com/'})
        if op_res.ok:
            print("process-operator is assigned")
        else:
            print(op_res.status_code)
            print(op_res.text)
            print("trouble in assigning process-operator")
    else:
        print("error in creating process-supervisor")
    res=session.post("https://smartfactory.bevywise.com/employee",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"department":"vmpprocess","employee_id":"vprocess-head1@gmail.com", "role":"Department Head","password":password,"role_id":3},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("process head created")
    else:
        print("error in creating process-head")
    res=session.post("https://smartfactory.bevywise.com/employee",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"department":"store","employee_id":"vstore-executive1@gmail.com", "role":"Executive","password":password,"role_id":6},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("store-executive created")
    else:
        print("error in creating store-executive")
    res=session.post("https://smartfactory.bevywise.com/employee",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"department":"store","employee_id":"vstore-manager1@gmail.com", "role":"Manager","password":password,"role_id":7},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("store-manager created")
    else:
        print("error in creating store-manager")
    res=session.post("https://smartfactory.bevywise.com/employee",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"department":"store","employee_id":"vstore-viewer1@gmail.com", "role":"Viewer","password":password,"role_id":8},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("store-viewer created")
    else:
        print("error in creating store-viewer")
    res=session.post("https://smartfactory.bevywise.com/employee",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"department":"maintenance","employee_id":"vmain-executive1@gmail.com", "role":"Executive","password":password,"role_id":4},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("main-executive created")
    else:
        print("error in creating main-executive")
    res=session.post("https://smartfactory.bevywise.com/employee",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),"department":"maintenance","employee_id":"vmain-manager1@gmail.com", "role":"Manager","password":password,"role_id":5},headers={'Referer':'https://smartfactory.bevywise.com/'})
    if res.ok:
        print("main-manager created")
    else:
        print("error in creating main-manager")
def login(user):
    if(user=="BA_SE"):
        userId="vstore-executive1@gmail.com"
    elif(user=="BA_SM"):
        userId="vstore-manager1@gmail.com"
    elif(user=="BA_SV"):
        userId="vstore-viewer1@gmail.com"
    elif(user=="BA_ME"):
        userId="vmain-executive1@gmail.com"
    elif(user=="BA_MM"):
        userId="vmain-manager1@gmail.com"
    elif(user=="BA_PH"):
        userId="vprocess-head1@gmail.com"
    elif(user=="BA_PS"):
        userId="vprocess-supervisor1@gmail.com"
    elif(user=="BA_PO"):
        userId="vprocess-operator1@gmail.com"  
    broken=requests.Session()
    login_csrf_response=broken.get("https://smartfactory.bevywise.com/login/")
    login_csrf=login_csrf_response.cookies.get('csrftoken')
    login_data={
    "username": userId,
    "password": password,
    "req_id": generate_uuid(),
    "csrfmiddlewaretoken": login_csrf
    }
    login_response=broken.post("https://smartfactory.bevywise.com/entry/login_check",data=login_data)
    if login_response.ok:
        print(userId,"user loggedin successfully")
        print(login_response.json())
        return broken   
    else:
        print("failed in user login")
        print(login_response.status_code)
def get_ba_session(user):
    return login(user)