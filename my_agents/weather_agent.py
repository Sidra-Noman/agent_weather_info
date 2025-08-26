from agents import Agent
from my_config.gemini_conf import MODEL
from my_tool.weather_tool import get_weather



weather_agent = Agent(
    name="Weather Assistant",
    instructions="You are helpful weather assistant by calling get weather tool",
    model=MODEL,
    tools=[get_weather]
)