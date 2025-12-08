# streamlit run widgets.py  -> Command to run the app from terminal

import streamlit as st  # Import Streamlit for building UI
import pandas as pd     # Import pandas for data handling

st.title("Streamlit Text Input")  # Display app title

name = st.text_input("Enter your name: ")  # Text input for name

if name:  # Check if name is entered
    st.write(f"Hello, {name}")  # Display greeting

age = st.slider("Select your age: ", 0, 100, 25)  # Slider for age selection
st.write(f"Your age is {age}.")  # Display selected age

options = ["Python", "Java", "C++", "Javascript"]  # Language options list
choice = st.selectbox("Choose your favorite language:", options)  # Dropdown menu
st.write(f"You selected {choice}.")  # Display selected option

data = {  # Sample data dictionary
    "Name": ["John", "Lily", "Merry", "Jack"],
    "Age": [28, 23, 25, 27],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)  # Convert dictionary to DataFrame
st.write(df)  # Display DataFrame

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")  # Upload CSV file

if uploaded_file is not None:  # Check if file is uploaded
    df = pd.read_csv(uploaded_file)  # Read CSV into DataFrame
    st.write(df)  # Display uploaded data
