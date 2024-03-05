import json
import os
from flask import Flask,render_template, request,jsonify,redirect, url_for
app = Flask(__name__)
from mes.test import *
from mes.otheruser import *
from mes.brokenacess import *

#change in main branch
# Define a global variable
selected_option = None

@app.route('/')
def index():
    # Pass the variable to the HTML template
    return render_template('index.html', selected_option=selected_option)
@app.route('/attack_results')
def attack_results():
    return render_template('attack_results.html')
@app.route('/attack_report')
def attack_report():
    with open('mes\\mes_final_report.json', 'r') as file:
            report_data = json.load(file)
    return render_template('attack_report.html',data=report_data)

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
        mes_test()
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
        attacks=["xss_attack","html_attack","from_other_user","session_cookies_theft"]
        for attack in attacks:
            result_dict["https://mes.bevywise.com/maintenance/main_dashboard/#Dashboard"][attack]="-"
        # Write the result_dict to a new JSON file
        with open('mes\\mes_final_report.json', 'w') as output_file:
            json.dump(result_dict, output_file, indent=2)
        with open('mes\\mes_success_attacks.json') as json_file:
            success_data = json.load(json_file)
        with open('mes\\mes_failure_attacks.json') as json_file:
            failure_data = json.load(json_file)
    #return render_template('attack_results.html',success_data=success_data,failure_data=failure_data)
        with open('mes\\mes_final_report.json', 'r') as file:
            report_data = json.load(file)
        #return render_template('attack_report.html',data=report_data)
        return redirect(url_for('attack_report'))
    if(selected_option=="mqtt"):
        return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)
