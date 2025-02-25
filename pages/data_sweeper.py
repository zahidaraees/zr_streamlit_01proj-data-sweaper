#imports dependencies.
import streamlit as st
import pandas as pd
import os
from io import BytesIO

#setup of  Application 
st.set_page_config(page_title= "Data Sweeper App by Zahida Raees ", layout="wide")
st.title("Data Sweeper")
st.write("Transformation of your files, between CSV and Excel formats with built-in data cleaning and visualiazation")

uploaded_files = st.file_uploader("Upload your files (CSV or Excel):",type=["csv","xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
      file_ext = os.path.splitext(file.name)[-1].lower()

      if file_ext == ".csv":
        df = pd.read_csv(file)
      elif file_ext ==  ".xlsx":
        df = pd.read_excel(file)
      else:
        st.error(f"Unspported file type: {file_ext}")
        continue

    #Display info about the file
    st.write(f"**File Name:** {file.name}")
    st.write(f"**File Size:** {file.size/1024}")

    #show 5 rows  of our DataFrame
    st.write("Preview the Head of the Dataframe")
    st.dataframe(df.head())

    #Options for data cleaning
    st.subheader("Data Cleaning Options")
    if st.checkbox(f"Clean Data for {file.name}"):
      col1, col2 = st.columns(2)

      with col1:
        if st.button(f"Remove Duplicate from {file.name}"):
          df.drop_duplicates(inplace=True)
          st.write("Duplicates Removed!")

      with col2:
        if st.button(f"Fill missing values from {file.name}"):
          numeric_cols = df.select_dtypes(include=['number']).columns
          df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
          st.write("Missing values have been filled!")

    # Choose Specific Columns to keep or convert
    st.subheader("Choose Specific Columns to convert")
    columns = st.multiselect(f"Choose Columns for {file.name}", df.columns,default=df.columns)
    df = df[columns]

#Create Some visualizations
st.subheader("Data Visualizations")
if st.checkbox("Show Visualization for {file.name}" ):
    st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])

#Coverting the File to CSV to Excel
    st.subheader("Conversion Opotions")
    conveersion_type = st.radio(f"Convert {file.name} to:", ("CSV", "Excel"),key=file.name)
    if st.button(f"Convert {file.name}"):
        buffer =BytesIO()
        if conveersion_type == "CSV":
            df.to_csv(buffer, index=False)
            file_name = file.name.replace(file_ext, ".csv")
            mime_type = "text/csv"

            
        elif conveersion_type == "Excel":
            df.to_excel(buffer, index=False)
            file_name = f"{file.name.replace(file_ext, '.xlsx')}"
            mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        buffer.seek(0)

    # Download the file       
        st.download_button(label="Click here to download", data=buffer,
            file_name=file_name, 
            mime=mime_type
            )

    st.success("All file Operations Completed Successfully!")      