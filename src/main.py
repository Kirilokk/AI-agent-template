import asyncio

from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio

from src.logfire_config import init_logfire

init_logfire()

class WeatherReport(BaseModel):
    location: str
    temperature: float
    condition: str
    forecast: str

server = MCPServerStdio(
    'uv', args=['run', '-m', 'src.mcp.server', 'stdio'], timeout=10
)

weather_agent = Agent(
    'openai:gpt-5.2',
    instructions='You are a weather data retrieval assistant. Your task is to return ONLY the current weather.',
    output_type=WeatherReport,
    toolsets=[server],
)


async def main():
    result = await weather_agent.run("I need the current weather right now in Washington state.")
    print(result.output)


if __name__ == "__main__":
    asyncio.run(main())
