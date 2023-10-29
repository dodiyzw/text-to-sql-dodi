import sys
sys.path.append("/Users/dodi/Documents/repository/text-to-sql-dodi")

import streamlit as st
from main.backend import flant5

st.title("Text to SQL Generator")
st.caption("Chatbot powered by flan-t5, put together by Dodi ;)")

# static default message when not in use, i.e. when the session state doesn't have the key "messages"
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you with SQL today?"}]
    
# appends the messages by looping through them in the chatbot.
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    
# creates the prompt bar
# prompt = st.chat_input("Say something")
# if prompt:
if prompt := st.chat_input(placeholder="Enter your SQL query here"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    print(prompt)
    st.chat_message("user").write(prompt)
    ## update it such that it takes the last entry, and then pass the content only.
    model_output_message = flant5.inference2(question_and_table=st.session_state.messages[-1]["content"])
    st.session_state.messages.append({"role": "assistant", "content": model_output_message})
    st.chat_message("assistant").write(model_output_message)
    # user has provided prompt at this point. We want to take it and pass it into model
    