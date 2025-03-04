#imports dependencies.
import streamlit as st
import pandas as pd
import os
from io import BytesIO, StringIO

#setup of Application 
st.set_page_config(page_title="Data Sweeper & Convertor - by Zahida Raees", layout="wide")
st.title("Data Sweeper & Convertor")
st.write("Transformation of your files, between CSV and Excel formats with built-in data cleaning and visualization")

uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

df = None  # Initialize df outside the loop

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue

        # Display info about the file
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.size/1024} KB")

        # Show 5 rows of our DataFrame
        st.write("Preview the Head of the Dataframe")
        st.dataframe(df.head())

        # Options for data cleaning
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
        columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
        df = df[columns]

        # Create Some visualizations
        st.subheader("Data Visualizations")
        if st.checkbox(f"Show Visualization for {file.name}"):
            numeric_df = df.select_dtypes(include='number')
            if not numeric_df.empty:
                st.bar_chart(numeric_df.iloc[:, :2])
            else:
                st.warning("No numeric columns available for visualization.")

        # Converting the File to CSV or Excel
        st.subheader("Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ("CSV", "Excel"), key=file.name)
        if st.button(f"Convert {file.name}"):
            if conversion_type == "CSV":
                # Use StringIO for CSV conversion
                buffer = StringIO()
                df.to_csv(buffer, index=False)
                buffer.seek(0)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
                data = buffer.getvalue().encode('utf-8')  # Encode as bytes for download
            elif conversion_type == "Excel":
                # Use BytesIO for Excel conversion
                buffer = BytesIO()
                df.to_excel(buffer, index=False, engine='openpyxl')
                buffer.seek(0)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                data = buffer

            # Download the file       
            st.download_button(
                label="Click here to download",
                data=data,
                file_name=file_name,
                mime=mime_type
            )

        st.success("All file Operations Completed Successfully!")
