import os
import time
from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError
from src.ingestion.docx_loader import load_docx
from src.ingestion.image_loader import load_image
from src.preprocessing.text_cleaner import clean_text
from src.llm.gemini_chain import get_chain

CHAIN = get_chain()

def run_extraction(file_path: str):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".docx":
        text = load_docx(file_path)
    elif ext in [".png", ".jpg", ".jpeg"]:
        text = load_image(file_path)
    else:
        raise ValueError("Unsupported file type")
    text = clean_text(text)
    max_retries = 3
    for attempt in range(max_retries):
        try:
            result = CHAIN.invoke({"document": text})
            time.sleep(2)
            return result.dict()
        except ChatGoogleGenerativeAIError:
            print(f"Rate limit hit. Retry {attempt+1}/{max_retries} in 20 sec...")
            time.sleep(20)

        except Exception as e:
            print("Unexpected error:", e)
            break
    return {
        "agreement_value": None,
        "agreement_start_date": None,
        "agreement_end_date": None,
        "renewal_notice_days": None,
        "party_one": None,
        "party_two": None,
    }