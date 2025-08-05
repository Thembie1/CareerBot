🎓 Career Guidance Chatbot
An AI-powered career guidance assistant that uses the OpenRouter API to provide personalized career advice through both a web interface and command-line chatbot.

✨ Features
🧠 AI chatbot for interactive career guidance (Web + CLI)

🎯 Personalized suggestions based on:
Interests
Skills
Favorite subjects

🤖 Powered by OpenRouter’s Claude 3.5 Sonnet model

💬 Beautiful real-time chat interface (Flask web app)

🔁 Handles follow-up questions for deeper career exploration

⚙️ Setup
1. Install Dependencies

2. Get an OpenRouter API Key
Go to https://openrouter.ai
Sign up or log in
Navigate to your account and generate an API key


3. Configure the API Key
Option A: Use the setup script (Recommended)
python setup.py
Option B: Manual Setup
Edit the config.env file and replace:
env
OPENROUTER_API_KEY=your_openrouter_api_key_here

🚀 Usage
Web Interface (Recommended)
Run the web server:
python app.py
Then open your browser and go to:
👉 http://localhost:5000

Command-Line Interface (CLI)
Run the chatbot in your terminal:
python app.py


💡 How It Works
Both interfaces will:

Ask about your interests (e.g., Art, Technology, Cybersecurity, etc.)
Ask about your skills (e.g., Coding, Drawing, Problem Solving, etc.)
Ask about your favorite subjects (e.g., Math, Computer Science, History, etc.)
Use your responses to generate tailored career suggestions
Allow you to ask follow-up questions about any career path

⚙️ Configuration
Key Component	Value
API Provider	OpenRouter
AI Model	anthropic/claude-3.5-sonnet
Config File	.env


🛠 Troubleshooting
"OPENROUTER_API_KEY not found"
Make sure your API key is set correctly in .env.

401 Unauthorized or API errors

Ensure your key is valid on OpenRouter

Check your account limits

