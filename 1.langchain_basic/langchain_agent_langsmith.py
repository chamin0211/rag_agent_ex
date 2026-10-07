from langchain.agents import create_agent

# 상위 폴더 paht 설정 -> common_config.py 모듈 인식을 위해 설정
import sys
sys.path.append("..")

from common_config import llm_connect
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_agent(
    model=llm_connect(),
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What is the weather in San Francisco?"}]}
)

print(result)