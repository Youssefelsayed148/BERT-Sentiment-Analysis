📌 BERT-Sentiment-Analysis
This project implements a BERT-based Sentiment Analysis model deployed as a Dockerized API with a Gradio web interface. It allows users to input text and instantly receive a sentiment prediction (Positive / Negative / Neutral).

📖Key features:-

-BERT Transformer Model for high-accuracy NLP.
-Class imbalance handling during training using class_weight.
-Gradio Interface for interactive predictions.
-Docker Deployment for easy sharing and portability.

🛠️ Approach:-

Data Preprocessing:
-Tokenized text using Hugging Face’s BertTokenizer.
-Lowercasing, cleaning, and truncating to max_length=128.
Handling Class Imbalance:
-Calculated the distribution of classes.
-Applied class weights in the loss function during training.

Model Training:
Base model: bert-base-uncased 
Optimizer: AdamW
Loss: Weighted Cross Entropy (with class weights).
Metrics: Accuracy, F1-score.

Deployment:
-Built main.py (FastAPI + Gradio) for the backend and UI.
-Created a Dockerfile to package the app, model, and dependencies.
-Exposed port 7860 for the Gradio interface.

📊 Evaluation:-

The model achieved 82% accuracy on the test set.

Class	Precision	Recall	F1-score
  0	    0.75	   0.87     0.80
  1	    0.90	   0.83     0.86
  2   	0.72	   0.80     0.76

Weighted Avg F1: 0.83

🔧 Model Optimization Ideas:-

-Increase training epochs to allow the model more learning time.
-Adjust learning rate (try smaller values for fine-tuning stability).
-Experiment with different optimizers.
-Handle class imbalance using oversampling.
-Use more training data or augment text data with paraphrasing techniques.
-Experiment with different pre-trained BERT variants (e.g., DistilBERT for speed, RoBERTa for accuracy).
