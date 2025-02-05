from groq import Groq
from flask import Flask, request
import json
import os
from dotenv import load_dotenv  # Import library dotenv

# Muat environment variables dari file .env
load_dotenv()

app = Flask(__name__)

# Baca environment variable untuk mode debug dan API key
DEBUG_MODE = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
GROQ_API_KEY = os.getenv('GROQ_API_KEY')  # Ambil API key dari environment variable

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY tidak ditemukan. Pastikan Anda telah menetapkan nilai ini di file .env.")

client = Groq(
    api_key=GROQ_API_KEY  # Gunakan API key dari environment variable
)

AVAILABLE_MODELS = {
    "deepseek-r1": "deepseek-r1-distill-llama-70b",
    "llama": "llama-3.2-1b-preview",
    "mixtral": "mixtral-8x7b-32768",
    "gemma2": "gemma2-9b-it",
    "llama70b": "llama-3.3-70b-versatile"
}

def ai_call(message, model_name):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{
                "role": "user",
                "content": message
            }],
            model=model_name,
            stream=False
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return str(e)

@app.route("/")
def main():
    if 'msg' not in request.args:
        return app.response_class(
            response='{"error":"Parameter \'msg\' tidak ditemukan"}',
            status=400,
            mimetype='application/json'
        )
    
    message = request.args.get('msg')
    if not message:
        return app.response_class(
            response='{"error":"Parameter \'msg\' tidak boleh kosong"}',
            status=400,
            mimetype='application/json'
        )
    model_key = request.args.get('model', 'llama')
    if model_key not in AVAILABLE_MODELS:
        return app.response_class(
            response='{"error":"Model tidak valid"}',
            status=400,
            mimetype='application/json'
        )
    
    model_name = AVAILABLE_MODELS[model_key]
    ai_response = ai_call(message, model_name)
    
    # Membuat dictionary terlebih dahulu
    response_dict = {
        "developer": "Muhammad Gagah",
        "model": model_key,
        "message": ai_response
    }
    
    # Menggunakan json.dumps untuk menghasilkan JSON yang benar dengan escape characters
    response = json.dumps(response_dict, ensure_ascii=False)
    
    return app.response_class(
        response=response,
        status=200,
        mimetype='application/json'
    )

@app.errorhandler(404)
def not_found(e):
    return app.response_class(
        response='{"error":"tidak diizinkan"}',
        status=404,
        mimetype='application/json'
    )

if __name__ == "__main__":
    # Gunakan DEBUG_MODE dari environment variable
    app.run(host="0.0.0.0", port=8080, debug=DEBUG_MODE)