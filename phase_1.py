# Part 1: Setup a Streamlit UI
import warnings
import logging

import streamlit as st

# Disable warnings and info logs
warnings.filterwarnings("ignore")
logging.getLogger("transformers").setLevel(logging.ERROR)

st.title('Ask Chatbot!')
# Setup a session state variable to hold all the old messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display all the historical messages
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

prompt = st.chat_input('Pass your prompt here')

if prompt:
    st.chat_message('user').markdown(prompt)
    # Store the user prompt in state
    st.session_state.messages.append({'role':'user', 'content': prompt})
    response = "I am your assistant"
    st.chat_message('assistant').markdown(response)
    st.session_state.messages.append(
            {'role':'assistant', 'content':response})


