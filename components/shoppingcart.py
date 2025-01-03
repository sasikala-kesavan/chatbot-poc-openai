import streamlit as st
from tools.utils import Utils
from components.cartitem import CartItem

class ShoppingCart:
    def show():
       st.sidebar.header(":shopping_trolley: Shopping Cart")
       img_b64 = Utils.get_ImageBase64(imageUrl="./assets/image/ericsson.png")
       st.markdown("<div class='title-container'><img src='"+img_b64+"'><h3>Exec Go - Guided Selling with Enterprise Chatbot</h3></div>",
                   unsafe_allow_html=True)
       
       CartItem.show()