import streamlit as st
from dataclasses import dataclass
from models import get_response_from_LLMS

st.set_page_config(layout='wide')
st.title("Start a Statement You Believe Is Right")

@dataclass
class Message:
    actor: str
    payload: str

USER = "user"
ASSISTANT1 = "assistant"
ASSISTANT2 = "assistant"
MESSAGES = "messages"

if MESSAGES not in st.session_state:
    st.session_state[MESSAGES] = [Message(actor=ASSISTANT1, payload="WE ARE READY FOR THE DISCUSION")]

msg: Message
for msg in st.session_state[MESSAGES]:
    st.chat_message(msg.actor).write(msg.payload)

prompt: str = st.chat_input("Enter a prompt here")
if prompt:
    st.session_state[MESSAGES].append(Message(actor=USER, payload=prompt))
    st.chat_message(USER, avatar='🧐').write(prompt)

    response1, response2 = get_response_from_LLMS(prompt)
    st.session_state[MESSAGES].append(Message(actor=ASSISTANT1, payload=response1))
    st.chat_message(ASSISTANT1, avatar='🐫').write(response1) 
    
    st.session_state[MESSAGES].append(Message(actor=ASSISTANT2, payload=response2))
    st.chat_message(ASSISTANT2, avatar='🦖').write(response2) 