
from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)


with open('crop_recommendation_model.pkl', 'rb') as file:
    model =pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        
        inputs = [
            float(request.form['N']),
            float(request.form['P']),
            float(request.form['K']),
            float(request.form['Temperature']),
            float(request.form['Humidity']),
            float(request.form['PH']),
            float(request.form['Rainfall'])
        ]

      
        prediction = model.predict([inputs])[0]

        return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
