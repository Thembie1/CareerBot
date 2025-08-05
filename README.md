# Career Guidance Chatbot

An AI-powered career guidance assistant that uses OpenRouter API to provide personalized career advice.

## Features

- Interactive career guidance chatbot (Web interface + Command line)
- Personalized career suggestions based on interests, skills, and favorite subjects
- Uses OpenRouter API with Claude 3.5 Sonnet model
- Beautiful web interface with real-time chat
- Follow-up questions and detailed career discussions

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get OpenRouter API Key

1. Go to [OpenRouter](https://openrouter.ai/keys)
2. Sign up or log in
3. Create a new API key
4. Copy the API key

### 3. Configure API Key

**Option A: Use the setup script (Recommended)**
```bash
python setup.py
```

**Option B: Manual configuration**
1. Edit `config.env` file
2. Replace `your_openrouter_api_key_here` with your actual API key

## Usage

### Web Interface (Recommended)
Run the web server:
```bash
python app.py
```

Then open your browser and go to: http://localhost:5000

### Command Line Interface
Run the chatbot in terminal:
```bash
python gemini.py
```

Both versions will:
1. Ask about your interests (Art, Technology, Cybersecurity, Data, Networking, Business)
2. Ask about your skills (Coding, Drawing, Database, Troubleshooting, Communication, Problem solving)
3. Ask about your favorite subjects (Math, Biology, Language, Computer Science, Statistics, Physics, Chemistry, History)
4. Provide personalized career suggestions using OpenRouter API
5. Allow follow-up questions about careers

## Configuration

The chatbot uses:
- **API**: OpenRouter (https://openrouter.ai/api/v1)
- **Model**: Claude 3.5 Sonnet (anthropic/claude-3.5-sonnet)
- **Configuration**: `config.env` file

## Files

- `app.py` - Flask web server (main application)
- `gemini.py` - Command line chatbot application
- `templates/index.html` - Web interface HTML template
- `setup.py` - Interactive setup script
- `config.env` - API configuration file
- `requirements.txt` - Python dependencies
- `README.md` - This documentation

## Troubleshooting

- **"OPENROUTER_API_KEY not found"**: Make sure you've set up your API key in `config.env`
- **API errors**: Check your OpenRouter account for API key validity and usage limits
- **Import errors**: Install required packages with `pip install -r requirements.txt` 