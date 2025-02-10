from flask import Flask, render_template, has_request_context, request, make_response, jsonify
import yaml, base64, os, json 
from kafka import *


app = Flask(__name__)
config_dir = os.path.dirname(os.path.abspath(__file__))
with open(config_dir + '/config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)
    
app.config.update(config)

# Flask application

@app.route('/api/v1/cloudGateway', methods=['GET','POST'])
def receiveSubscription():
    """
    Handle HTTP requests for the cloud gateway endpoint.
    
    Returns:
        str: "POST" if the request method is POST, otherwise "GET".
    """
    if request.method == 'POST':
        # Handle POST request
        if request.headers.get('X-Api-Key') == base64.b64encode((app.config['cmsAuth']['clientId'] +":"+ app.config['cmsAuth']['clientSecret']).encode()).decode():
            
            json_data = request.json
            
            if sendMessageToTopic(app.config['kafka_service']['KAFKA_TOPIC_NAME'], json.dumps(json_data)):
            
                data = {
                    "status" : "200",
                    "message" : "Success"
                }
                return jsonify(data)
        
            else: 
                
                data = {
                "status" : "1000",
                "message" : "Failed to send kafka message"
            }
            
            return jsonify(data)
            
        elif not request.headers.get('X-Api-Key'):
            data = {
                "status" : "403",
                "message" : "Unauthorized" 
            }
            return jsonify(data)
    else:
        # Handle GET request
        return "Сouldn't process your request. Please try again."
    
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)