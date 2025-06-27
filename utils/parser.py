import re

def clean_input(text: str) -> str:
    # Remove extra spaces, fix casing if needed
    return re.sub(r'\s+', ' ', text.strip())
