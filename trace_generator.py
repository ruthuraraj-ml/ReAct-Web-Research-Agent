class TraceGenerator:

    def generate(self, entries):

        trace = []

        trace.append("# ReAct Research Trace\n")

        for entry in entries:

            trace.append(
                f"\n## Question {entry['id']}\n"
            )

            trace.append(
                f"### Question\n"
                f"{entry['question']}\n"
            )

            trace.append(
                f"\n### Thought\n"
                f"{entry['thought']}\n"
            )

            trace.append(
                f"\n### Action\n"
                f"{entry['action']}\n"
            )

            trace.append(
                f"\n### Observation\n"
                f"{entry['observation']}\n"
            )

            trace.append(
                f"\n### Summary\n"
                f"{entry['summary']}\n"
            )

            trace.append(
                "\n---\n"
            )

        return "\n".join(trace)