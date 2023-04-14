import os


from langchain.memory import ConversationBufferMemory
from langchain.memory import RedisChatMessageHistory

from tools import CancelLicense, RenewLicense

from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

from langchain.agents.tools import Tool

chat = ChatOpenAI(temperature=0, verbose=True)
llm = OpenAI(temperature=0, model_name="text-davinci-003")


tools = [
    RenewLicense(),
    CancelLicense(),
]

# history = RedisChatMessageHistory("foo")
memory = ConversationBufferMemory(memory_key="chat_history")


agent = initialize_agent(
    tools, chat, agent="chat-zero-shot-react-description", verbose=True, memory=memory
)

response = chat(
    [
        SystemMessage(
            content="you are..."
        )
    ]
)
print(response)


agent.run("Please cancel the license 1234567890 and renew 999999999")
