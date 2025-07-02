import streamlit as st
from jarvis_logic import process_command

st.title(" Jarvis AI - Text Command Assistant")

command = st.text_input("Type your command:")

if st.button("Send"):
    if command:
        response = process_command(command)
        st.success(response)
    else:
        st.warning("Please type a command.")
