from flask import Flask, request, make_response, jsonify, redirect
import yaml, os, ast
from model import *

# Flask App
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    return "Hello World"

@app.route('/api/v1/consumer/subscriptions', methods=['POST'])
def getCmsData():
    try:
        create_table_subscr()
        json_data = ast.literal_eval(request.json)
        insert_subscription(json_data['subscriptionName'],
                            json_data['subscriptionType'], 
                            json_data['validityPeriod'],
                            json_data['subscriptionDescription'],
                            json_data['deeplinkPayment'],
                            json_data['subscriptionCost'])
        
        return "Succesfully received data from CMS"        
    except IOError as e:
        print(e)
    
    
@app.route('/api/v1/subscriptions', methods=['GET'])
def getAllSubscr():
    try:
        data = get_subscription()
        print(data)
     
        return data
    except:
        print("error")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083)