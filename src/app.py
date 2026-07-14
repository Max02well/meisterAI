from src.llm.assistant import MeisterAI

assistant = MeisterAI()

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