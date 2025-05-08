import streamlit as st
import pandas as pd

st.title("BMI Calculator")
height=st.slider("Select your height (in cms) ",100,250,175)
weight=st.slider("Select your weight (in kgs)" , 40,200,70)
bmi=weight/((height/100)**2)
st.write(f"your BMI is : {bmi}")
st.write("----BMI Categories----")
st.write("-underweight : BMI less than 18.9")
st.write("-normal weight : BMI between 18.5 and 24.9")
st.write("-overweight : BMI between 25 and 29.9")
st.write("-obesity : BMI 30 or greater")