class IntentDetector:
    """
    Detects the user's intent from the question.
    """

    def detect(self, question: str) -> str:

        question = question.lower()

        # Resume related
        if any(word in question for word in [
            "resume",
            "cv",
            "ats",
            "job",
            "interview"
        ]):
            return "resume"

        # Teaching / Explanation
        if any(word in question for word in [
            "explain",
            "understand",
            "teach",
            "why",
            "how"
        ]):
            return "teacher"

        # Summaries
        if any(word in question for word in [
            "summary",
            "summarize",
            "overview"
        ]):
            return "summary"

        # Financial
        if any(word in question for word in [
            "stock",
            "market",
            "finance",
            "investment",
            "share"
        ]):
            return "finance"

        # Research
        if any(word in question for word in [
            "research",
            "paper",
            "journal"
        ]):
            return "research"

        # Default
        return "general"