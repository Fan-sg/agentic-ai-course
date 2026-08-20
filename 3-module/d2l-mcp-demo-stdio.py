import asyncio
import os

from dotenv import load_dotenv
from agents import Agent, Runner
from agents.mcp import MCPServerStdio


# --------------------------------------------------
# Configuration
# --------------------------------------------------

load_dotenv(override=True)

MODEL = "gpt-4.1-mini"

SERVER_PATH = os.path.abspath(
    "d2l-local-mcp/server.py"
)

server_params = {
    "command": "uv",
    "args": [
        "run",
        "python",
        SERVER_PATH,
    ],
}


# --------------------------------------------------
# Demo 1: Discover MCP Tools
# --------------------------------------------------

async def demo_list_tools():

    print("\n==============================")
    print("DEMO 1 - MCP Tool Discovery")
    print("==============================")

    async with MCPServerStdio(
        params=server_params
    ) as server:

        tools = await server.list_tools()

        print(f"\nFound {len(tools)} tool(s):")

        for tool in tools:
            print(f"\nTool name: {tool.name}")
            print(f"Description: {tool.description}")
            print(f"Input schema: {tool.inputSchema}")


# --------------------------------------------------
# Demo 2: Direct MCP Tool Call
# --------------------------------------------------

async def demo_call_tool():

    print("\n==============================")
    print("DEMO 2 - Direct MCP Tool Call")
    print("==============================")

    async with MCPServerStdio(
        params=server_params
    ) as server:

        result = await server.call_tool(
            "get_current_datetime",
            {}
        )

        print("\nTool result:")
        print(result)


# --------------------------------------------------
# Demo 3: LLM + MCP
# --------------------------------------------------

async def demo_agent():

    print("\n==============================")
    print("DEMO 3 - Agent + MCP")
    print("==============================")

    system_prompt = (
        "Answer time and date questions using "
        "the available tools rather than guessing."
    )

    async with MCPServerStdio(
        params=server_params
    ) as server:

        agent = Agent(
            name="Time Assistant",
            instructions=system_prompt,
            model=MODEL,
            mcp_servers=[server],
        )

        question = (
            "What is the current date and time? "
            "What day of the week is it?"
        )

        print(f"\nUser: {question}")

        result = await Runner.run(
            agent,
            question
        )

        print("\nAssistant:")
        print(result.final_output)


# --------------------------------------------------
# Main
# --------------------------------------------------

async def main():

    await demo_list_tools()

    await demo_call_tool()

    await demo_agent()


if __name__ == "__main__":
    asyncio.run(main())