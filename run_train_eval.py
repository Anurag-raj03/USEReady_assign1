# import pandas as pd
# from src.batch.batch_predict import generate_predictions
# from src.evaluation.recall import calculate_recall
# generate_predictions(
#     "data/train.csv",
#     "data/train",
#     "train_predictions.csv"
# )
# true_subset = pd.read_csv("data/train.csv").head(2)
# true_subset.to_csv("data/train_subset.csv", index=False)

# scores = calculate_recall(
#     "data/train_subset.csv",
#     "train_predictions.csv"
# )
# print(f"Train Recall: {scores}")
from src.batch.batch_predict import generate_predictions
from src.evaluation.recall import calculate_recall

generate_predictions(
    "data/train_subset.csv",
    "data/train",
    "train_predictions.csv"
)

scores = calculate_recall(
    "data/train_subset.csv",
    "train_predictions.csv"
)

print(f"Train Recall: {scores}")