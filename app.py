import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# Enable Langsmith Tracking
os.environ["LANGCHAIN_TRACKING_V2"] = "true"

# Prompt template

prompt = ChatPromptTemplate(
    [
        ("system", "You are a anime expert asistant. Please respond preciecly all anime related questions"),
        ("user", "Question:{question}")
    ]
)

# Streamlit framework
st.title("Langchain Demo - Anime Assistant Using gemma:2b")
input_text = st.text_input(label="Ask Question", value="Enter you question here")

# Call ollama model
model_name = "gemma:2b"
llm = Ollama(model=model_name)

output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if st.button("Generate"):
    st.write(chain.invoke({"question":input_text}))
