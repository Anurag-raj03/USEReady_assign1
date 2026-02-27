import pandas as pd
from src.evaluation.normalizer import normalize_text, normalize_date

DATE_COLUMNS = ["Aggrement Start Date", "Aggrement End Date"]

def calculate_recall(true_csv, pred_csv):
    true_df = pd.read_csv(true_csv)
    pred_df = pd.read_csv(pred_csv)
    merged = pd.merge(true_df, pred_df, on="File Name", suffixes=("_true", "_pred"))
    print("Merged rows:", len(merged))
    print("Merged File Names:", merged["File Name"].tolist())
    recall_scores = {}
    for col in true_df.columns:
        if col == "File Name":
            continue
        correct = 0
        for _, row in merged.iterrows():
            true_val = row[f"{col}_true"]
            pred_val = row[f"{col}_pred"]
            if col in DATE_COLUMNS:
                true_val = normalize_date(true_val)
                pred_val = normalize_date(pred_val)
            else:
                true_val = normalize_text(true_val)
                pred_val = normalize_text(pred_val)
            if true_val == pred_val:
                correct += 1
        recall_scores[col] = correct / len(merged) if len(merged) > 0 else 0
    return recall_scores