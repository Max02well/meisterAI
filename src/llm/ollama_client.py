from openai import OpenAI,APIConnectionError
import os

client = OpenAI(
    # base_url="http://localhost:11434/v1",
    # api_key="ollama"
    api_key=os.getenv("LLM_API_KEY", ""),
    base_url=os.getenv("LLM_BASE_URL", "http://localhost:11434/v1"),
)

def generate(prompt):
    try:
        response = client.chat.completions.create(

            # model="llama3.1",
            # model="qwen2.5:7b",
             model=os.getenv("LLM_MODEL"),

            temperature=0,
            # stream= True,

            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )

        return response.choices[0].message.content
    except APIConnectionError:
        return "Unable to connect to the configured LLM provider."
    except Exception as e:
        return f"LLM Error: {e}"
