import streamlit as st

# Page Title
st.title("A Programmer & Literary Author")
st.markdown("---")

# Section 1: My Introduction 
st.header("Who am I... ")
st.write("""
Hi,
I am Zahida Raees, Student of  GIAIC Q3-Section A. 

As a developer, my major expertise are in Desktop Application Development for the financial, trading, manufacturing and service-oriented industries. In the world of web, for Frontend Development, I worked in Next-JS, TypeScript, React, Mouk-ai, Sanity, Streamlit. While for backend and fullstack development, I have selected NEXTJS & Python. As a literary author, I have published five books in different literary genres. I have the honor of being the first female novelist and the third short story writer of Balochi language & literature. I'm an M.Phil scholar and Assistant Teacher at the University of Karachi. Last but not least, I am always on the way to upgrade my knowledge & skills in the fields of my profession and interests.


""")
st.image("https://personal-portfolio-react-nextjs-css.vercel.app/_next/image?url=%2Fassets%2Fzr_pic_latest.jpg&w=750&q=75", caption="Zahida Raees",  use_container_width =True)
st.markdown("---")

# Section 2: My Projects
st.header("My Projects")

# 1st Project
col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://personal-portfolio-react-nextjs-css.vercel.app/_next/image?url=%2Fassets%2Fproject00.png&w=3840&q=75", width=250)
with col2:
    st.subheader("Ecommerce UI/UX")
    st.write("""
    Ecommerce UI/UX, Figma, NextJS-Tailwind CSS
    """)
# second project    
col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://personal-portfolio-react-nextjs-css.vercel.app/_next/image?url=%2Fassets%2Fproject05.png&w=3840&q=75", width=250)
with col2:
    st.subheader("Simple Multipage Website")
    st.write("""
    Simple Multipage Website with Tailwind CSS
    """)

# Third Project
col3, col4 = st.columns([1, 3])
with col3:
    st.image("https://personal-portfolio-react-nextjs-css.vercel.app/_next/image?url=%2Fassets%2Fproject04.png&w=3840&q=75", width=150)
with col4:
    st.subheader("Responsive Website")
    st.write("""
    Responsive Website With Core HTML, CSS.
    """)

# Forth Project
col3, col4 = st.columns([1, 3])
with col3:
    st.image("https://personal-portfolio-react-nextjs-css.vercel.app/_next/image?url=%2Fassets%2Fproject01.png&w=3840&q=75", width=150)
with col4:
    st.subheader("Dynamic Resume Builder, Shareable and Editatble")
    st.write("""
    Dynamic Resume Builder with Unique Path and Shareable Link in HTML, CSS, Typescript.
    """)

# Fifth Project
col3, col4 = st.columns([1, 3])
with col3:
    st.image("https://personal-portfolio-react-nextjs-css.vercel.app/_next/image?url=%2Fassets%2Fproject02.png&w=3840&q=75", width=150)
with col4:
    st.subheader("Dynamic Inventory Management System Milestone 5:")
    st.write("""
    Dynamic Inventory Management System Milestone 5: Implmention of Basic Validation for Product Input in Dynamic Inventory Management System . HTML , CSS, Typescript
    """)

# Sixth Project
col3, col4 = st.columns([1, 3])
with col3:
    st.image("https://personal-portfolio-react-nextjs-css.vercel.app/_next/image?url=%2Fassets%2Fproject03.png&w=3840&q=75", width=150)
with col4:
    st.subheader("Dynamic blog")
    st.write("""
    Dynamic blog . next-js, sanity using default blog template
    """)

st.markdown("---")

# Section 3: Contact Information
st.header("Get in Touch")
st.write("Feel free to reach out to us at:")
st.markdown("""
- **Email:** zahidaraeesi@hotmail.com
- **Phone:** +92-333-1234567 (its fake)
- **Address:** Karachi. Pakistan
""")

# Social Media Links
st.markdown("""
Connect with us on:
- [LinkedIn](https://www.linkedin.com/in/zahida-raees-837602a/)
- [GitHub](https://github.com/zahidaraees)
- [Facebook](https://www.facebook.com/zahida.raeesi)
""")
