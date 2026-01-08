from langchain_openai import OpenAI   # using langchain-openai package
# using openai package alternate for openai integration
from langchain_huggingface import ChatHuggingFace # using openai package alternate for openai integration
from dotenv import load_dotenv

load_dotenv()

# llm = OpenAI(model='gpt-3.5-turbo-instruct')

llm = ChatHuggingFace(repo_id="google/flan-t5-large")

result = llm.invoke("What is AI?")

print(result)