# Code refactored from https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps
import streamlit as st
from tools.utils import Utils
from components.sidebar import SideBar
from components.chatbot import ChatBot

st.set_page_config(
    page_title="Exec Go - Guided Selling with Enterprise Chatbot",
    page_icon="favicon.ico",
    layout="centered"
)

Utils.load_css()

SideBar.show()
ChatBot.show()

