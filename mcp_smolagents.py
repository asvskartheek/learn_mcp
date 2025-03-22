from smolagents import ToolCollection, CodeAgent
from mcp import StdioServerParameters

# Gemini
from smolagents import LiteLLMModel
from dotenv import load_dotenv
import os

load_dotenv()
model = LiteLLMModel(
    model_id="gemini/gemini-2.0-flash", 
    temperature=0.4,
    api_key=os.environ["GEMINI_API_KEY"]
)

# OpenRouter
# from smolagents import LiteLLMModel
# from dotenv import load_dotenv
# import os

# load_dotenv()
# model = LiteLLMModel(
#     model_id="openrouter/qwen/qwq-32b:free",
#     temperature=0.6,
#     api_key=os.environ["OPENROUTER_API_KEY"]
# )

server_parameters = StdioServerParameters(
    command="uvx",
    args=["--quiet", "pubmedmcp@0.1.3"],
    env={"UV_PYTHON": "3.12", **os.environ},
)

with ToolCollection.from_mcp(server_parameters) as tool_collection:
    agent = CodeAgent(tools=[*tool_collection.tools], model=model, add_base_tools=True, planning_interval=10)
    agent.run("Please find a remedy for hangover.")