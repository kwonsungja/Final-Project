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

# Corrected URL (raw image link from GitHub)
image_url = "https://raw.githubusercontent.com/kwonsungja/Final-Project/main/images/snow.png"

# Load and display the image from the URL
try:
    response = requests.get(image_url)
    response.raise_for_status()  # Ensure the request was successful
    image = Image.open(BytesIO(response.content)).convert("RGB")  # Ensure the image is processed as RGB
    st.image(image, caption="A friendly teacher welcoming you!")
    st.markdown("➰ URL: final project app")
    st.markdown("➰ Since Dec. 22, 2024.")

except requests.exceptions.RequestException as e:
    st.write(f"⚠️ Unable to load the image from the URL! Error: {e}")
except Exception as e:
    st.write(f"⚠️ An error occurred while processing the image. Error: {e}")

