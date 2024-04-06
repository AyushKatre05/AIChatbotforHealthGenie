import streamlit as st
from bot2 import chat

def main():
    st.title("Chatbot")

    user_input = st.text_input("Enter your message here:")

    if st.button("Send"):
        if user_input:
            bot_response = chat(user_input)
            st.success(f"Bot: {bot_response}")
        else:
            st.warning("Please enter a message.")

if __name__ == "__main__":
    main()
