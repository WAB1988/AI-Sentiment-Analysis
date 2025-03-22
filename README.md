# AI Sentiment Analysis Web Application

A web application that performs sentiment analysis on user-provided text using the Groq AI API. The application features a modern interface and can analyze sentiments from various sources, including IMDB reviews.

## Features

- Modern, responsive web interface
- Real-time sentiment analysis
- Support for analyzing text from URLs (e.g., IMDB reviews)
- Powered by Groq AI API
- Customizable analysis queries

## Prerequisites

- Python 3.8 or higher
- Chrome browser (for web scraping)
- Groq API key

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd AI_Sentiment_Analysis
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Unix or MacOS
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

## Project Structure

```
AI_Sentiment_Analysis/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables
├── static/            # Static files (CSS, JavaScript)
│   ├── style.css
│   └── script.js
└── templates/         # HTML templates
    └── index.html
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Enter a URL (e.g., IMDB reviews page) and your analysis query
4. Click "Analyze Sentiment" to get the results

## Technologies Used

- Flask (Python web framework)
- Selenium (Web scraping)
- Groq AI API (Sentiment analysis)
- Bootstrap (Frontend styling)
- JavaScript (Frontend functionality)

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Groq AI for providing the API
- Flask framework and its contributors
- Bootstrap for the UI components 