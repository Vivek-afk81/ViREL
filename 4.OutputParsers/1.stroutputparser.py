from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model=ChatGroq(model_name="llama-3.3-70b-versatile")

# 1st prompt template
template1=PromptTemplate(template="Write a detailed report on {topic}",
                         input_variables=['topic']
)

# 2nd prompt template
template2=PromptTemplate(template="Write a 5 line summary on the following {text}",
                         input_variables=['text']
)

parser=StrOutputParser()

chain=template1 | model | parser | template2 | model | parser

response=chain.invoke({'topic':"Black Hole"})
print(response)