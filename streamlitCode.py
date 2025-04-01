import streamlit as st
import datetime
import Milestone1

st.title("Food App-Milestone 1")
st.write("MileStone")

d = st.date_input("Meal Option date?", datetime.date(2025, 4, 1))
st.write("You Selected", d)