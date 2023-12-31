#Diabetes
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
import random
import pickle

dliabetes = pd.read_csv('/Users/bumsoojoe/Desktop/Section4_project/csv/diabetes_prediction_dataset.csv')

df = dliabetes.drop_duplicates()
df = df.reset_index(drop=True)
df.rename(columns={'gender':'sex','smoking_history':'smoking'},inplace=True)
df['sex'] = df['sex'].str.lower()
df = df.astype({'age':'int64'})
other = list(df[df['sex'] == 'Other'].index)
nan = list(df[df['smoking'] == 'No Info'].index)
df = df.drop(other)
df = df.drop(nan)
df = df.reset_index(drop=True)

smoking_yes = ['ever','current']
smoking_no = ['never', 'former', 'not current']
df = df.copy()
df = df.replace(smoking_yes,'yes')
df = df.replace(smoking_no,'no')

train, test = train_test_split(df, test_size=0.2, stratify=df['diabetes'],random_state=42)
train, val = train_test_split(train, test_size=0.2, stratify=train['diabetes'],random_state=42)

y_train = train['diabetes']
x_train = train.drop(columns=['diabetes','HbA1c_level','blood_glucose_level','hypertension','heart_disease'],axis=1)

y_val = val['diabetes']
x_val = val.drop(columns=['diabetes','HbA1c_level','blood_glucose_level','hypertension','heart_disease'],axis=1)

y_test = test['diabetes']
x_test = test.drop(columns=['diabetes','HbA1c_level','blood_glucose_level','hypertension','heart_disease'],axis=1)

print('train : ', x_train.shape, y_train.shape)
print('val : ', x_val.shape, y_val.shape)
print('test : ', x_test.shape, y_test.shape)

model = make_pipeline(
            OrdinalEncoder(),
            SimpleImputer(strategy="median"),
            XGBClassifier(
                objective="binary:logistic",
                eval_metric="error",
                n_estimators=200,
                random_state=42,
                n_jobs=-1,
                max_depth=7,
                learning_rate=0.1,
                use_label_encoder=False,
            ),
            )

model.fit(x_train,y_train)
print("검증 정확도", model.score(x_val, y_val))
y_pred = model.predict(x_val)
print(classification_report(y_val, y_pred))
y_test_pred = model.predict(x_test)
print(classification_report(y_test, y_test_pred))

with open('Diabetes_model.pkl','wb') as pickle_file:
    pickle.dump(model, pickle_file)