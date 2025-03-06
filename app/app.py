import streamlit as st
import utils

st.set_page_config(page_title="LAHS Chatbot", page_icon=":eagle:")
st.title("LAHS AI")

with st.spinner("Loading data..."):
    retriver = utils.get_retriever()

with st.form(key="user_input", clear_on_submit=False):
    prompt = st.text_input("Enter your question here")
    submit = st.form_submit_button("Ask")

if(prompt and submit):
    chunks = retriver.invoke(prompt)
    response = utils.get_response(utils.rewrite_prompt(prompt, chunks))
    st.write(response)