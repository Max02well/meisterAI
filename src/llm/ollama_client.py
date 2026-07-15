from openai import OpenAI,APIConnectionError

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

def generate(prompt):
    try:
        response = client.chat.completions.create(

            # model="llama3.1",
            model="qwen2.5:7b",

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
        return "Unable to connect to the Ollama server."
    except Exception as e:
        return f"LLM Error: {e}"