from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from common.config import (
    API_KEY,
    BASE_URL,
    EMBEDDING_MODEL,
    MODEL,
)

def get_llm_model(
    model: str = MODEL,
    api_key: str = API_KEY,
    temperature: float = 0,
    max_tokens: int = 512
):
    return ChatOpenAI(
        model=MODEL,
        api_key=API_KEY,
        base_url=BASE_URL,  # MonoRouter 사용 시 필요, .env의 LLM_BASE_URL을 읽음
        temperature=temperature,
        use_responses_api=False,  # base url로 할 때는 이부분 넣어야 함.(MonoRouter 사용)
        max_tokens=max_tokens,
    )


def get_embedding_model():
    embedding_model = EMBEDDING_MODEL
    embeddings = OpenAIEmbeddings(
        api_key=API_KEY,
        base_url=BASE_URL,
        model=embedding_model
    )
    return embeddings