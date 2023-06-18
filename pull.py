import sqlite3
import pandas as pd

conn = sqlite3.connect('project4.db')
df_d = pd.read_csv('/Users/bumsoojoe/Desktop/Section4_project/csv/diabetes_prediction_dataset.csv')
df_m = pd.read_csv('/Users/bumsoojoe/Desktop/Section4_project/csv/medical.csv')

df_d.to_sql('diabetes_prediction_dataset', conn, if_exists='fail')
df_m.to_sql('medical', conn, if_exists='fail')
cur = conn.cursor()
query = 'SELECT * FROM diabetes_prediction_dataset'
result = cur.execute(query).fetchall()
print(result)