import os 
from dotenv import load_dotenv 
from google import genai

load_dotenv()

client=genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
def calculate(a:float,b:float,operation:str) -> float:
    """
    performs a basic mathematical calculation.

    Args:
    a:First number.
    b:second number.
    operation:add,subtract,multiply or divide    
    """
    if operation =="add":
        return a+b
    if operation == "subtract":
        return a-b
    if operation == "multiply":
        return a *b
    if operation == "divide":
        if b==0:
            return "Cannot divide by zero"
        return a/b
    return "unknown operation you might have meant something"
chat = client.chats.create(
    model="gemini-3.6-flash",
    config={
        "tools": [calculate]
    }
)


def ask(question: str):

    response = chat.send_message(question)

    return response.text
