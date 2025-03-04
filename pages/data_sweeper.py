import streamlit as st
import pandas as pd
import os
from io import BytesIO, StringIO

# App Configuration
st.set_page_config(page_title="Data Sweeper & Converter by Zahida Raees", layout="wide")
st.title("🧹 Data Sweeper & Converter")
st.write("Upload your file, clean it, and convert between CSV and Excel formats!")

# File Uploader
uploaded_files = st.file_uploader("Upload CSV or Excel Files:", type=["csv", "xlsx"], accept_multiple_files=True)

if "cleaned_data" not in st.session_state:
    st.session_state.cleaned_data = {}

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Load Data
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file format: {file_ext}")
            continue

        # Store in session state to persist changes
        if file.name not in st.session_state.cleaned_data:
            st.session_state.cleaned_data[file.name] = df.copy()

        cleaned_df = st.session_state.cleaned_data[file.name]

        # Display File Info
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.size / 1024:.2f} KB")
        st.dataframe(cleaned_df.head())

        # Data Cleaning Options
        st.subheader("🧹 Data Cleaning Options")
        col1, col2 = st.columns(2)

        # Remove Duplicates
        if col1.button(f"Remove Duplicates in {file.name}"):
            cleaned_df.drop_duplicates(inplace=True)
            st.session_state.cleaned_data[file.name] = cleaned_df
            st.success("✅ Duplicates Removed!")

        # Fill Missing Values in Numeric Columns
        if col2.button(f"Fill Missing Numeric Values in {file.name}"):
            numeric_cols = cleaned_df.select_dtypes(include='number').columns
            cleaned_df[numeric_cols] = cleaned_df[numeric_cols].fillna(cleaned_df[numeric_cols].mean())
            st.session_state.cleaned_data[file.name] = cleaned_df
            st.success("✅ Missing Numeric Values Filled!")

        # Column Selection
        st.subheader("🎯 Select Columns to Keep (Optional)")
        selected_columns = st.multiselect(f"Select Columns for {file.name}", cleaned_df.columns, default=cleaned_df.columns)
        cleaned_df = cleaned_df[selected_columns]
        st.session_state.cleaned_data[file.name] = cleaned_df

        # Data Visualization (Fixed)
        st.subheader("📊 Data Visualization")
        if st.checkbox(f"Show Bar Chart for {file.name}"):
            numeric_cols = cleaned_df.select_dtypes(include='number').columns  # Get only numeric column names
            if len(numeric_cols) > 0:
                st.bar_chart(cleaned_df[numeric_cols].head())  # Display only first few rows
            else:
                st.warning("⚠️ No numeric columns available for visualization.")

        # File Format Conversion
        st.subheader("⬇️ Download Cleaned File")
        file_format = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

        # Generate and Download File
        def generate_download_link(df, format, original_filename):
            filename_base = os.path.splitext(original_filename)[0]  # Remove original extension
            if format == "CSV":
                buffer = StringIO()
                df.to_csv(buffer, index=False)
                buffer.seek(0)
                st.download_button(
                    label=f"📥 Download {filename_base}.csv",
                    data=buffer.getvalue(),
                    file_name=f"{filename_base}.csv",
                    mime="text/csv"
                )
            else:
                buffer = BytesIO()
                df.to_excel(buffer, index=False, engine='openpyxl')
                buffer.seek(0)
                st.download_button(
                    label=f"📥 Download {filename_base}.xlsx",
                    data=buffer,
                    file_name=f"{filename_base}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

        # Corrected Download Button
        if st.button(f"Download Final {file.name} as {file_format}"):
            generate_download_link(cleaned_df, file_format, file.name)
            st.success(f"✅ {file.name} has been cleaned & converted to {file_format}!")

        st.write("---")
