import streamlit as st
import datetime
import Milestone1

st.title("Food App-Milestone 1")

### DATE ###
st.write("Date Selection")
date = st.date_input("Meal Option date?", datetime.date(2025, 4, 1))
st.write("You Selected", date)


### LOCATION ###

# dictionary with a dining hall's specific meal ids
mealIDs = {'Bao': [96, {'Breakfast': 148, 'Lunch': 149, 'Dinner': 312}], 
         'Bates': [95, {'Breakfast': 145, 'Lunch': 146, 'Dinner': 311}],
         'StoneD': [131, {'Breakfast': 261, 'Lunch': 262, 'Dinner': 263}], 
         'Tower': [97, {'Breakfast': 153, 'Lunch': 154, 'Dinner': 310}]
         }

st.write("Location Selection")
chosenLocation = st.selectbox(
    "Please select a dining hall:",
    ("Bates", "Lulu","Stone Davis","Tower")
)
st.write("You Selected", chosenLocation)


### MEAL TYPE ###
st.write("Meal type Selection")
chosenMeal = st.selectbox(
    "Please select a meal time:",
    ("Breakfast", "Lunch","Dinner")
)
st.write("You Selected", chosenMeal)