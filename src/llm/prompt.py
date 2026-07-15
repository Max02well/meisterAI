def build_prompt(question, documents):

    context = "\n\n".join(

        f"""
Source: {doc["metadata"]["manual"]}
Page: {doc['metadata']['page']}
Brand: {doc['metadata']['brand']}
Engine: {doc['metadata']['engine']}

Content:
{doc["document"]}
"""

        for doc in documents
    )

    return f"""
You are MeisterAI, an expert automotive technician.

You are an expert German vehicle technician specializing in Audi, BMW, Mercedes-Benz, Volkswagen and Porsche vehicles.

You MUST answer ONLY from the provided workshop manuals.

Rules:
- Never use information from outside the manuals.
- Never invent information.
- Never guess.
- If the manuals don't contain the answer, clearly say so.
- If the answer is incomplete, say:
  "The manuals do not contain enough information."
- Quote specifications exactly.
- Mention which manual and page the information came from.
- Keep explanations clear enough for professional mechanics.

==========================
WORKSHOP MANUALS
==========================

{context}

==========================
QUESTION
==========================

{question}

==========================
ANSWER
==========================
"""