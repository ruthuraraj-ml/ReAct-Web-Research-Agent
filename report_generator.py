class ReportGenerator:

    def generate(
        self,
        topic,
        entries,
        consolidated_report=None
    ):

        report = []

        report.append(
            f"# Research Report: {topic}\n"
        )

        report.append(
            "## Introduction\n"
        )

        report.append(
            f"This report presents findings gathered by the ReAct Research Agent on the topic: {topic}.\n"
        )

        report.append(
            "\n# Research Questions and Findings\n"
        )

        for entry in entries:

            report.append(
                f"\n## {entry['question']}\n"
            )

            report.append(
                f"{entry['summary']}\n"
            )

            report.append(
                "\n### Sources\n"
            )

            for source in entry["sources"]:

                report.append(
                    f"- {source}"
                )

            report.append("\n")

        if consolidated_report:

            report.append(
                "\n# Consolidated Analysis\n"
            )

            report.append(
                consolidated_report
            )

        return "\n".join(report)