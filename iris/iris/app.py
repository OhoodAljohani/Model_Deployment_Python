# Importing 
import numpy as np
from flask import Flask, request, jsonify, render_template
import flask
import pickle
import csv
from sklearn import preprocessing
from joblib import load
import sklearn
# Creat Flask App : 
app = Flask(__name__)
# Loading the model from ./model
model = load(open('..\iris\model\iris-model.joblib','rb'))
# Printing Libraries versions : 
'''print(np.__version__)#1.18.5
print(flask.__version__)#1.1.2
print(csv.__version__) #1.0
print(sklearn.__version__) #0.23.1'''
# Creating the home route for the app homepage : 
@app.route('/')
# The homepage function : 
def home():
    '''
    This function for the homepage rout will return the main.html page . 
    '''
    return render_template('main.html')
# Creating the prdicit route for the app predicting api : 
@app.route('/predict',methods=['POST'])
# The predicting function : 
def predict():
    '''
    This function for the prdicit api  rout will return the prdicted class 
    to the main.html page  . 
    
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    #prediction = model.predict(preprocessing.normalize(final_features))
    prediction = model.predict(final_features)
    print(final_features)
    output = prediction
    if output[0]==0:
        return render_template('main.html', prediction_text="The data entered indicates Iris Setosa Class ")
    if output[0]==1:
        return render_template('main.html', prediction_text="The data entred indicates Iris Versicolour Class ")
    if output[0]==2:
        return render_template('main.html', prediction_text="The data entered indicates  Iris Virginica Class ")

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)
