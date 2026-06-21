from langchain_core.prompts import PromptTemplate

static_prompt=PromptTemplate(
    input_variables=[],
    template="Write a short fun fact"
)

prompt_text=static_prompt.format()
print(prompt_text)