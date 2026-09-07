from enum import Enum


class Task(str, Enum):
    SUMMARIZE = "summarize"
    EXPLAIN = "explain"
    ANALYZE = "analyze"
    COMPARE = "compare"
    EXTRACT = "extract"
    FIND = "find"
    ANSWER = "answer"
    GENERATE = "generate"
    RECOMMEND = "recommend"
    REVIEW = "review"
    REWRITE = "rewrite"
    TRANSLATE = "translate"
    CLASSIFY = "classify"
    CHAT = "chat"


class TaskDetector:

    def detect(self, question: str) -> Task:

        q = question.lower().strip()

        # ----------------------------
        # Summarize
        # ----------------------------
        if any(keyword in q for keyword in [
            "summarize",
            "summary",
            "summarise",
            "brief",
            "overview",
            "key points",
            "tl;dr"
        ]):
            return Task.SUMMARIZE

        # ----------------------------
        # Explain
        # ----------------------------
        if any(keyword in q for keyword in [
            "explain",
            "what is",
            "meaning",
            "describe",
            "understand",
            "how does",
            "how do"
        ]):
            return Task.EXPLAIN

        # ----------------------------
        # Analyze
        # ----------------------------
        if any(keyword in q for keyword in [
            "analyze",
            "analyse",
            "analysis",
            "evaluate",
            "assess"
        ]):
            return Task.ANALYZE

        # ----------------------------
        # Compare
        # ----------------------------
        if any(keyword in q for keyword in [
            "compare",
            "difference",
            "vs",
            "versus",
            "better than"
        ]):
            return Task.COMPARE

        # ----------------------------
        # Extract
        # ----------------------------
        if any(keyword in q for keyword in [
            "extract",
            "list",
            "show all",
            "pull out",
            "give all"
        ]):
            return Task.EXTRACT

        # ----------------------------
        # Find
        # ----------------------------
        if any(keyword in q for keyword in [
            "find",
            "search",
            "locate",
            "where"
        ]):
            return Task.FIND

        # ----------------------------
        # Generate
        # ----------------------------
        if any(keyword in q for keyword in [
            "generate",
            "create",
            "write",
            "draft",
            "prepare"
        ]):
            return Task.GENERATE

        # ----------------------------
        # Recommend
        # ----------------------------
        if any(keyword in q for keyword in [
            "recommend",
            "suggest",
            "jobs",
            "career",
            "role",
            "roles",
            "companies",
            "next step",
            "best fit"
        ]):
            return Task.RECOMMEND

        # ----------------------------
        # Review
        # ----------------------------
        if any(keyword in q for keyword in [
            "review",
            "feedback",
            "improvement",
            "improve this document"
        ]):
            return Task.REVIEW

        # ----------------------------
        # Rewrite
        # ----------------------------
        if any(keyword in q for keyword in [
            "rewrite",
            "rephrase",
            "improve writing"
        ]):
            return Task.REWRITE

        # ----------------------------
        # Translate
        # ----------------------------
        if "translate" in q:
            return Task.TRANSLATE

        # ----------------------------
        # Classify
        # ----------------------------
        if any(keyword in q for keyword in [
            "classify",
            "categorize",
            "category"
        ]):
            return Task.CLASSIFY

        # ----------------------------
        # Default
        # ----------------------------
        return Task.CHAT