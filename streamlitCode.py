import streamlit as st
import datetime
import Milestone1 as m1
import pandas as pd

st.title("Food App-Milestone 1")

### DATE ###
st.write("Date Selection")
date = st.date_input("Meal Option date?", datetime.date(2025, 4, 1))
st.write("You Selected", date)


### LOCATION ###

locations = {'Lulu': [96, {'Breakfast': 148, 'Lunch': 149, 'Dinner': 312}], 
         'Bates': [95, {'Breakfast': 145, 'Lunch': 146, 'Dinner': 311}],
         'Stone Davis': [131, {'Breakfast': 261, 'Lunch': 262, 'Dinner': 263}], 
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

userInput = st.text_input("What do you wanna eat?")
printOutput = 0
if userInput:

    output = m1.get_menu(date, locations[chosenLocation][0],locations[chosenLocation][1][chosenMeal])
    data = m1.createDf(output)[["name", "description", "categoryName"]].drop_duplicates()
    search = data["name"].str.contains(userInput, case=False, na=False)


    printOutput = st.button("generate menu")

if printOutput:
    # st.dataframe(data[search])
    name, description, category, journal = st.columns(4)

    with name:
        st.markdown('**Dish Name**')
        dish = data[search]['name'].tolist()
        for i in dish:
            st.write(i)

    with description:
        st.markdown('**Description**')
        desc = data[search]['description'].tolist()
        for i in desc:
            st.write(i)

    with category:
        st.markdown('**Category**')
        cats = data[search]['categoryName'].tolist()
        for i in cats:
            st.write(i)

    with journal:
        st.markdown("**:red[Add to journal]**")
        for i in range(len(dish)):
            st.button('Add', key=i)