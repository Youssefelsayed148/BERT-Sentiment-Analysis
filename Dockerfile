FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy Python files
COPY main.py .
COPY Inference.py .
COPY requirements.txt .
# Copy model folder
COPY model ./model


# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports for FastAPI and Gradio
EXPOSE 8000 
EXPOSE 7860
# Command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]