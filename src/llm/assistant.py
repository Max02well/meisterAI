from src.retrieval.retriever import Retriever

from src.llm.prompt import build_prompt

from src.llm.ollama_client import generate


class MeisterAI:

    def __init__(self):

        self.retriever = Retriever()

    def ask(self, question):

        #
        # Retrieve documents
        #

        documents = self.retriever.search(question)

        #
        # Build prompt
        #

        prompt = build_prompt(
            question,
            documents
        )

        #
        # Generate answer
        #

        answer = generate(prompt)

        return answer, documents