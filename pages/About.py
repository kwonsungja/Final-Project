import streamlit as st

st.title("About Kwon")
st.header("To be a good English teacher")

# 이미지 추가
st.subheader("Meet our mascot!")

# Corrected Raw Image URL
image_url = "https://raw.githubusercontent.com/kwonsungja/Final-Project/main/images/english%20image.png"

# Display the image
try:
    st.image(image_url, caption="Your friendly mascot!", width=300)
    st.write("This cute character is here to cheer you on as you learn and grow! 🌟")
except Exception as e:
    st.error(f"⚠️ An error occurred while displaying the image: {e}")
