
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page Configurations
st.set_page_config(page_title="My Cool Streamlit Website", page_icon="🌍", layout="wide")

# Custom CSS Styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
    }
    .css-1d391kg {
        color: white;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title & Sidebar
st.title("🚀 Welcome to My Streamlit Website")
st.sidebar.header("Navigation")
st.sidebar.markdown("Choose a section from the sidebar.")

# Buttons and Interactions
if st.button("Click Me!"):
    st.success("You clicked the button!")

# Display Image
st.image("https://source.unsplash.com/600x300/?nature", caption="Nature is beautiful!")

# Random Data for Charts
data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])

# Line Chart
st.subheader("📊 Random Line Chart")
st.line_chart(data)

# Bar Chart
st.subheader("📊 Random Bar Chart")
st.bar_chart(data)

# User Input Example
st.subheader("🔢 Enter Your Name")
user_name = st.text_input("What's your name?", "")
if user_name:
    st.write(f"Hello, {user_name}! 👋 Welcome to the Streamlit Web App.")

# Footer
st.markdown("---")
st.markdown("💡 **Created using Python & Streamlit** | 🌟 Follow for more projects!")
