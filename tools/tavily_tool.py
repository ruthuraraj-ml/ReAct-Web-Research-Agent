from tavily import TavilyClient

from config import (
    TAVILY_API_KEY,
    MAX_SEARCH_RESULTS
)


class TavilySearchTool:

    def __init__(self):

        self.client = TavilyClient(
            api_key=TAVILY_API_KEY
        )

    def search(self, query: str):

        response = self.client.search(
            query=query,
            max_results=MAX_SEARCH_RESULTS
        )

        results = []

        for result in response.get("results", []):

            results.append(
                {
                    "title": result.get("title", ""),
                    "content": result.get("content", "")[:1000],
                    "url": result.get("url", "")
                }
            )

        return results