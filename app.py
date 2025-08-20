from flask import Flask, request, jsonify,render_template
import joblib

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    data= request.get_json() or {}
    message=(data.get("message")or "").strip()
    if not message:
        return jsonify({"error":"message is required"}),400
    features = vectorizer.transform([message])
    prediction = model.predict(features)[0]
    
    confidence = None
    try:
        probabilities = model.predict_proba(features)[0]
        confidence = float(probabilities.max())
    except Exception:
        confidence = None
    return jsonify({"label":str(prediction), "confidence": confidence})
    
if __name__=='__main__':
    app.run()


