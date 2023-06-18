from pymongo import MongoClient
import pandas as pd

myclient = MongoClient("mongodb+srv://project4:project4@cluster0.vk1xckz.mongodb.net/?retryWrites=true&w=majority")

db = myclient.get_database('project4')

cl = db.get_collection('diabetes_prediction_dataset')
csv_d = '/Users/bumsoojoe/Desktop/Section4_project/csv/diabetes_prediction_dataset.csv'
file = pd.read_csv(csv_d, encoding="utf-8")
cl.insert_many(file.to_dict('records'))

cl = db.get_collection('medical')
csv_m = '/Users/bumsoojoe/Desktop/Section4_project/csv/medical.csv'
file = pd.read_csv(csv_m, encoding="utf-8")
cl.insert_many(file.to_dict('records'))