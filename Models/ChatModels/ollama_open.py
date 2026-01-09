
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatOllama(
    model="llama2",
    base_url="http://localhost:11434"
)

response = llm.invoke([
    HumanMessage(content="What is AI?")
])

print(response.content)

