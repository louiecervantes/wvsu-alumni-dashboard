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

# helper function to get the CSV file
def get_file(campus='Main', year='2013'):
    csvfile = ''
    if campus == 'Main':
        if year=='2013':
            csvfile = '2013-main.csv'
        elif year=='2014':
            csvfle = ''
        elif year=='2015':
            csvfle = ''
        elif year=='2016':
            csvfle = ''
        elif year=='2017':
            csvfle = ''
        elif year=='2018':
            csvfle = '2018-main.csv'
        elif year=='2019':
            csvfle = ''
        elif year=='2020':
            csvfle = ''
        elif year=='2021':
            csvfle = ''
        elif year=='2022':
            csvfle = ''
    elif campus == 'Himamaylan':
        #add more csv files here
        csvfile = ''    
    return csvfile

def load_csvfile():
    csvfile = ''
    csvfile = get_file(campus, year)
    if len(csvfile) > 0:     
        df = pd.read_csv(csvfile, dtype='str', header=0, sep = ",", encoding='latin')
        st.dataframe(df, width=800, height=400)
        st.write("Properties of the dataset")
        desc = df.describe().T
        st.write(desc)
        if st.button('Begin'):
            st.write("Put some code here")
    else:
        st.write('No data to process!')   
    return
    
# Define the Streamlit app
def app():
    
    # Load image from file
    img = Image.open("wvsu_logo.png")
    new_size = (200, 200)
    img = img.resize(new_size)
 
    # Create a container element and center it vertically
    container = st.container()
    container.horizontal_alignment = "center"

    # Display the image inside the container element and align it to the center
    with container:
        st.image(img)
        st.title("Welcome to the WVSU Alumni Dashboard")
        
    st.subheader("(c) 2023 WVSU Management Information System")
                 
    st.write("This dashboard is managed by: \nDr. Jonathan P. Glorial \nDirector, WVSU Alumni Office \nalumni@wvsu.edu.ph")
                 
    st.write("A university alumni dashboard is a visual representation of data that provides insights into the institution's alumni network. It typically includes key performance indicators such as demographics, employment status, industry and job titles, alumni engagement, student success, alumni feedback, social media engagement, giving history, and contact information. The dashboard is designed to provide a quick and easy way for university administrators to monitor and analyze data related to their alumni network, identify trends, and make data-driven decisions to improve alumni relations and engagement.")

    st.subheader("Demographics")
    campus = 'Main'
    options = ['Main', 'Calinog', 'Himamaylan', 'Janiuay', 'Lambunao', 'Pototan','All']
    selected_option = st.selectbox('Select the campus', options)
    if selected_option=='Main':
        campus = selected_option
    else:
        campus = selected_option

    year = '2013'
    options = ['2013', '2014', '2015', '2016', '2017', '2018','2019', '2020', '2021', '2022']
    
    selected_option = st.selectbox('Select the year', options)
    if selected_option=='2013':
        year = selected_option
        load_csvfile
    else:
        year = selected_option
        load_csvfile

# Run the app
if __name__ == "__main__":
    app()
