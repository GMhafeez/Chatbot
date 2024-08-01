import requests
import streamlit as st

# def get_openai_response(input_text):
#     response = requests.post("http://localhost:8000/essay/invoke",
#                              json={"input":{"topic":input_text }})
#     return response.json()["output"]

def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
    json={"input":{"topic":input_text }})
    return response.json()["output"]
#streamlit framework

st.title("lagchain demo with OpenApi and Gemma API")
input_text2 = st.text_input("write an essay on")

# if input_text:
#     st.write(get_openai_response(input_text))
if input_text2:
    st.write(get_ollama_response(input_text2))
 