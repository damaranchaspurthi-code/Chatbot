import streamlit as st
import ollama

#page configuration
st.set_page_config(
    page_title="OLLAMA Chatbot",
    page_icon=" ai.jpg"
)

st.title(" My OLLAMA CHATBOT")
st.caption("Powered by Ollama + Streamlit")

if "messages" not in st.session_state:
    st.session_state.messages = []

#Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

#Chat input
prompt = st.chat_input("Type your message...")

if prompt:

    # Store user messsage
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    # Get response from Ollama
    response = ollama.chat(
        model="llama3.2",
        messages=st.session_state.messages
    )

    answer = response["message"]["content"]

    # Store AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    # Display AI response
    with st.chat_message("assistant"):
        st.write(answer)