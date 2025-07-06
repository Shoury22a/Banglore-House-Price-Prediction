# app.py — Streamlit version for Bengaluru House Price Prediction
import streamlit as st
import pandas as pd
import pickle


model = pickle.load(open("Ridgemodel.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))
df = pd.read_csv("Cleaned_data.csv")

st.set_page_config(page_title="Bangalore House Price Predictor", layout="centered")
st.title(" Bangalore House Price Predictor")

locations = sorted(df["location"].unique())
location = st.selectbox(" Select Location", locations)
sqft = st.number_input(" Total Square Feet", min_value=300, max_value=10000, step=10, value=1000)
bath = st.slider(" Number of Bathrooms", 1, 10, step=1)
bhk = st.slider(" Number of Bedrooms (BHK)", 1, 10, step=1)

if st.button(" Predict Price"):
    try:
        input_df = pd.DataFrame([[sqft, bath, bhk, location]], columns=columns)
        prediction = model.predict(input_df)[0]
        st.success(f" Estimated Price: ₹ {round(prediction, 2)} Lakhs")
    except Exception as e:
        st.error(f" Error during prediction: {e}")
