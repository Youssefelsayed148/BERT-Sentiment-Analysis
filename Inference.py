import torch
from transformers import BertTokenizerFast, BertForSequenceClassification

# Map numeric labels to sentiment strings
LABELS = {0: "Negative", 1: "Neutral", 2: "Positive"}

# Load tokenizer and model from the saved folder
MODEL_FOLDER = "./model"  # path to your saved model folder
tokenizer = BertTokenizerFast.from_pretrained(MODEL_FOLDER)
model = BertForSequenceClassification.from_pretrained(MODEL_FOLDER)
model.eval()

def predict_sentiment(text: str) -> str:
    """
    Predicts the sentiment of a single text input.
    """
    # Tokenize the input text
    inputs = tokenizer(
        text, 
        return_tensors="pt", 
        padding=True, 
        truncation=True, 
        max_length=128
    )
    
    # Forward pass without gradient calculation
    with torch.no_grad():
        outputs = model(**inputs)
        predicted_class_id = outputs.logits.argmax(dim=1).item()
    
    return LABELS[predicted_class_id]

# Example usage
if __name__ == "__main__":
    sample_text = "Stocks surged after the positive earnings report."
    sentiment = predict_sentiment(sample_text)
    print(f"Text: {sample_text}")
    print(f"Predicted Sentiment: {sentiment}")
