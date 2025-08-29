from flask import Flask, request, jsonify, render_template
from google.generativeai import GenerativeModel
import google.generativeai as genai
from flask_cors import CORS  
import markdown

app = Flask(__name__, static_url_path='/static')
CORS(app)

def gemini_to_html(text):
    return markdown.markdown(text, extensions=['extra'])

@app.route('/')
def home():
    return render_template("index.html")

# Configure Gemini API
genai.configure(api_key="AIzaSyDH92jtFhAVhn4HRoOpfrflEy_BtHJQ2D8")
model = GenerativeModel("gemini-2.5-flash")

@app.route('/generate', methods=['POST'])
def generate_pitch():
    data = request.json
    prompt = f"""
    Generate an elevator pitch, tagline, slide bullets, 
    value proposition, competitors and possible revenue models for this startup:
    Idea: {data['idea']}
    Problem: {data['problem']}
    Target Audience: {data['audience']}
    Features: {data['features']}
    """
    response = model.generate_content(prompt)
    res = gemini_to_html(response.text)
    return jsonify({"output": res})

if __name__ == '__main__':
    app.run(debug=True)
