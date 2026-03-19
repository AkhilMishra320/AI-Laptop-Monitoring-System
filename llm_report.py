def generate_report(event_text: str) -> str:
    """
    Later this will call real LLM API.
    For now we simulate intelligent report.
    """

    return (
        "Security Alert:\n"
        f"{event_text}\n"
        "The system detected suspicious activity and responded automatically."
    )