
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

result = llm.embed_query("What is AI?")

print(result)