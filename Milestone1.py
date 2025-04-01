#Milestone1

import requests
import json
import csv
import pandas as pd

locations = ['Bao', 'Bates', 'StoneD', 'Tower']
meals = ['Breakfast', 'Lunch', 'Dinner']
locationIDs = {'Bao': 96, 
             'Bates': 95, 
             'StoneD': 131, 
             'Tower': 97
             }
mealIDs = {'Bao': {'Breakfast': 148, 'Lunch': 149, 'Dinner': 312}, 
         'Bates': {'Breakfast': 145, 'Lunch': 146, 'Dinner': 311},
         'StoneD': {'Breakfast': 261, 'Lunch': 262, 'Dinner': 263}, 
         'Tower': {'Breakfast': 153, 'Lunch': 154, 'Dinner': 310}
         }

with open ('wellesley-dining.csv', 'w',newline='') as file:
    fieldnames = ['location','meal','locationID','mealID']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for l in locations:
        for m in meals:
            dct = {'location':l, 'meal':m, 'locationID':locationIDs[l], 'mealID':mealIDs[l][m]}
            print(dct)
            writer.writerow(dct)
            
def get_menu(date, locID, mealID):
    baseURL = "https://dish.avifoodsystems.com/api/menu-items/week"
    params = {'date': date,
              'locationID': locID,
              'mealID': mealID}

    response = requests.get(baseURL, params=params)
    data = response.json()
    return data

get_menu("4/1/2025", 96, 148)

df=pd.read_csv('wellesley-dining.csv')

print(df.head(3))
