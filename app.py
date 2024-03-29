import json
import os
from flask import Flask,render_template, request,jsonify,redirect, url_for
app = Flask(__name__)
# from mes.test import *
from mes.test2 import *
from mes.otheruser import *
from mes.brokenacess import *
from mqtt.mqtttest import *

# Define a global variable
selected_option = None

@app.route('/')
def index():
    # Pass the variable to the HTML template
    return render_template('index.html', selected_option=selected_option)
@app.route('/attack_results')
def attack_results():
    with open('mes\\mes_success_attacks.json') as json_file:
            success_data = json.load(json_file)
    with open('mes\\mes_failure_attacks.json') as json_file:
            failure_data = json.load(json_file)
    return render_template('attack_results.html',success_data=success_data,failure_data=failure_data)
@app.route('/attack_report')
def attack_report():
    with open('mes\\mes_final_report.json', 'r') as file:
            report_data = json.load(file)
    return render_template('attack_report.html',data=report_data)

#MQTT URLS
@app.route('/mqtt_attack_report')
def mqtt_attack_report():
    with open('mqtt\\mqtt_final_report.json', 'r') as file:
            report_data = json.load(file)
    return render_template('mqtt_attack_report.html',data=report_data)

@app.route('/update', methods=['POST'])
def update():
    global selected_option
    # Get the selected option from the form
    selected_option = request.form['option']
    # Redirect to the main page
    if(selected_option=="mes"):
        if os.path.exists("mes\\mes_success_attacks.json"):
            os.remove("mes\\mes_success_attacks.json")
        if os.path.exists("mes\\mes_failure_attacks.json"):
            os.remove("mes\\mes_failure_attacks.json")
        if os.path.exists("mes\\mes_attack_report.json"):
            os.remove("mes\\mes_attack_report.json")
        if os.path.exists("mes\\mes_final_report.json"):
            os.remove("mes\\mes_final_report.json")
        #mes_test()
        mes_testv2()
        with open('mes\\mes_attack_report.json', 'r') as file:
            data = json.load(file)

        # Create a dictionary to store the results
        result_dict = {}
        # Iterate through each entry in the original JSON data
        for entry in data:
            page = entry['Page']
            attack = entry['Attack']
            status_code = entry['Statuscode']

            # Determine the success value based on the status code
            
            success = "success" if status_code == 200 else "failure"

            # Update the result_dict with the corresponding values
            if page not in result_dict:
                result_dict[page] = {}

            result_dict[page][attack] = success
        pages=["https://smartfactory.bevywise.com/cycle_page","https://smartfactory.bevywise.com/targets","https://smartfactory.bevywise.com/rm_vs_parts","https://smartfactory.bevywise.com/customer","https://smartfactory.bevywise.com/employee_page","https://smartfactory.bevywise.com/management/","https://smartfactory.bevywise.com/store/#Dashboard","https://smartfactory.bevywise.com/mrp/ppc_dashboard/","https://smartfactory.bevywise.com/department/","https://smartfactory.bevywise.com/maintenance/main_dashboard/#Dashboard"]
        for page in pages:
            result_dict[page]["fileupload"]="-"
        attacks=["xss_attack","html_attack","from_other_user","session_cookies_theft","BA_MM"]
        for attack in attacks:
            result_dict["https://smartfactory.bevywise.com/maintenance/main_dashboard/#Dashboard"][attack]="-"
        pages=["https://smartfactory.bevywise.com/management/","https://smartfactory.bevywise.com/mrp/ppc_dashboard/","https://smartfactory.bevywise.com/department/"]
        for page in pages:
            result_dict[page]["from_other_user"]="-"
        attacks=["from_other_user","BA_SE","BA_SM"]
        for attack in attacks:
            result_dict["https://smartfactory.bevywise.com/store/#Dashboard"][attack]="-"
        result_dict["https://smartfactory.bevywise.com/department/"]["BA_PH"]="-"
        # Write the result_dict to a new JSON file
        with open('mes\\mes_final_report.json', 'w') as output_file:
            json.dump(result_dict, output_file, indent=2)
    #return render_template('attack_results.html',success_data=success_data,failure_data=failure_data)
        with open('mes\\mes_final_report.json', 'r') as file:
            report_data = json.load(file)
        #return render_template('attack_report.html',data=report_data)
        return redirect(url_for('attack_report'))
    if(selected_option=="mqtt"):
        if os.path.exists("mqtt\\mqtt_attack_report.json"):
            os.remove("mqtt\\mqtt_attack_report.json")
        if os.path.exists("mqtt\\mqtt_final_report.json"):
            os.remove("mqtt\\mqtt_final_report.json")
        mqtt_test()
        with open('mqtt\\mqtt_attack_report.json', 'r') as file:
            data = json.load(file)

        # Create a dictionary to store the results
        result_dict = {}
        # Iterate through each entry in the original JSON data
        for entry in data:
            page = entry['Page']
            attack = entry['Attack']
            status_code = entry['Statuscode']

            # Determine the success value based on the status code
            
            success = "success" if status_code == 200 else "failure"

            # Update the result_dict with the corresponding values
            if page not in result_dict:
                result_dict[page] = {}

            result_dict[page][attack] = success
        result_dict["https://publicmqtt.bevywise.com/#dashboard"]["BA_ADMIN"]="-"
        pages=["https://publicmqtt.bevywise.com/#settings-user/Administrative_User","https://publicmqtt.bevywise.com/#settings-user/Standard_User"]
        attacks=["xss_attack","html_attack","session_cookies_theft"]
        for page in pages:
            for attack in attacks:
                result_dict[page][attack]="-"
        with open('mqtt\\mqtt_final_report.json', 'w') as output_file:
            json.dump(result_dict, output_file, indent=2)
        return redirect(url_for('mqtt_attack_report'))
if __name__ == '__main__':
    app.run(debug=True)
