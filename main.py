import streamlit as st
from groq import Groq
from dotenv import load_dotenv, find_dotenv
import os

# Load environment variables
_ = load_dotenv(find_dotenv())
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

st.title("DrepaAI")
st.write("The AI companion of Sickle cell disease patients, doctors and families")

# Initialize session state for the model and messages
if "mistral_model" not in st.session_state:
    st.session_state["mistral_model"] = "mixtral-8x7b-32768"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all messages from session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Capture the user input
prompt = st.chat_input("What is up?")

if prompt:
    # Append user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get assistant's response
    chat_completion = client.chat.completions.create(
        model=st.session_state["mistral_model"],
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ],
    )
    assistant_message = chat_completion.choices[0].message.content

    # Display assistant's response
    with st.chat_message("assistant"):
        st.markdown(assistant_message)

    # Append assistant message to session state
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})
