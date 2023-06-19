import psycopg2
import pandas as pd

uri ='postgres://cuhrcpzz:IXWBI13FTFgQHhMk2sND0EITRZk92mhR@rajje.db.elephantsql.com/cuhrcpzz'
conn = psycopg2.connect(
    host="rajje.db.elephantsql.com",
    database="cuhrcpzz",
    user="cuhrcpzz",
    password="IXWBI13FTFgQHhMk2sND0EITRZk92mhR")

df_d = pd.read_csv('/Users/bumsoojoe/Desktop/Section4_project/csv/diabetes_prediction_dataset.csv')
df_m = pd.read_csv('/Users/bumsoojoe/Desktop/Section4_project/csv/medical.csv')

df_d.to_sql('diabetes_prediction_dataset', conn, if_exists='fail')
df_m.to_sql('medical', conn, if_exists='fail')
cur = conn.cursor()
print(conn)