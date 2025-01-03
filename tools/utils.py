import io
from PIL import Image
import base64
import streamlit as st


class Utils:
    def get_ImageBase64(imageUrl):
        file = open(imageUrl, "rb")
        contents = file.read()
        img_str = base64.b64encode(contents).decode("utf-8")
        buffer = io.BytesIO()
        file.close()
        img_data = base64.b64decode(img_str)
        img = Image.open(io.BytesIO(img_data))
        resized_img = img.resize((150, 60))  # x, y
        resized_img.save(buffer, format="PNG")
        img_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        return "data:image/png;base64, "+img_b64

    def load_css():
        with open("./assets/css/main_style.css") as f:
            css = f.read()
            st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
