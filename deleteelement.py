import uuid
import requests
import json

def generate_uuid():
    return str(uuid.uuid4())

session1 = requests.Session()

# Perform login
login_csrf_response = session1.get("https://smartfactory.bevywise.com/login")
login_csrf = login_csrf_response.cookies.get('csrftoken')
login_data = {
    "username": "venkat7venkatesh77@gmail.com",
    "password": "@Venkystark77",
    "req_id": generate_uuid(),
    "csrfmiddlewaretoken": login_csrf
}
login_response = session1.post("https://smartfactory.bevywise.com/entry/login_check", data=login_data)

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
if login_response.ok:
    with open('mes\\urlfiles.json') as json_file:
            json_data = json.load(json_file)
    for top_key in json_data:
        sub_json=json_data[top_key]
        for sub_key in sub_json:
            if(sub_key=="https://smartfactory.bevywise.com/master_delete" or sub_key=="https://smartfactory.bevywise.com/emp_master_delete_emp"):
                inner_json=sub_json[sub_key]
                delete_elements(session1,url,sub_key,inner_json["from_other_user"])
            else:
                url=sub_key

#     # Make the GET request to retrieve process data
#     response = session1.get('https://smartfactory.bevywise.com/process')

#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Parse the JSON response
#         data = response.json()

#         # Extract the id values
#         id_values = [item['id'] for item in data['data']]

#         # Print the id values
#         print("ID Values:", id_values)

#     else:
#         # Print an error message if the request was not successful
#         print('Failed to retrieve data:', response.status_code)

# else:
#     print("Login failed")
