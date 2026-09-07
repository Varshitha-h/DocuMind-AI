TASK_PROMPTS = {

    "summarize": """
Summarize the document clearly.

Focus on:
- Main ideas
- Key findings
- Important conclusions

Avoid unnecessary details.
""",

    "explain": """
Explain the requested topic in a simple and understandable way.

Use examples whenever useful.

Avoid overly technical language unless the document requires it.
""",

    "analyze": """
Analyze the document carefully.

Identify:
- Important observations
- Strengths
- Weaknesses
- Risks
- Insights

Provide objective analysis.
""",

    "compare": """
Compare the requested items.

Highlight:
- Similarities
- Differences
- Advantages
- Disadvantages

Present the comparison clearly.
""",

    "extract": """
Extract only the requested information.

Do not summarize.

Return exactly what the user requested whenever possible.
""",

    "find": """
Search the document for the requested information.

If found,
provide the answer with enough surrounding context.

If not found,
clearly state that the information does not exist in the document.
""",

    "answer": """
Answer the user's question directly.

Use the uploaded document whenever possible.

If the answer is unavailable in the document,
say so before using general knowledge.
""",

    "generate": """
Generate the requested content using the document as the primary source.

Keep the generated content professional,
accurate and relevant.
""",

    "recommend": """
Provide recommendations based primarily on the uploaded document.

Do not invent recommendations that contradict the document.

Explain why each recommendation is suitable.
""",

    "review": """
Review the document carefully.

Identify:
- mistakes
- improvements
- missing information
- inconsistencies

Provide constructive feedback.
""",

    "rewrite": """
Rewrite the requested content.

Improve:
- grammar
- clarity
- readability
- professionalism

Do not change the original meaning.
""",

    "translate": """
Translate the requested text accurately.

Preserve meaning,
formatting,
and technical terminology.
""",

    "classify": """
Classify the requested content into the most appropriate category.

Explain briefly why it belongs there.
""",

    "chat": """
Answer naturally.

Maintain conversation context.

Use the uploaded document whenever it is relevant.
"""
}