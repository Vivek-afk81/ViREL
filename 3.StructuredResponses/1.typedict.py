from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()
model=ChatGroq(model_name="llama-3.3-70b-versatile")

#schema

class Review(TypedDict):
    summary:str
    sentiment:str

prompt="""The hardware is great, but the software feels bloateed.
There are too many pre-installed apps that I never use and can't uninstall.
The battery life is decent, but it could be better.
Also the UI lools outdated compared to other brands.
Hoping for a software update to fix this. Overall, it's an average phone with some
good features but also some drawbacks."""

# response=model.invoke(prompt)
# print(response.content)


structured_model=model.with_structured_output(Review)
structured_response=structured_model.invoke(prompt)
print(structured_response)