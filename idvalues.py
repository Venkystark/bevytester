import requests
from mes.otheruser import get_other_user_session
import json

session=get_other_user_session()
res=session.get("http://192.168.0.178:8080/process")
if res.ok:
    data=res.json()
    #id_values=[item['id']for item in data['data']]
    id_values=[item['id'] for item in data['data'] if item["process_name"] != "broken" and item["process_name"]!="brok"]
    print(id_values)
else:
    print(res.status_code)
    print(res.text)
    print("cant get")