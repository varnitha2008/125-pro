from flask import Flask,jsonify, request
import cv2
import numpy as np
from classifier import get_prediction
app = Flask(__name__)


@app.route("/predict_data", methods=["POST"]) 
def predict_data():
    image=request.files.get("digit")
    prediction=get_prediction(image)
    return jsonify({"prediction":prediction})


if (__name__ == "__main__"):
      app.run(debug=True)       