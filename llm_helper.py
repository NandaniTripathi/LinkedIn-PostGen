
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY is missing. Please configure it in your environment."
    )

llm = ChatGroq(
    groq_api_key=api_key,
    model_name="openai/gpt-oss-20b",
    temperature=0.7,
)

if __name__ == "__main__":
    response = llm.invoke(
        "Two most important ingredients in samosa are"
    )

    print(response.content)




