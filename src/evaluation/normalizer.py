import pandas as pd
from datetime import datetime
import re

def normalize_text(value):
    if pd.isna(value):
        return ""
    value = str(value).strip().lower()
    value = value.replace(",", "")
    if re.fullmatch(r"\d+\.0+", value):
        value = str(int(float(value)))
    value = re.sub(r"\b(mr|mrs|ms|dr)\.?\b", "", value)
    value = re.sub(r"[^\w\s]", "", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()

def normalize_date(value):
    if pd.isna(value) or value == "":
        return ""
    value = str(value).strip()
    value = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', value)
    for fmt in ("%d.%m.%Y", "%d/%m/%Y", "%d-%m-%Y"):
        try:
            return datetime.strptime(value, fmt).strftime("%d.%m.%Y")
        except:
            continue
    try:
        return datetime.strptime(value, "%d day of %B, %Y").strftime("%d.%m.%Y")
    except:
        pass

    try:
        return datetime.strptime(value, "%d %B %Y").strftime("%d.%m.%Y")
    except:
        pass

    return value