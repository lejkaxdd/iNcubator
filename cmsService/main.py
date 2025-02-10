from flask import Flask, render_template, request, make_response, jsonify, redirect
import yaml, base64, uuid, time, os
from security import *
from datetime import datetime, timedelta , timezone
import requests as req

app = Flask(__name__, template_folder='templates')
config_dir = os.path.dirname(os.path.abspath(__file__))
with open(config_dir + '/config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)
    
app.config.update(config)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == app.config['cmscreds']['username'] and base64.b64encode(password.encode()).decode() == app.config['cmscreds']['password']:
            gen_uuid =  str(uuid.uuid4())
            tz = timezone(timedelta(hours=6))
            expires_time = datetime.now(tz) + timedelta(minutes=30)
            resp = make_response(redirect('/editor'))
            resp.set_cookie('token', gen_uuid, secure=False, httponly=False, expires=time.mktime(expires_time.timetuple()))
            return resp
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')


@app.route('/editor', methods=['GET']) # Add check cookie time
def editor_page():

    if request.cookies.get('token'):
        return render_template('editor.html')
    else:
        return redirect("/")
    

@app.route('/api/v1/editor/create', methods=['POST'])
def editor(): 

    if request.content_type == 'application/json':
        
        json_data = request.json
        response = req.post("http://cloud-gateway:9000/api/v1/cloudGateway", json=json_data, headers={'X-Api-Key': app.config['cmscreds']['apiKey'] })
        if response.status_code == 200:
            return render_template('editor.html')
        else:
            data = {
                "status" : "400",
                "message" : "Bad request"
            }
            return jsonify(data)
    else:
        data = {
            "status": "400",
            "message" : "unsupported content-type"
        }
        return jsonify(data)
        
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)