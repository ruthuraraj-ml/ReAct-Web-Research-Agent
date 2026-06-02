class ResearchMemory:

    def __init__(self):

        self.entries = []

    def add_entry(
        self,
        question,
        thought,
        action,
        observation,
        summary,
        sources
    ):

        entry = {
            "id": len(self.entries) + 1,

            "question": question,

            "thought": thought,

            "action": action,

            "observation": observation,

            "summary": summary,

            "sources": sources
        }

        self.entries.append(entry)

    def get_all(self):

        return self.entries

    def get_entry(self, entry_id):

        for entry in self.entries:

            if entry["id"] == entry_id:
                return entry

        return None

    def count(self):

        return len(self.entries)