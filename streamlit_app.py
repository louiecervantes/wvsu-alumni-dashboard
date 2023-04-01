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
            csvfile = ''
        elif year=='2015':
            csvfile = ''
        elif year=='2016':
            csvfile = ''
        elif year=='2017':
            csvfile = ''
        elif year=='2018':
            csvfile = '2018-main.csv'
        elif year=='2019':
            csvfile = ''
        elif year=='2020':
            csvfile = ''
        elif year=='2021':
            csvfile = ''
        elif year=='2022':
            csvfile = ''
    elif campus == 'Himamaylan':
        #add more csv files here
        csvfile = ''    
    return csvfile

def filterBy(df, college):
    filtered_df = df[df['COLLEGE'] == college]  
    return filtered_df

def loadcsvfile(campus, year):
    csvfile = ''
    csvfile = get_file(campus, year)
    if len(csvfile) > 0:

        df = pd.read_csv(csvfile, dtype='str', header=0, sep = ",", encoding='latin')
        st.dataframe(df, width=800, height=400)
        st.write("Properties of the dataset")
        desc = df.describe().T
        st.write(desc) 
        hasData = True
        
    else:
        hasData = False
        st.write('No data to process!')   
    return hasData
    
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
    
    hasData = false
    
    selected_option = st.selectbox('Select the year', options)
    if selected_option=='2013':
        year = selected_option
        hasData = loadcsvfile(campus, year)
    else:
        year = selected_option
        hasData = loadcsvfile(campus, year)
    
    if st.button('By Gender'):
        if hasData==True:
            #Gender
            st.write("Distribution by gender")
            scounts=df['GENDER'].value_counts()
            labels = list(scounts.index)
            sizes = list(scounts.values)
            custom_colours = ['#ff7675', '#74b9ff']
            fig = plt.figure(figsize=(12, 4))
            plt.subplot(1, 2, 1)
            plt.pie(sizes, labels = labels, textprops={'fontsize': 10}, startangle=140, autopct='%1.0f%%', colors=custom_colours)
            plt.subplot(1, 2, 2)
            sns.barplot(x = scounts.index, y = scounts.values, palette= 'viridis')
            st.pyplot(fig)
        else:
            st.write("No data to process!")
            
    if st.button("By Municipality"):
        if hasData==True:
            #Municipality
            st.write('Distribution by Municipality/City')
            value_counts = df['MUNICIPAL/ CITY'].value_counts(normalize=True)
            value_counts = value_counts.mul(100).round(2).astype(str) + '%'
            value_counts.name = 'Percentage'
            result = pd.concat([df['MUNICIPAL/ CITY'].value_counts(), value_counts], axis=1)
            result.columns = ['Counts', 'Percentage']
            st.write(pd.DataFrame(result))  
        else:
            st.write('No data to process!')
            
    if st.button("By Province"):
        if hasData==True:
            #Province
            st.write('Distribution by Province')
            fig = plt.figure(figsize=(6, 2))
            p = sns.countplot(x="PROVINCE", data = df, palette="muted")
            _ = plt.setp(p.get_xticklabels(), rotation=90)
            st.pyplot(fig)
            
            #tabular data
            st.write('No. of graduates per province')
            # get value counts and percentages of unique values in column 
            value_counts = df['PROVINCE'].value_counts(normalize=True)
            value_counts = value_counts.mul(100).round(2).astype(str) + '%'
            value_counts.name = 'Percentage'
            result = pd.concat([df['PROVINCE'].value_counts(), value_counts], axis=1)
            result.columns = ['Counts', 'Percentage']
            st.write(pd.DataFrame(result))
            
            st.write('Distribution by Province')
            scounts=df['PROVINCE'].value_counts()
            labels = list(scounts.index)
            sizes = list(scounts.values)
            custom_colours = ['#ff7675', '#74b9ff']

            fig = plt.figure(figsize=(6, 10))
            plt.subplot(2, 1, 1)
            plt.pie(sizes, labels = labels, textprops={'fontsize': 10}, startangle=140, 
                   autopct='%1.0f%%', colors=custom_colours)
            plt.subplot(2, 1, 2)
            sns.barplot(x = scounts.index, y = scounts.values, palette= 'viridis') 
            st.pyplot(fig)   
        else:
            st.write("No data to process!")
            
    if st.button("By Degree Program"):
        if hasData==True:    
            st.write('Alumni distributed by degree program')
            st.write(df['DEGREE PROGRAM'].value_counts())
            
            st.write('Filter by college')
            college = 'CAS'
            options = df['COLLEGE'].unique()
            selected_option = st.selectbox('Select the college', options)
            
            filtered_df = ''
            if selected_option=='CAS':
                college = selected_option
                filtered_df = filterBy(df, college)
            else:
                college = selected_option
                filtered_df = filterBy(df, college)
                
            st.write('Graduates distributed per program under the college: ' + college)
            fig = plt.figure(figsize=(6, 2))
            p = sns.countplot(x="DEGREE PROGRAM", data = filtered_df, palette="muted")
            _ = plt.setp(p.get_xticklabels(), rotation=90)
            st.pyplot(fig)      
        else:
            st.write("No data to process!")

# Run the app
if __name__ == "__main__":
    app()
