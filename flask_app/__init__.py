import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from category_encoders import OrdinalEncoder
from sklearn.model_selection import train_test_split
from category_encoders import OrdinalEncoder
from sklearn.impute import SimpleImputer
from xgboost import XGBClassifier
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import classification_report
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import r2_score
import random
import pickle
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    home = render_template('index.html')
    return home, 200

@app.route('/main',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        sex = request.form['sex']
        age = int(request.form['age'])
        somking = request.form['somking']
        children = int(request.form['children'])
        stature = int(request.form['stature'])
        weight = int(request.form['weight'])
        bmi = round(weight/(stature*0.01),2)
        if bmi >= 35: #20미만(저체중),20-24(정상),25-29(과체중),30이상(비만)
            bmi_result = '고도비만'
        elif bmi >= 30:
            bmi_result = '비만'
        elif bmi >= 25:
            bmi_result = '과체중'
        elif bmi >= 20:
            bmi_result = '정상'
        else:
            bmi_result = '저체중'
        data = {'sex':sex,'age':age,'smoking':somking,'children':children, 'bmi':bmi}
        df = pd.DataFrame(data=data,index=[0])
        diat = df[['sex','age','smoking','bmi']]
        with open('Diabetes_model.pkl','rb') as pickle_file:
            model_d =pickle.load(pickle_file)
        df['diabetes'] = model_d.predict(diat)
        if df['diabetes'][0] == 1:
            diat_result = '당신은 당뇨 가능성이 있습니다.'
        else:
            diat_result = '당신은 정상입니다.'
        df = df[['age', 'sex', 'bmi', 'children', 'smoking', 'diabetes']]
        with open('medical_model.pkl','rb') as pickle_file:
            model_m =pickle.load(pickle_file)
        date_pred = model_m.predict(df)[0]
        result = '{:0,.2f}'.format(date_pred)
        result_12 = '{:0,.2f}'.format((date_pred/12))
        
    main = render_template('main.html',bmi=bmi,bmi_result=bmi_result,diat_result=diat_result,result=result,result_12=result_12)
    return main, 200

if __name__ == "__main__":
    app.run(debug = True)
