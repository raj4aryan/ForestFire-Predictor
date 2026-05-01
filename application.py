from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

ridge_model = pickle.load(open('Models/forestFireRidge.pkl', 'rb'))
scaler = pickle.load(open('Models/preprocessFF.pkl', 'rb'))

application = Flask(__name__)
app = application

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predictor", methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws= float(request.form.get('Ws'))
        Rain= float(request.form.get('Rain'))
        FFMC= float(request.form.get('FFMC'))
        DMC= float(request.form.get('DMC'))
        ISI= float(request.form.get('ISI'))
        Classes= float(request.form.get('Classes'))
        Region= float(request.form.get('Region'))
        data = scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        result = ridge_model.predict(data)
        return render_template('predictor.html', result = result[0])
    else:
        return render_template('predictor.html')

if __name__ == '__main__':
    app.run(debug=True)
