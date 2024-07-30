#Import streamlit package
import streamlit as st

#Set a title
st.title("Simple Bot using Streamlit")

#Give simple introductory comment
st.write("""

This bot will echo what you tell it by saying Thank you for telling me xxx

""")

#Check if there's previous history
if "messages" not in st.session_state:
    st.session_state.messages = []

#To display history messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


prompt = st.chat_input("What is in your mind?")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("assistant"):
        response = "Thank you for telling me " + prompt
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})