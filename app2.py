#medical
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
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

def eval_models(y_true, y_pred) :
    mse = mean_squared_error(y_true, y_pred).round(3)
    rmse = np.sqrt(mse).round(3)
    mae = mean_absolute_error(y_true, y_pred).round(3)
    r2 = r2_score(y_true, y_pred)

    return mse, rmse, mae, r2

class medical:
    # 파일 로드
    def __init__(self):
        medical = pd.read_csv()
        return medical
    
    # 파일 전처리
    def EDA(self,medical):
        df = medical.copy()
        df = df.drop_duplicates()
        df = df.reset_index(drop=True)
        df.rename(columns={'smoker':'smoking'},inplace=True)
        df['bmi'] = round(df['bmi'],2)
        return df

    # diabetes 모델에 데이터 업로드
    def diabetes_load(self,df):
        model_d = None
        md = df[['sex','age','smoking','bmi']]
        with open('Diabetes_model.pkl','rb') as pickle_file:
            model_d =pickle.load(pickle_file)
        df['diabetes'] = model_d.predict(md)
        return df

    def train_test(self,df):
        train, test = train_test_split(df, test_size=0.2,random_state=42)
        train, val = train_test_split(train, test_size=0.2,random_state=42)

        y_train = train['charges']
        x_train = train.drop(columns=['charges'],axis=1)

        y_val = val['charges']
        x_val = val.drop(columns=['charges'],axis=1)

        y_test = test['charges']
        x_test = test.drop(columns=['charges'],axis=1)

        print('train : ', x_train.shape, y_train.shape)
        print('val : ', x_val.shape, y_val.shape)
        print('test : ', x_test.shape, y_test.shape)
        return x_train, y_train, x_val, y_val, x_test, y_test
    
    
    # 머신러닝 모델
    def model(self, x_train, y_train, x_val, y_val, x_test, y_test):
        model = make_pipeline(
        OrdinalEncoder(),
        XGBRegressor(),
        )
        model.fit(x_train,y_train)
        y_train_pred = model.predict(x_train)
        y_val_pred = model.predict(x_val)
        y_test_pred = model.predict(x_test)

        comparison = pd.DataFrame(index=['mse', 'rmse', 'mae', 'r2'], columns=['Train', 'Validation','test'])
        comparison['Train'] = eval_models(y_train, y_train_pred)
        comparison['Validation'] = eval_models(y_val, y_val_pred)
        comparison['test'] = eval_models(y_test, y_test_pred)
        print(comparison)

        return model

    # 머신러닝 모델 내보네기
    def output_model(self,model):
        with open('medical_model.pkl','wb') as pickle_file:
            return pickle.dump(model, pickle_file)

