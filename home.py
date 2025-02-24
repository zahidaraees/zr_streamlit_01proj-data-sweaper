# First Project of Data Sweeper App in Streamlit Python by Zahida Raees. Part of Growth Mindset. 
import streamlit as st


st.set_page_config(
    page_title="Home Page",
    page_icon="🏠",
    layout="centered",    
    initial_sidebar_state="expanded",
    
    
    
    )   

st.title("Welcome to Data Sweeper App")
st.subheader("By Zahida Raees")

st.markdown("This app is a simple tool to help you clean your data. It is a part of my learning journey in Data Science. I hope you find it useful. ")

st.markdown("## Features")
st.markdown("- **Data Cleaning**: Remove duplicates, missing values, and outliers.")
st.markdown("- **Data Visualization**: Create visualizations of your data.")    
st.markdown("- **File Conversion**: Convert between CSV and Excel formats.")

st.markdown("## How to use")
st.markdown("1. Upload your data file in CSV or Excel format.")
st.markdown("2. Select the data cleaning options you want to apply.")
st.markdown("3. Select the data visualization options you want to apply.")    
st.markdown("4. Select the file conversion options you want to apply.")        
st.markdown("5. Click the 'Apply' button.")    
st.markdown("6. Download the resulting file.")
st.markdown("## Contact")
st.markdown("If you have any questions or feedback, please contact me at [email](zahidaraeesi@hotmail.com)")          
st.markdown("## Disclaimer")
st.markdown("This app is provided 'as is' without any warranty. Use at your own risk.")         
st.subheader("Thank you ")
st.markdown(".......for visiting my app, Click on following button or options from sidebar menu")                                                                              
st.link_button("Go to Data Sweeper App", "data_sweeper.py")