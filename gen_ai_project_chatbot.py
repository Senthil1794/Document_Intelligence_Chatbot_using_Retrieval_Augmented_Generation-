# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 12:14:29 2026

@author: Senthil
"""

from flask import Flask, request, jsonify, render_template
from gen_ai_project import get_llm

path = r'C:\Users\admin\Documents\GenAI\Session_35_GenAI\project'

chatbot = get_llm(path)

# Create Flask app
app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route("/")
def home():
    return render_template("index.html")

# Define a route for the prediction endpoint
@app.route('/get_answer', methods=["POST"])

def get_answer():
    question = request.form['question']
    answer = chatbot.invoke({'question':question, 'chat_history':[]})
    return(jsonify(answer))

# Run the app if executed directly
if __name__ == "__main__":
    app.run()