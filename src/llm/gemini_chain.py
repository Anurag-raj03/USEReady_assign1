from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from src.config.settings import GOOGLE_API_KEY, MODEL_NAME
from src.llm.schema import RentalMetadata
from src.llm.fewshot_builder import build_fewshot_examples

def get_chain(use_fewshot=True):
    llm = ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        google_api_key=GOOGLE_API_KEY,
        temperature=0,
        top_p=0.1
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
You are a strict legal information extraction system.

Extract structured rental agreement metadata accurately and consistently.

========================
FIELD DEFINITIONS
========================

1. Agreement Value
- Extract ONLY the MONTHLY RENTAL AMOUNT.
- Look near phrases such as:
  "monthly rent", "rent per month", "rent shall be", "agreed rent".
- DO NOT extract:
  • security deposit
  • advance
  • maintenance
  • refundable amount
  • total yearly rent
- Return digits only.
- No commas.
- No currency symbols.

2. Agreement Start Date
- The date tenancy begins.
- Often mentioned as:
  "commencing from", "with effect from".
- Convert to DD.MM.YYYY format.
- Example correct format: 20.05.2007
- Do NOT return natural language dates.
- Do NOT return slashes or hyphen formats.

3. Agreement End Date
- The date tenancy expires.
- Often mentioned as:
  "ending on", "valid until", "for a period of".
- Convert to DD.MM.YYYY format.
- Example correct format: 20.05.2007
- Do NOT return natural language dates.
- Do NOT change invalid dates if clearly written.

4. Renewal Notice (Days)
- Number of days prior notice required before termination or expiry.
- Look for:
  "prior notice", "termination notice", "notice period".
- Ignore notice mentioned in other contexts.
- Return digits only.

5. Party One
- The LESSOR / OWNER / LANDLORD.
- Extract only the person name.
- Remove titles such as:
  Mr., Mrs., Ms., Dr., Prof.
- Remove relationship terms:
  S/O, D/O, W/O.
- Remove addresses.
- Keep name formatting clean.
  Example:
  "Mrs.Asha Ramesh & Mr.Ramesh.K.N."
  → "Asha Ramesh & Ramesh K.N"

6. Party Two
- The LESSEE / TENANT.
- Apply same cleaning rules as Party One.

========================
STRICT RULES
========================

1. Do NOT guess.
2. Do NOT infer missing values.
3. If a field is not clearly found, return null.
4. Return ONLY structured output.
5. No explanations.
6. No additional text.

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