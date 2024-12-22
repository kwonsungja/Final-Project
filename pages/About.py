import streamlit as st

st.title("About Kwon")
st.header("To be a good English teacher")

# 이미지 추가
st.subheader("Meet our mascot!")
# Raw 이미지 링크 사용
image_url = "https://github.com/kwonsungja/Final-Project/blob/main/images/english%20image.png"
st.image(image_url, caption="Your friendly mascot!", width=300)

st.write("This cute character is here to cheer you on as you learn and grow! 🌟")
