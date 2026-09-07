from enum import Enum


class Intent(str, Enum):
    DOCUMENT = "document"
    GENERAL = "general"
    HYBRID = "hybrid"
    CONVERSATION = "conversation"


class DocumentType(str, Enum):
    RESUME = "resume"
    RESEARCH = "research"
    INVOICE = "invoice"
    CONTRACT = "contract"
    MEDICAL = "medical"
    FINANCIAL = "financial"
    PRESENTATION = "presentation"
    MEETING_NOTES = "meeting_notes"
    CODE = "code"
    GENERAL = "general"
    UNKNOWN = "unknown"


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