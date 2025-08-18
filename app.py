from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return """
    <html>
      <body>
        <h2>Spam Detector</h2>
        <input type="text" id="msg" placeholder="Enter message">
        <button onclick="predict()">Check</button>
        <p id="result"></p>
        <script>
          async function predict() {
            const message = document.getElementById('msg').value;
            const res = await fetch('/predict', {
              method: 'POST',
              headers: {'Content-Type': 'application/json'},
              body: JSON.stringify({message})
            });
            const data = await res.json();
            document.getElementById('result').innerText = JSON.stringify(data);
          }
        </script>
      </body>
    </html>
    """
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


