from agent import ResearchAgent
from trace_generator import TraceGenerator
from report_generator import ReportGenerator


def main():

    topic = input(
        "Enter research topic: "
    )

    agent = ResearchAgent()

    findings = agent.run(topic)

    consolidated_report = (
        agent.llm.beautify_report(
            topic,
            findings
        )
    )

    trace = TraceGenerator().generate(
        findings
    )

    with open(
        "outputs/trace.md",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(trace)

    print(
        "\nTrace saved to outputs/trace.md"
    )

    report = ReportGenerator().generate(
        topic,
        findings,
        consolidated_report
    )

    with open(
        "outputs/report.md",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)

    print(
        "\nReport saved to outputs/report.md"
    )

if __name__ == "__main__":
    main()