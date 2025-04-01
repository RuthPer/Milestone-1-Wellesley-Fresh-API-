#Milestone1


# importing necessary libraries
import requests
import json
import csv
import pandas as pd
import datetime
import time
import os



# creating lists of locations and meals
locations = ['Bao', 'Bates', 'StoneD', 'Tower']
meals = ['Breakfast', 'Lunch', 'Dinner']

# dictionary with a dining hall's id
locationIDs = {'Bao': 96, 
             'Bates': 95, 
             'StoneD': 131, 
             'Tower': 97
             }

# dictionary with a dining hall's specific meal ids
mealIDs = {'Bao': {'Breakfast': 148, 'Lunch': 149, 'Dinner': 312}, 
         'Bates': {'Breakfast': 145, 'Lunch': 146, 'Dinner': 311},
         'StoneD': {'Breakfast': 261, 'Lunch': 262, 'Dinner': 263}, 
         'Tower': {'Breakfast': 153, 'Lunch': 154, 'Dinner': 310}
         }


'''

'''
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


def write_menus(csvfile, date):
    with open(csvfile, 'r') as inFile:
        reader = csv.DictReader(inFile)
        for row in reader:
            day = date.strftime("%m-%d-%Y")
            data = get_menu(date, row['locationID'], row['mealID'])
            fname = f"{row['location']}-{row['meal']}-{day}.json"
            with open(fname, 'w') as outFile:
                json.dump(data, outFile)
            time.sleep(2)

day = datetime.datetime(2025, 4, 1)
write_menus('wellesley-dining.csv', day)

filedir = [file for file in os.listdir() if '2025' in file]
filedir

for file in filedir:
    with open(file, 'r') as inFile:
        rows = json.load(inFile)
        print(f"{len(rows)} rows in {file}")

currentdf = pd.DataFrame()

count = 0
for file in filedir:
    newdf = pd.read_json(file)
    newdf['diningHall'] = file.split('-')[0]
    newdf['mealType'] = file.split('-')[1]
    currentdf = pd.concat([currentdf, newdf], ignore_index=True)
    print(f"Appended {file}. Now size is ({len(currentdf)}, {len(currentdf.columns)})")