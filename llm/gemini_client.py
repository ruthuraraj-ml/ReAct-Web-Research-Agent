from google import genai

from config import GEMINI_API_KEY, MODEL_NAME


class GeminiClient:
    def __init__(self):
        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def generate(self, prompt: str) -> str:

        response = self.client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        if hasattr(response, "text"):
            return response.text

        return ""

    def generate_questions(self, topic: str):

        prompt = f"""
You are a research planning assistant.

Generate exactly 6 research questions about:

{topic}

Requirements:
- Cover definition
- Applications
- Benefits
- Challenges
- Ethics
- Future trends

Return only the questions.
One question per line.
Do not number them.
Do not add explanations.
"""

        text = self.generate(prompt)

        questions = [
            q.strip()
            for q in text.split("\n")
            if q.strip()
        ]

        return questions
    
    def summarize_search_results(self, question: str, search_results: list):

        results_text = ""

        for idx, result in enumerate(search_results, start=1):

            results_text += f"""
            Result {idx}
            
            Title:
            {result['title']}
            
            Content:
            {result['content']}"""

        prompt = f"""
        You are a research analyst.

        Research Question:
        {question}
    
        Search Results:
        {results_text}
    
        Task:
        Analyze the search results and identify the most important findings.
    
        Return:
        Return 3-5 concise bullet points.

        Each bullet:
        - Maximum 25 words
        - No sub-explanations
        - No introductory text
    
        Do not write an essay.
        Do not repeat information.
        Focus on key insights only.
        """

        summary = self.generate(prompt)

        return summary
    
    def beautify_report(self, topic, findings):

        findings_text = ""

        for entry in findings:

            findings_text += f"""
    Question:
    {entry['question']}

    Summary:
    {entry['summary']}

    """

        prompt = f"""
    You are an expert research report writer.

    Topic:
    {topic}

    Research Findings:
    {findings_text}

    Create a concise consolidated report.

    Requirements:

    - Maximum 600 words
    - Professional academic tone
    - Do not repeat every finding individually
    - Synthesize common themes

    Structure:

    1. Overview
    2. Key Concepts
    3. Benefits and Applications
    4. Challenges and Limitations
    5. Future Directions
    6. Conclusion

    Return only the report.
    """

        return self.generate(prompt)