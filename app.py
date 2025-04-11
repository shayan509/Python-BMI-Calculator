# Python BMI Calculator

import streamlit as st
import pandas as pd

def main():
    st.title("BMI Calculator")
    st.subheader("Made by Muhammad Shayan Imran")
    st.subheader("Github : 'shayan509'")
    st.write("Enter your weight and height to calculate your BMI.")

    weight = st.slider("Enter your Weight (in kg)" , 0, 200, 50)
    height_ft = st.slider("Enter your Height (in ft)" , 0, 10, 5, )

    height_m = height_ft * 0.3048
    bmi = weight / (height_m**2)
    st.write("Your BMI is:", round(bmi, 2))

    if bmi < 18.5:
        st.write("You are Underweight")
    elif bmi >= 18.5 and bmi < 24.9:
        st.write("You are Normal")
    elif bmi >= 25 and bmi < 29.9:
        st.write("You are Overweight")
    else:
        st.write("You are Obese")

if __name__ == "__main__":
    main()
