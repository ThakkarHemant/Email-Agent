import warnings
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from utils.parser import clean_input
warnings.filterwarnings("ignore")

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
    temperature=0.7,
    google_api_key=google_api_key
)

# Define prompt
template = PromptTemplate(
    input_variables=["raw_input"],
    template="""
You are a professional email-writing assistant.

Your task is to convert the following informal or incomplete English input from a non-native speaker into a professional, formal email.

If any information is missing (like recipient name, exact date, etc.), make polite assumptions and generate a complete email anyway.

Input: {raw_input}

Return only:
Subject: <subject line>
Email:
<email body>
"""
)

# Create a chain
email_chain = LLMChain(llm=llm, prompt=template)

def run_email_agent(user_input: str) -> str:
    cleaned = clean_input(user_input)
    result = email_chain.invoke({"raw_input": cleaned})
    return result["text"]
