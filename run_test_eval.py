import pandas as pd
from src.batch.batch_predict import generate_predictions
from src.evaluation.recall import calculate_recall
generate_predictions("data/test.csv","data/test","test_predictions.csv")
scores = calculate_recall("data/test.csv","test_predictions.csv")
print(f"Test Recall: {scores}")
metrics_df = pd.DataFrame(
    list(scores.items()),
    columns=["Metric", "Recall"]
)
metrics_df.to_csv("test_metrics.csv", index=False)
print("Test metrics saved to test_metrics.csv")