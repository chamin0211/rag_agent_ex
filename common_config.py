from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv(override=True)

BASE_URL = "https://monogpt.kr/api/monorouter/v1"
api_key = os.getenv("LLM_API_KEY")

def llm_connect(
    model: str,
    temperature: float = 0,
    max_tokens: int = 512
):
    return ChatOpenAI(
        model=model,
        api_key=api_key,
        base_url=BASE_URL,
        temperature=temperature,
        use_responses_api=False,  # base url로 할 때는 이부분 넣어야 함.(MonoRouter 사용)
        max_tokens=max_tokens,
    )