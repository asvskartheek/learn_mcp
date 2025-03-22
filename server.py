# server.py is a simple example of a FastMCP server
from mcp.server import FastMCP

server = FastMCP("Demo")

@server.tool("add")
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@server.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Return a greeting"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    server.run() # this is needed to start the server, even for running the inspector this is needed.