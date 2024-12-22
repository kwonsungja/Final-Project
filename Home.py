import streamlit as st 
from PIL import Image
import requests
from io import BytesIO

# Title
st.write("# Welcome to my classroom")

st.markdown("""
**"Success is not final, failure is not fatal:  
It is the courage to continue that counts."**  
&nbsp;  
:fire: *Keep pushing forward!* :muscle:  
:rocket: *The sky is not the limit!* :stars:
""")

# Correct URL of the image
image_url = "https://raw.githubusercontent.com/kwonsungja/KSJ24/main/images/snow.png"

# Load and display the image from the URL
try:
    response = requests.get(image_url)
    response.raise_for_status()  # Ensure the request was successful
    image = Image.open(BytesIO(response.content))
    st.image(image, caption="A friendly teacher welcoming you!")
except requests.exceptions.RequestException as e:
    st.write(f"⚠️ Unable to load the image from the URL! Error: {e}")
except Exception as e:
    st.write(f"⚠️ An error occurred while processing the image. Error: {e}")
