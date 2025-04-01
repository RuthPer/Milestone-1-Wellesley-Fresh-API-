import streamlit as st
import datetime
import Milestone1

st.title("Food App-Milestone 1")
st.write("Date Selection")

date = st.date_input("Meal Option date?", datetime.date(2025, 4, 1))
st.write("You Selected", date)

st.write("Location Selection")
chosenLocation = st.selectbox(
    "Please select a dining hall:",
    ("Bates", "Lulu","Stone Davis","Tower")
)
st.write("You Selected", chosenLocation)

st.write("Meal type Selection")
chosenMeal = st.selectbox(
    "Please select a meal time:",
    ("Breakfast", "Lunch","Dinner")
)
st.write("You Selected", chosenMeal)