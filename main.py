from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()


llm = ChatOpenAI(model="gpt-5-mini")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    result = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content="Search if it is worth to shift from frontend developer to AI Engineer on 2026?"
                )
            ]
        }
    )
    print(result)


if __name__ == "__main__":
    main()
