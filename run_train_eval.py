import pandas as pd
from src.batch.batch_predict import generate_predictions
from src.evaluation.recall import calculate_recall
generate_predictions("data/train.csv","data/train","train_predictions.csv")
scores = calculate_recall("data/train.csv","train_predictions.csv")
print(f"Train Recall: {scores}")
metrics_df = pd.DataFrame(list(scores.items()),columns=["Field", "Recall"])
average_recall = sum(scores.values()) / len(scores)
metrics_df.loc[len(metrics_df)] = ["Average Recall", average_recall]
metrics_df.to_csv("train_metrics.csv", index=False)
print("Metrics saved to train_metrics.csv")