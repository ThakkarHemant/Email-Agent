from langchain.agents import Tool
from agent.prompts import prompt_email_generator
from utils.parser import clean_input

def write_email(text: str) -> str:
    clean = clean_input(text)
    return prompt_email_generator(clean)

tools = [
    Tool.from_function(
        func=write_email,
        name="EmailWriter",
        description="Generates professional emails from informal prompts."
    )
]
