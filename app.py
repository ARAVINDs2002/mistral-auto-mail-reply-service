from flask import Flask, render_template, request
import requests

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"


# -------- Email Preprocessing --------
def preprocess_email(text):
    """
    Clean and limit email size to avoid exceeding model context.
    """

    if not text:
        return ""

    text = text.strip()

    # Remove common email separators
    separators = [
        "-----Original Message-----",
        "From:",
        "Sent from my iPhone"
    ]

    for sep in separators:
        if sep in text:
            text = text.split(sep)[0]

    MAX_LENGTH = 3000

    if len(text) > MAX_LENGTH:
        text = text[:MAX_LENGTH]

    return text


# -------- Generate Reply --------
def generate_reply(email_body, instruction):

    prompt = f"""
You are a professional email assistant.

Your task is to write a clear, polite, and professional reply.

Email received:
{email_body}

Instruction:
{instruction}

Write only the reply email.
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        data = response.json()
        return data.get("response", "").strip()

    except requests.exceptions.RequestException:
        return "Error: Unable to connect to the AI model."


# -------- Flask Route --------
@app.route("/", methods=["GET", "POST"])
def index():

    reply = ""

    if request.method == "POST":

        email_body = request.form.get("email_body", "")
        instruction = request.form.get("instruction", "")

        email_body = preprocess_email(email_body)

        if email_body:
            reply = generate_reply(email_body, instruction)
        else:
            reply = "Please enter an email body."

    return render_template("index.html", reply=reply)


# -------- Run Server --------
if __name__ == "__main__":
    app.run(debug=True)