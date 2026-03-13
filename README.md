# Email Reply Generator

A locally hosted web application built with Flask that generates professional email replies using the **Mistral** AI model via **Ollama**. This tool helps you quickly draft clear, polite, and professional email responses based on the received email and a specific instruction.

## Features
- **Local AI Processing**: Uses Ollama to run the Mistral model locally, ensuring privacy and avoiding API costs.
- **Easy-to-use Interface**: A simple web form to paste the original email and provide instructions for the reply.
- **Email Preprocessing**: Automatically removes common email separators and limits text length to optimize the prompt for the AI model.

## Prerequisites

1. **Python 3.x**
2. **Ollama**: You need to have [Ollama](https://ollama.com/) installed on your machine to run the Mistral model locally.

## Setup Instructions

### 1. Set up Ollama and the Mistral Model

First, make sure the Mistral model is downloaded and ready in Ollama. Open your terminal or command prompt and run:

```bash
# Optional: If you don't have a dedicated GPU, you can set this environment variable
# set OLLAMA_NO_GPU=1  (Windows cmd) or $env:OLLAMA_NO_GPU="1" (PowerShell)

# Download the mistral model
ollama pull mistral

# (Optional) Test running the model in your terminal
ollama run mistral
```

Make sure the Ollama API server is running (usually it starts automatically on `http://localhost:11434` when you run Ollama).

### 2. Set up the Python Environment

Navigate to the project directory and create a virtual environment (recommended):

```bash
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment
# On Windows:
myenv\Scripts\activate
# On macOS/Linux:
# source myenv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Start the Flask server:

```bash
python app.py
```

The application will be accessible at `http://localhost:5000/`.

## Usage

1. Open your web browser and go to `http://localhost:5000/`.
2. Paste the email you received in the first text box.
3. Provide an instruction for the reply in the second text box (e.g., "Decline the request politely" or "Accept the meeting for next Tuesday").
4. Click the generate button to create your professional email reply.
