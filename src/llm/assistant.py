from src.retrieval.retriever import Retriever

from src.llm.prompt import build_prompt

from src.llm.ollama_client import generate
import time


class MeisterAI:

    def __init__(self):

        self.retriever = Retriever()

    def ask(self, question):

        #
        # Retrieve documents
        #
        start = time.time()
        documents = self.retriever.search(question)
        
        print(f"Retrieval: {time.time()-start:.2f}s")

        #
        # Build prompt
        #

        prompt = build_prompt(
            question,
            documents
        )
        llm_start = time.time()

        #
        # Generate answer
        #

        answer = generate(prompt)
        print(f"LLM: {time.time()-llm_start:.2f}s")

        print(f"Total: {time.time()-start:.2f}s")
    

        return answer, documents