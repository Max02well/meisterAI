from src.llm.assistant import MeisterAI

assistant = MeisterAI()
#This is a simple command-line interface to interact with the MeisterAI assistant.(for CLI use only)
# It continuously prompts the user for questions, processes them through the assistant, and displays the answers along with their sources. 
# The loop continues until the user types "exit" or "quit".

while True:

    question = input("\nAsk MeisterAI > ")

    if question.lower() in ["exit", "quit"]:

        break

    answer, docs = assistant.ask(question)

    print("\n")

    print(answer)

    print("\nSources")

    print("="*60)

    for doc in docs:

        meta = doc["metadata"]

        print(

            f"{meta['manual']} - Page {meta['page']}"

        )