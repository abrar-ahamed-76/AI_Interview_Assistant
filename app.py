import streamlit as st
from groq import Groq
st.set_page_config(page_title = 'AI Interview Assistant', page_icon='🎯', layout='centered')
st.title('🎯AI Interview Assistant')
st.caption('practice interviews with Ai-generated questions and constructive feedback.')
st.caption('Built by : ABRAR AHAMED 😎')
try: 
    client = Groq(api_key=st.secrets['GROQ_API_KEY'])
    st.write("API Connection successful")
except (keyError, FileNotFoundError):
    st.error('GROQ_API_KEY is missing.Add it to streamlit Clode->App setting secrets")
    st.stop()
