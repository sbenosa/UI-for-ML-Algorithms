'''
Author: Sherwin Benosa
Exposing Salary Prediction in API
April 10, 2019
'''
import pickle
from flask import Flask, request
from flasgger import Swagger
from flask.views import View

import numpy as np
import pandas as pd

with open('predict_salary.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
    
app =Flask(__name__)
swagger = Swagger(app)


@app.route('/')
def predict_salary():	
    """Example endpoint returning a prediction of Salary
    ---
    parameters:
      - name: position
        in: query
        type: string
        required: true
      - name: experience
        in: query
        type: number
        required: true
      - name: industry
        in: query
        type: string
        required: true
    """
    position = request.args.get('position')
    experience = request.args.get('experience')
    industry = request.args.get('industry')
    
    prediction = model.predict(np.array([[position, experience, industry]]))
    return str(prediction)

@app.route('/predict_file', methods=["POST"])
def predict_salary_file():
    """Example file endpoint returning a prediction of salary
    ---
    parameters:
      - name: input_file
        in: formData
        type: file
        required: true
    """
    input_data = pd.read_csv(request.files.get('input_file'), header=None)
    prediction = model.predict(input_data)
    return str(list(prediction))

if __name__ == '__main__':
    app.run()

