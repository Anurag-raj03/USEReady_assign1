from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from src.config.settings import GOOGLE_API_KEY, MODEL_NAME
from src.llm.schema import RentalMetadata
from src.llm.fewshot_builder import build_fewshot_examples

def get_chain(use_fewshot=True):
    llm = ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        google_api_key=GOOGLE_API_KEY,
        temperature=0
    )
    structured_llm = llm.with_structured_output(RentalMetadata)
    fewshot_text = ""
    if use_fewshot:
        fewshot_text = build_fewshot_examples(
            "data/train.csv",
            "data/train",
            limit=1
        )

    system_prompt = f"""
You are a precise rental agreement information extraction system.

Your task is to extract structured metadata from the document.

STRICT RULES (follow carefully):

1. Extract only the minimal core value for each field.
2. Do NOT rewrite dates into natural language.
3. Do NOT correct invalid dates.
4. Do NOT interpret or infer missing values.
5. Do NOT add titles (Mr., Mrs., Dr., etc).
6. Do NOT include addresses, S/O, W/O, D/O, or relationship details.
7. Agreement Value must contain digits only (no commas, no currency symbols).
8. Renewal Notice is usually mentioned near expiry clause or termination clause. Look carefully for notice period in days. Renewal Notice must contain digits only.
9. Dates must be returned exactly as written in the document.
10. If a field is not found, return null.
11. Return only structured output — no explanation.

Renewal Notice refers to the number of days prior notice required before termination or expiry. 
Search the entire document carefully for phrases containing "notice", "prior notice", "before expiry", or "termination".

{fewshot_text}
"""

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            (
                "human",
                "Extract the required rental metadata from the following document:\n\n{document}"
            ),
        ]
    )

    return prompt | structured_llm