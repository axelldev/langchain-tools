from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient()


@tool
def search(query: str) -> str:
    """ "
    Tool that searches the web for information.
    Args:
        query: The query to search the web fro.
    Returns:
        The information found on the web.
    """
    print(f"Searching the web for {query}")
    return tavily.search(query=query)


llm = ChatOpenAI(model="gpt-5-mini")
tools = [search]
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
