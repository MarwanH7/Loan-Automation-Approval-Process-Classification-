from flask import render_template, request, jsonify,Flask
import flask
import numpy as np
import traceback #allows you to send error to user
import pickle
import pandas as pd


# App definition
app = Flask(__name__)

# importing models
with open('regressor.pkl', 'rb') as f:
   regressor = pickle.load (f)

with open('model_columns.pkl', 'rb') as f:
   model_columns = pickle.load (f)

#webpage

@app.route('/')
def welcome():
   return "Welcome!, actual webpage still in creation, Use this Flask App to know your loan acceptance status, in the url add /predict to start"

@app.route('/predict', methods=['POST','GET'])
def predict():

   if flask.request.method == 'GET':
       return "Prediction page.For Post requests use post man and send your Loan data, in json format get specific         prediction. The required column names are Gender, Married, Education, Self_Employed ApplicantIncome,      CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,Property_Area "

   if flask.request.method == 'POST':
       try:
           json_ = request.json # '_' since 'json' is a special word
           print(json_)
           query_ = pd.get_dummies(pd.DataFrame(json_))
           query = query_.reindex(columns = model_columns, fill_value= 0)
           prediction = list(regressor.predict(query))

           return jsonify({
               "prediction":str(prediction)
           })

       except:
           return jsonify({
               "trace": traceback.format_exc()
               })


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5555)


