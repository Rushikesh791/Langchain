from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
load_dotenv()

llm = ChatHuggingFace(repo_id="google/flan-t5-large")

result = llm.invoke("What is AI?")

print(result)
