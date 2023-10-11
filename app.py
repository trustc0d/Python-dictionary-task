import os
import openai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('API_KEY')
openai.api_base = os.getenv("API_BASE")

st.set_page_config(
    page_title="Simple Dictionary",
    page_icon="💡",
    layout="centered",
    initial_sidebar_state="auto",
)

def get_definition(user_input):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt = f"Can you explain {user_input} in simple terms, in one sentence? After the explanation, say something like '[It's/They're] essentially [explanation] 💡.' Please keep your response brief.",
    temperature=0.5,
    max_tokens=112,
    )

    return response.choices[0].text

st.markdown("<h1><center>💡Simple Dictionary</center></h1>", unsafe_allow_html=True)
st.markdown("<h6><center>Enter a word or phrase below to get a simple definition in seconds... 📖</center></h6>", unsafe_allow_html=True)

user_input = st.text_input(" ", placeholder="[word or phrase]", label_visibility="hidden")
chat_button = st.columns((5, 3, 5))[1].button("Get Definition ✨")
st.write("")
if chat_button and user_input.strip() != "":
    with st.spinner("Loading... 🤓"):
        st.info(get_definition(user_input))

st.markdown("<hr><center>© Omar Anwar 2023</center><hr>", unsafe_allow_html=True)
st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)