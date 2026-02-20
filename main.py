from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

from models.models import AgentSearchResponse

load_dotenv()


llm = ChatOpenAI(model="gpt-5-mini")
tools = [TavilySearch()]


agent = create_agent(model=llm, tools=tools, response_format=AgentSearchResponse)


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
