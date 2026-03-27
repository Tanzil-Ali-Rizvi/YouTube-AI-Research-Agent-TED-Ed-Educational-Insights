from pydantic_ai import Agent
from agent.tools import TedEdTools

tools = TedEdTools()
agent = Agent(
    'openai:gpt-4o',
    system_prompt="You are a research assistant specializing in youth education and mental health using TED-Ed lessons.",
)

@agent.tool
def search_ted_ed(ctx, query: str):
    return tools.search_lessons(query)

async def ask_agent(question: str):
    result = await agent.run(question)
    print(result.data)

if __name__ == "__main__":
    import asyncio
    asyncio.run(ask_agent("What do TED-Ed lessons say about the impact of social media on teen sleep?"))
