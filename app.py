from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index_new.html')


standard_to = StandardScaler()

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == "POST":

         Married = request.form.get('Married',False)
         if(Married == 'yes'):
             Married_Yes = 1
         else:
             Married_Yes = 0
         
         Dependents = request.form.get('Dependents',False)
         if(Dependents == '1'):
             Dependents_1 = 1
             Dependents_2 = 0
             Dependents_3 = 0
         elif(Dependents == '2'):
             Dependents_1 = 0
             Dependents_2 = 1
             Dependents_3 = 0
         elif(Dependents == '3'):
             Dependents_1 = 0
             Dependents_2 = 0
             Dependents_3 = 1
         else:
             Dependents_1 = 0
             Dependents_2 = 0
             Dependents_3 = 0
         Education = request.form.get('Education',False)
         
         if(Education == 'Not Graduate'):

             Education_Not_Graduate = 1
         else:
             Education_Not_Graduate = 0

         LoanAmount = float(request.form.get('LoanAmount',False))
         Loan_Amount_Term = float(request.form.get('Loan_Amount_Term',False)) 
         Income = float(request.form.get('Income',False))


         Property_Area = request.form.get('Property_Area',False) 
         if(Property_Area == 'Semiurban'):
             Property_Area_Semiurban = 1
             Property_Area_Urban = 0
         elif(Property_Area == 'Urban'):

              Property_Area_Urban = 1
              Property_Area_Semiurban = 0
         else:
              Property_Area_Urban = 0
              Property_Area_Semiurban = 0
         Credit_History = float(request.form.get('Credit_History',False))
         prediction=model.predict([[Credit_History , Income , LoanAmount , Loan_Amount_Term , Property_Area_Semiurban , Education_Not_Graduate , Property_Area_Urban , Married_Yes , Dependents_1 , Dependents_2 , Dependents_3]])
         
         #output=round(prediction[0],2)

         if prediction == 0:
            return render_template('index_new.html',prediction_texts = 'Not Eligible')
        
         else:
            return render_template('index_new.html',prediction_texts = 'Eligible')
    else:

        return render_template('index_new.html')


if __name__ == '__main__':
    app.run(debug=True)
   

         
