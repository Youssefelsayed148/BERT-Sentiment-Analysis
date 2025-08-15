from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import gradio as gr
from Inference import predict_sentiment

app = FastAPI(title="BERT Sentiment Analysis API")

# Optional: simple FastAPI route
@app.get("/")
def read_root():
    return {"message": "Welcome to the BERT Sentiment Analysis API!"}

# Gradio interface
def gradio_predict(text):
    return predict_sentiment(text)

# Launch Gradio as a web app
gr_interface = gr.Interface(
    fn=gradio_predict,
    inputs="text",
    outputs="text",
    title="BERT Sentiment Analysis",
    description="Enter a sentence and get the predicted sentiment (Negative, Neutral, Positive)."
)

@app.on_event("startup")
def launch_gradio():
    # Launch Gradio in a non-blocking way
    gr_interface.launch(share=True, server_name="0.0.0.0", server_port=7860, inline=True)

