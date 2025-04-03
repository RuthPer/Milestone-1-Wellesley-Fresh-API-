import streamlit as st
import datetime
import Milestone1 as m1
import pandas as pd

st.title("Food App-Milestone 1")

### DATE ###
dateCon = st.container(border=True)
dateCon.write("Date Selection")
date = dateCon.date_input("Meal Option date?", datetime.date(2025, 4, 1))
st.write("You Selected", date)


### LOCATION ###

locations = {'Lulu': [96, {'Breakfast': 148, 'Lunch': 149, 'Dinner': 312}], 
         'Bates': [95, {'Breakfast': 145, 'Lunch': 146, 'Dinner': 311}],
         'Stone Davis': [131, {'Breakfast': 261, 'Lunch': 262, 'Dinner': 263}], 
         'Tower': [97, {'Breakfast': 153, 'Lunch': 154, 'Dinner': 310}]
         }
locCon = st.container(border=True)
locCon.write("Location Selection")
chosenLocation = locCon.selectbox(
    "Please select a dining hall:",
    ("Bates", "Lulu","Stone Davis","Tower")
)
st.write("You Selected", chosenLocation)


### MEAL TYPE ###
mealCon = st.container(border=True)
mealCon.write("Meal Time Selection")
chosenMeal = mealCon.selectbox(
    "Please select a meal time:",
    ("Breakfast", "Lunch","Dinner")
)
st.write("You Selected", chosenMeal)

searchCon = st.container(border=True)
userInput = searchCon.text_input("What do you wanna eat?")
printOutput = 0
if userInput:

    output = m1.get_menu(date, locations[chosenLocation][0],locations[chosenLocation][1][chosenMeal])

    data = m1.createDf(output)[["name","description"]].drop_duplicates()
    search = data["name"].str.contains(userInput, case=False, na=False)

    printOutput = st.button("Generate menu")

if printOutput:
    if data[search].empty:
        searchCon.write("Not a Meal Option!")
    else:
        st.markdown(
            """
                div[data-testid="stFullScreenFrame"] {
                    border: 1px solid red;
                }
            """,
            unsafe_allow_html=True
        )
        searchCon.dataframe(data[search], hide_index=True)