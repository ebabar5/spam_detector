from flask import Flask, request, jsonify
from model import *
from sklearn.feature_extraction.text import TfidfVectorizer



app = Flask(__name__)
@app.route('/predict',methods=['POST','OPTIONS'])
def home():
    if request.method == 'OPTIONS':
        return('',204)
    data=request.get_json()
    message=data['message']
    message=vec.transform(data['message'])
    prediction=model.predict(message)
    return jsonify(int(prediction[0]))
    
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    return response
if __name__=='__main__':
    app.run(debug=True,port=5000)