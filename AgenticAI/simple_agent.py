from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_core.tools import tool
import math
from dotenv import load_dotenv

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

@tool
def add(a:float,b:float)->float:
    """ add two numbers"""
    return a+b

def multiply(a:float,b:float)->float:
    """ multiply two numbers"""
    return a*b


def square_root(a:float)->float:
    """ square root of a number"""
    return math.sqrt(a)


agent = create_agent(
    model=model,
    tools=[add,multiply,square_root]
)

def run_agent(question: str):
    print(f"User : {question}")

    result = agent.invoke({
        "messages": [("user", question)]
    })

    answer = result["messages"][-1].content
    return answer

print(run_agent("What is the square root of 16?"))

