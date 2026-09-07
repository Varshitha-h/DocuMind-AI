from enum import Enum


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


class DocumentDetector:
    """
    Detects the uploaded document type based on its content.
    """

    def detect(self, document_text: str) -> DocumentType:

        if not document_text:
            return DocumentType.GENERAL

        text = document_text.lower()

        # ----------------------------
        # Resume
        # ----------------------------
        if any(keyword in text for keyword in [
            "experience",
            "work experience",
            "education",
            "skills",
            "technical skills",
            "projects",
            "certifications",
            "internship",
            "employment"
        ]):
            return DocumentType.RESUME

        # ----------------------------
        # Research Paper
        # ----------------------------
        if any(keyword in text for keyword in [
            "abstract",
            "introduction",
            "methodology",
            "methods",
            "results",
            "discussion",
            "references",
            "conclusion"
        ]):
            return DocumentType.RESEARCH

        # ----------------------------
        # Invoice
        # ----------------------------
        if any(keyword in text for keyword in [
            "invoice",
            "invoice number",
            "tax invoice",
            "gst",
            "subtotal",
            "total amount",
            "amount due",
            "bill to"
        ]):
            return DocumentType.INVOICE

        # ----------------------------
        # Contract
        # ----------------------------
        if any(keyword in text for keyword in [
            "agreement",
            "terms and conditions",
            "party",
            "termination",
            "confidentiality",
            "obligations",
            "effective date"
        ]):
            return DocumentType.CONTRACT

        # ----------------------------
        # Medical Report
        # ----------------------------
        if any(keyword in text for keyword in [
            "patient",
            "diagnosis",
            "prescription",
            "doctor",
            "blood",
            "haemoglobin",
            "hemoglobin",
            "test result"
        ]):
            return DocumentType.MEDICAL

        # ----------------------------
        # Financial Report
        # ----------------------------
        if any(keyword in text for keyword in [
            "balance sheet",
            "profit",
            "loss",
            "cash flow",
            "assets",
            "liabilities",
            "revenue",
            "income statement"
        ]):
            return DocumentType.FINANCIAL

        # ----------------------------
        # Presentation
        # ----------------------------
        if any(keyword in text for keyword in [
            "agenda",
            "slide",
            "thank you",
            "presentation",
            "speaker notes"
        ]):
            return DocumentType.PRESENTATION

        # ----------------------------
        # Meeting Notes
        # ----------------------------
        if any(keyword in text for keyword in [
            "meeting",
            "minutes",
            "attendees",
            "action items",
            "discussion",
            "follow up"
        ]):
            return DocumentType.MEETING_NOTES

        # ----------------------------
        # Source Code
        # ----------------------------
        if any(keyword in text for keyword in [
            "import ",
            "from ",
            "class ",
            "def ",
            "function",
            "public class",
            "#include",
            "console.log",
            "return "
        ]):
            return DocumentType.CODE

        return DocumentType.GENERAL