import streamlit as st


class ChatBot:

    def show():
        messages = st.container(height=450)

        # Function to display the chat history
       
        # Initialize chat history if it doesn't exist
        if "chat_history" not in st.session_state:
                 st.session_state.chat_history = []
        messages.chat_message("assistant",avatar="assets/image/bot.png" ).write(
                    "Hi there, how can i help you?")

        if user_input := st.chat_input("Type here few words to continue..."):
            st.session_state.chat_history.append(
                {"user": "user", "text": user_input})
            # Example: Add a bot's response
            bot_response = f"Bot: I received your message: {user_input}"
            st.session_state.chat_history.append(
                {"user": "assistant", "text": bot_response})
            # Reset input field after sending
            st.session_state.chat_input = ""
        def display_chat():
            for msg in st.session_state.chat_history:
                messages.chat_message(msg['user']).write(msg['text'])
        display_chat()
