import pandas as pd
from src.pipeline.extractor_pipeline import run_extraction
from src.utils.file_matcher import find_file
def generate_predictions(csv_path, folder_path, output_csv):
    df = pd.read_csv(csv_path)
    predictions = []
    print("Files being processed:")
    print(df["File Name"].tolist())
    for _, row in df.iterrows():
        file_base = row["File Name"]
        file_path = find_file(folder_path, file_base)
        if file_path is None:
            print(f"File not found for: {file_base}")
            formatted_result = {
                "File Name": file_base,
                "Aggrement Value": None,
                "Aggrement Start Date": None,
                "Aggrement End Date": None,
                "Renewal Notice (Days)": None,
                "Party One": None,
                "Party Two": None,
            }
            predictions.append(formatted_result)
            continue
        result = run_extraction(file_path)
        formatted_result = {
            "File Name": file_base,
            "Aggrement Value": result.get("agreement_value"),
            "Aggrement Start Date": result.get("agreement_start_date"),
            "Aggrement End Date": result.get("agreement_end_date"),
            "Renewal Notice (Days)": result.get("renewal_notice_days"),
            "Party One": result.get("party_one"),
            "Party Two": result.get("party_two"),
        }
        predictions.append(formatted_result)
    pd.DataFrame(predictions).to_csv(output_csv, index=False)