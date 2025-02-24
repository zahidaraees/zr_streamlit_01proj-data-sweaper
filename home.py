# First Project of Data Sweeper App in Streamlit Python by Zahida Raees. Part of Growth Mindset. 
# This is the Home Page of the App.
import streamlit as st

# Page Configurations   
st.set_page_config(
    page_title="Home Page",
    page_icon="🏠",
    layout="centered",    
    initial_sidebar_state="expanded",
)   

st.title("Welcome to Data Sweeper App") # Title of the page
st.subheader("By Zahida Raees") # Subtitle of the page

## Description of the app
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
st.markdown("If you have any questions or feedback, please contact me at [email](mailto:zahidaraeesi@hotmail.com)")          

st.markdown("## Disclaimer")
st.markdown("This app is provided 'as is' without any warranty. Use at your own risk.")         

st.subheader("Thank you ")
st.markdown(".......for visiting my app, Click on the following button or select it from the sidebar menu")  

# Custom CSS for the stylish button
button_style = """
    <style>
    .button {
        display: inline-block;
        padding: 14px 28px;
        font-size: 18px;
        font-weight: bold;
        color: white;
        background: linear-gradient(135deg, #ff7e5f, #feb47b);
        text-align: center;
        text-decoration: none;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s, box-shadow 0.3s;
        margin-top: 20px;
    }
    .button:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
    }
    </style>
"""

# HTML for the button link
button_html = '''
    <a href="/pages/data_sweeper" class="button">Data Sweeper App</a>
'''

# Inject CSS and HTML into Streamlit app
st.markdown(button_style, unsafe_allow_html=True)
st.markdown(button_html, unsafe_allow_html=True)

st.markdown("---")
