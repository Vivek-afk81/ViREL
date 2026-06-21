from langchain_core.prompts import PromptTemplate

dynamic_prompt=PromptTemplate(
    template="Write a short fun fact about {topic} in {style} style",
    input_variables=["topic","style"],
)

prompt_text=dynamic_prompt.format(topic="One piece",style="humorous")
#now you can use this template to create new prompt
prompt1=dynamic_prompt.format(topic="rasmalai",style="funny")
print(prompt_text)