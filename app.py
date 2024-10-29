from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
import re
from ecommbot.retrieval_generation import generation
from ecommbot.ingest import ingestdata

app = Flask(__name__)

load_dotenv()

vstore = ingestdata("done")
chain = generation(vstore)

def format_bold_and_list_text(text):
    # Convert **text** to <strong>text</strong> for HTML bold formatting
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Convert lines starting with '* ' into HTML list items
    text = re.sub(r'\* (.*?)\n', r'<li>\1</li>', text)
    # Wrap the entire list with <ul> tags if any <li> tags are present
    if "<li>" in text:
        text = "<ul>" + text + "</ul>"
    # Replace remaining newlines with <br> for other line breaks
    return text.replace('\n', '<br>')

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    result = chain.invoke(input)

    # Format the result text to handle bold, lists, and line breaks
    result_html = format_bold_and_list_text(result)

    # Embed the formatted text in a styled HTML structure
    formatted_result = (
        "<div style='font-family: Arial, sans-serif; color: #333; line-height: 1.6;'>"
        "<p><strong>Response:</strong></p>"
        "<div style='padding: 10px; border: 1px solid #ddd; background-color: #f9f9f9; border-radius: 8px;'>"
        f"{result_html}"
        "</div>"
        "</div>"
    )

    print("Response:", formatted_result)
    return formatted_result

if __name__ == '__main__':
    app.run(host="0.0.0.0")