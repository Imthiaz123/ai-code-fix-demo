import streamlit as st
st.title('AI Bug Fix Assistant')
code = st.text_area('Paste your Python code:')
if st.button('Suggest Fixes'):
    if not code.strip():
        st.warning('Please paste some code first.')
    else:
        st.write('🔧 This is where AI suggestions will appear (connect OpenAI API).')
