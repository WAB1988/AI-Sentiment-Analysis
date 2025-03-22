from flask import Flask, render_template, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from groq import Groq
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

def scrape_comments(url):
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.imdb.com/title/tt0050083/reviews/?ref_=tt_ururv_sm")
        comments = driver.find_elements(By.CLASS_NAME, "ipc-html-content-inner-div")
        return [comment.text for comment in comments if comment.text.strip()]
    finally:
        driver.quit()

def analyze_sentiment(text, query):
    client = Groq(api_key=os.getenv('GROQ_API_KEY'))
    
    system_prompt = f"""You are a sentiment analysis expert. Analyze the following text based on this specific requirement: {query}
    
    Text to analyze: {text}
    
    Provide a clear and concise analysis."""

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_prompt
            }
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.5,
        max_completion_tokens=1024,
    )
    
    return chat_completion.choices[0].message.content

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    url = data.get('url')
    query = data.get('query')
    
    try:
        comments = scrape_comments(url)
        combined_comments = "\n".join(comments)
        analysis = analyze_sentiment(combined_comments, query)
        return jsonify({'success': True, 'analysis': analysis})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
