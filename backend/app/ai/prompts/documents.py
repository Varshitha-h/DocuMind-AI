DOCUMENT_PROMPTS = {

    "resume": """
The uploaded document is a resume.

When answering:
- Focus on the candidate's skills, experience, education, certifications, and projects.
- Recommend suitable job roles only if asked.
- Highlight strengths and possible improvements when requested.
- Do not invent experience that is not present in the resume.
""",

    "research": """
The uploaded document is a research paper.

When answering:
- Focus on the research objective, methodology, results, and conclusions.
- Explain technical concepts clearly.
- Keep scientific terminology accurate.
""",

    "invoice": """
The uploaded document is an invoice.

When answering:
- Focus on invoice number, customer details, vendor details, dates, GST/tax, totals, and payment information.
- Return exact values whenever possible.
- Do not estimate financial values.
""",

    "contract": """
The uploaded document is a contract.

When answering:
- Focus on obligations, parties involved, important clauses, dates, confidentiality, payment terms, termination conditions, and responsibilities.
- Avoid interpreting legal meaning beyond what is written.
""",

    "medical": """
The uploaded document is a medical report.

When answering:
- Explain medical terms in simple language.
- Mention abnormal values if requested.
- Do not provide a medical diagnosis unless it is explicitly present in the document.
""",

    "financial": """
The uploaded document is a financial report.

When answering:
- Focus on revenue, expenses, profit/loss, assets, liabilities, and financial trends.
- Present numbers accurately.
- Do not fabricate financial analysis.
""",

    "presentation": """
The uploaded document is a presentation.

When answering:
- Focus on the key topics discussed.
- Summarize slides naturally.
- Avoid repeating slide titles unnecessarily.
""",

    "meeting_notes": """
The uploaded document contains meeting notes.

When answering:
- Focus on attendees, decisions, action items, deadlines, and discussion points.
- Present action items clearly when requested.
""",

    "code": """
The uploaded document contains source code.

When answering:
- Explain the code accurately.
- Describe functions, classes, variables, and logic.
- Suggest improvements only if requested.
- Never invent code that does not exist.
""",

    "general": """
The uploaded document is a general document.

Answer naturally using the document context.
Only use general knowledge if the document does not contain the requested information.
"""
}