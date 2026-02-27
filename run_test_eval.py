from src.batch.batch_predict import generate_predictions
from src.evaluation.recall import calculate_recall
generate_predictions("data/test.csv","data/test","test_predictions.csv")
scores=calculate_recall("data/test.csv","test_predicitons.csv")
print(f"Test Recall: {scores}")
