from openai import OpenAI

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
            stream= True,

            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )

        return response.choices[0].message.content

    except APIConnectionError:
            raise RuntimeError(
                "Could not connect to Ollama. "
                "Make sure Ollama is running by executing 'ollama serve'."
            )