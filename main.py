from openai import AsyncOpenAI
import asyncio
from agents import Runner,set_tracing_disabled
from my_agents.weather_agent import weather_agent
from my_schema.agent_output import Weather

set_tracing_disabled(True)
# result= Runner.run_sync(starting_agent=weather_agent, input="What is weather in Karachi?")
# print("Result",result.final_output)


async def main():
    agent = weather_agent
    prompt = input("Enter your question : ")
    result = await Runner.run(agent, prompt)
    print(result.final_output)
   


if __name__ == "__main__":
 

    asyncio.run(main())
