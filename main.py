import os
from openai import OpenAI
from dotenv import load_dotenv
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
@app.route('/chat', methods=['POST'])
def chat_endpoint():
    user_req = request.get_json()
    user_message = user_req.get("message")
    if not user_message:
        return "No message provided", 400
    response = chat(user_message, None)
    return jsonify({"reply": response})

@app.route('/')
def home():
    return render_template('chat.html')

load_dotenv("./.env")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

context = """Act as a professional 5-star chef, but adapted for hostel students. Give short, practical, and easy-to-follow cooking tips, recipes, or meal ideas using minimal ingredients and equipment. Responses should be clear, simple, and directly usable, no fluff, but still feel professional."""

def chat(message, _):
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL"),
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    app.run(debug=True)