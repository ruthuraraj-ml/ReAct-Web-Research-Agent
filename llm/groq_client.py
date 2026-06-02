from groq import Groq

from config import GROQ_API_KEY


class GroqClient:

    def __init__(self):

        self.client = Groq(
            api_key=GROQ_API_KEY
        )

        self.model = "llama-3.3-70b-versatile"

    def generate(self, prompt):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    def generate_thought(
        self,
        question
    ):

        prompt = f"""
You are the reasoning component of a ReAct research agent.

Research Question:
{question}

Generate a concise thought describing
what information should be gathered.

Return only the thought.

Maximum 30 words.
"""

        return self.generate(prompt)

    def generate_observation(
        self,
        question,
        search_results
    ):

        results_text = ""

        for idx, result in enumerate(
            search_results,
            start=1
        ):

            results_text += f"""
Result {idx}

Title:
{result["title"]}

Content:
{result["content"][:150]}
"""

        prompt = f"""
You are a ReAct research agent.

Research Question:
{question}

Search Results:
{results_text}

Generate an observation ONLY from the search results.

Do not use external knowledge.

Identify the 2–3 most common themes
appearing across the retrieved sources.

Return only the observation.

Maximum 40 words.
"""

        return self.generate(prompt)