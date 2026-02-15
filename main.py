from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

load_dotenv()


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
    return "Tokyo weather is sunny"


llm = ChatOpenAI(model="gpt-5-mini")
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    result = agent.invoke(
        {"messages": [HumanMessage(content="What is the weather in Tokyo?")]}
    )
    print(result)


if __name__ == "__main__":
    main()
