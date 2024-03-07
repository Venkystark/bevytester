import requests
from mes.otheruser import get_other_user_session
#from mqtt.test import get_session
import json
#main
session=get_other_user_session()
post_res=session.post("http://192.168.0.178:8080/store/productionparts/",data={"csrfmiddlewaretoken":session.cookies.get('csrftoken'),
"date": "2024-02-28","material_name": "<script>console.log(\"script inventory\");</script>","material_id": "-","total_inwards": "8","quality_check": "yes","rejection": "2","available": "6","material_type": "Tools" 
},headers={'Referer':'http://192.168.0.178:8080/'})
if post_res.ok:
    print("posted successfully")
    #print(post_res)
    print(post_res.status_code)
    print(post_res.content)
    if(post_res.text.__contains__("failed")):
        print("failed")
else:
    print(post_res.status_code)
    print(post_res.text)
    #print(post_res.text)