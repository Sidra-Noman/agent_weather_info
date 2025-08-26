from agents import function_tool
import requests




@function_tool
def get_weather(city: str):
  """
  Get the weather of a provided city (mocked).
  """
  return {"city": city, "temperature": "35", "condition": "Sunny"}
