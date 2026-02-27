import pandas as pd
import os
from src.ingestion.docx_loader import load_docx
from src.preprocessing.text_cleaner import clean_text

def build_fewshot_examples(train_csv_path, train_folder, limit=1):
    df = pd.read_csv(train_csv_path)
    examples = []
    for i in range(min(limit, len(df))):
        row = df.iloc[i]
        file_base = row["File Name"]
        for file in os.listdir(train_folder):
            if file.startswith(file_base):
                file_path = os.path.join(train_folder, file)
                break
        else:
            continue
        if file_path.endswith(".docx"):
            text = load_docx(file_path)
        else:
            continue 
        text = clean_text(text)
        text = text[:1000]
        example_text = f"""
Example {i+1}:
Document:
{text}
Expected Output:
agreement_value: {row['Aggrement Value']}
agreement_start_date: {row['Aggrement Start Date']}
agreement_end_date: {row['Aggrement End Date']}
renewal_notice_days: {row['Renewal Notice (Days)']}
party_one: {row['Party One']}
party_two: {row['Party Two']}
"""
        examples.append(example_text)

    return "\n".join(examples)