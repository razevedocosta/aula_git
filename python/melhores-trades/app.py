from flask import Flask, jsonify, request
from joblib import load

app = Flask(__name__)

@app.route("/")
def index():
    if 'query' not in request.args:
        return jsonify({"prediction": None, "message": "send me a text"})
    
    query = request.args.get("query")
    model = load("model.joblib")
    labels = ['c', 'v']

    predict = model.predict([query])
    prediction = labels[predict[0]]

    return jsonify({"prediction": prediction})