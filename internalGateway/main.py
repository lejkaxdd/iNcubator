from flask import Flask, render_template, has_request_context, request, make_response, jsonify
import requests, ast 

app = Flask(__name__)
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def index():
    req = requests.get("http://subscriptionService:8083/api/v1/subscriptions")    
    if req:
        print(req.content)
        print(req.text)
        subscriptions = ast.literal_eval(req.text) 
        return render_template('index.html', len = len(subscriptions), elements = subscriptions)
    else:
        return render_template("shimmer.html")
    # return render_template("index.html", eleme)
    
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)