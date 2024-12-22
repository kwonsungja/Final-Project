import streamlit as st
import qrcode
from PIL import Image
import io

# 앱 링크
app_link = "https://kwon24.streamlit.app/"

# QR 코드 생성 함수
def generate_qr_code(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    # 이미지 생성
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Streamlit UI
st.title("Final-Project: APP Learning Plan")
st.markdown("This app helps you learn about forming regular plural nouns in English.")

# QR 코드 생성 및 표시
qr_image = generate_qr_code(app_link)
buffer = io.BytesIO()
qr_image.save(buffer, format="PNG")
buffer.seek(0)

# 앱 링크 및 QR 코드 표시
st.write(f"Access the app using the link below or scan the QR code!")
st.markdown(f"[**Click here to open the app**]({app_link})")
st.image(buffer, caption="Scan this QR code to open the app!", use_column_width=True)
