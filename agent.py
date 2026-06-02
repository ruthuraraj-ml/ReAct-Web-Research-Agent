from llm.gemini_client import GeminiClient
from llm.groq_client import GroqClient
from tools.tavily_tool import TavilySearchTool
from memory import ResearchMemory


class ResearchAgent:

    def __init__(self):

        self.llm = GeminiClient()

        self.groq = GroqClient()

        self.search_tool = TavilySearchTool()

        self.memory = ResearchMemory()

    def run(self, topic):

        questions = self.llm.generate_questions(
            topic
        )

        for question in questions:

            thought = self.groq.generate_thought(
                question
                )
            print("\n[Thought]")
            print(thought)

            action = "search_web"

            results = self.search_tool.search(
                question
            )

            observation = (
                self.groq.generate_observation(
                    question,
                    results
                )
            )
            print("\n[Observation]")
            print(observation)

            summary = (
                self.llm.summarize_search_results(
                    question,
                    results
                )
            )
            print("\n[Summary]")
            print(summary)


            sources = [
                result["url"]
                for result in results
            ]

            self.memory.add_entry(
                question=question,

                thought=thought,

                action=action,

                observation=observation,

                summary=summary,

                sources=sources
            )

        return self.memory.get_all()