import pandas as pd
from datetime import datetime
import re

def normalize_text(value):
    if pd.isna(value):
        return ""
    value = str(value).strip().lower()
    value = value.replace(",", "")
    if re.match(r"^\d+\.0$", value):
        value = value[:-2]
    if re.match(r"^\d+\.00$", value):
        value = value[:-3]
    value = re.sub(r"\s+", " ", value)
    return value.strip()
def normalize_date(value):
    if pd.isna(value) or value == "":
        return ""
    value = str(value).strip()
    for fmt in ("%d.%m.%Y", "%d/%m/%Y", "%d-%m-%Y"):
        try:
            return datetime.strptime(value, fmt).strftime("%d.%m.%Y")
        except:
            continue
    try:
        cleaned = re.sub(r"(st|nd|rd|th)", "", value.lower())
        return datetime.strptime(cleaned, "%d day of %B %Y").strftime("%d.%m.%Y")
    except:
        pass
    try:
        cleaned = re.sub(r"(st|nd|rd|th)", "", value.lower())
        return datetime.strptime(cleaned, "%d %B %Y").strftime("%d.%m.%Y")
    except:
        pass
    return value.lower()