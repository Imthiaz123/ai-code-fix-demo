import streamlit as st
import openai

st.title('AI Bug Fix Assistant')

code_input = st.text_area('Paste your Python code here:')

if st.button('Suggest Fixes'):
    if code_input.strip():
        st.subheader('AI Suggestions:')
        st.write('This is where OpenAI API output will go.')
    else:
        st.warning('Please paste some code first.')
