import re
def clean_text(text:str)->str:
    text=re.sub(r"\s+"," ",text)
    text=text.replace("\n"," ")
    text=re.sub(r"[^\x00-\x7F]+"," ",text)
    return text.strip()
