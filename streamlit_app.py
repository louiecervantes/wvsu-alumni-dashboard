#Input the relevant libraries
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from scipy.stats import chi2_contingency
from PIL import Image

# Define the Streamlit app
def app():
    
    # Load image from file
    img = Image.open("wvsu_logo.png")
    new_size = (200, 200)
    img = img.resize(new_size)
    st.image(img, use_column_width=True, output_format='auto', align='center')

    st.title("Welcome to the WVSU Alumni Dashboard", align='center')
    st.subheader("(c) 2023 WVSU Management Information System")
                 
    st.write("This tool is managed by:")
    st.write("Dr. Jonathan P. Glorial")
    st.write("Director")
    st.write("WVSU Alumni Office")
    st.write("alumni@wvsu.edu.ph")
                 
    st.write("A university alumni dashboard is a visual representation of data that provides insights into the institution's alumni network. It typically includes key performance indicators such as demographics, employment status, industry and job titles, alumni engagement, student success, alumni feedback, social media engagement, giving history, and contact information. The dashboard is designed to provide a quick and easy way for university administrators to monitor and analyze data related to their alumni network, identify trends, and make data-driven decisions to improve alumni relations and engagement.")

    st.subheader("Demographics")
    df = pd.read_csv('2013-main.csv', dtype='str', header=0, sep = ",", encoding='latin')
    st.dataframe(df, width=800, height=400)
    st.write("Properties of the dataset")
    desc = df.describe().T
    st.write(desc)

    if st.button('Begin'):
        st.write("Put some code here")

# Run the app
if __name__ == "__main__":
    app()
