from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_community.llms import Ollama
import streamlit as st
import os
 
from dotenv import load_dotenv

api_key_1 = os.getenv("OPENAI_API_KEY")

api_key_2 = os.getenv("LANGCHAIN_API_KEY")

if api_key_1:
    os.environ["OPENAI_API_KEY"] = api_key_1
    print("API key loaded successfully.")
else:
    print("Warning: OPENAI_API_KEY not found in environment variables.")

## LangSmith tracking
os.environ["LANGCHAIN_TRACKING_V2"] = "true"

if api_key_2:
    os.environ["OPENAI_API_KEY"] = api_key_1
    print("API key loaded successfully.")
else:
    print("Warning: OPENAI_API_KEY not found in environment variables.")    

prompt = ChatPromptTemplate.from_messages(
    [
        ("system, you are helpful assistant. please response to user querires"),
        ("user", "Question: {question}")
    ]
)
## stream lit 
st.title("langchain demo with Gemma")
input_text = st.text_input("Search the topic u want")
 
# Ollama  llm 
llm = Ollama (model = "gemma")

output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))