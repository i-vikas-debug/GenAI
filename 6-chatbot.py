import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os

# Set LangChain API key from environment variable (only if already set in your system)
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Set tracking as a string value
os.environ["LANGCHAIN_TRACKING_V2"] = "true"

# Set the LangChain project name
os.environ["LANGCHAIN_PROJECT"] = "Q and A chat bot app"

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system","Answer to query"),
    ("user","qustion:{question}")
])

from langchain_groq import ChatGroq

groq_api_key = os.getenv("GROQ_API_KEY")

from langchain_core.output_parsers import StrOutputParser


def generate_response(question,api_key,llm):
    llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser
    ans = chain.invoke({"question":question})
    return ans 

st.title("Welcome to the Q&A ChatBot app")
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama3-8b-8192")
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("enter your api key", type="password")

user_input = st.text_input("Ask Anything")
if user_input:
    response = generate_response(user_input,api_key,llm)
    st.write(response)
