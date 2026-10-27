from mcp.server.mcpserver import MCPServer

server = MCPServer(name="course-local-demo")

COURSE_TOPICS = {
    1: "LLM foundations and prompting",
    2: "Function calling and tool use",
    3: "Model Context Protocol (MCP)",
}


@server.tool()
def add_numbers(a: float, b: float) -> dict:
    """Add two numbers and return the operands and sum."""
    return {"a": a, "b": b, "sum": a + b}


@server.tool()
def get_course_topic(module_number: int) -> dict:
    """Return the topic taught in a numbered course module."""
    topic = COURSE_TOPICS.get(module_number)
    if topic is None:
        return {
            "module_number": module_number,
            "error": "Unknown module number",
        }
    return {"module_number": module_number, "topic": topic}


@server.tool()
def word_count(text: str) -> dict:
    """Count whitespace-separated words in text."""
    return {"text": text, "word_count": len(text.split())}


if __name__ == "__main__":
    server.run(transport="stdio")
