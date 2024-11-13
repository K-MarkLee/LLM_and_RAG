import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


os.environ["OPENAI_API_KEY"] = os.getenv("GPT_API")


model = ChatOpenAI(model="gpt-4")


system_template = "Translate the following sentence from English to {lang} : "

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{text}")
])

message = {"lang":"Korean", "text":"Its been a long day without you my friend"}

parser = StrOutputParser()


chain = prompt_template | model | parser

response = chain.invoke(message)
print(response)

response = chain.invoke({f"lang":"English","text":response})
print(response)