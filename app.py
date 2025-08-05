from flask import Flask, render_template, request, jsonify
import os
from openai import OpenAI
from dotenv import load_dotenv
import pathlib

# Load environment variables
current_dir = pathlib.Path(__file__).parent.absolute()
env_path = current_dir / '.env'
load_dotenv(dotenv_path=env_path)

api_key = os.environ.get("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError(
        "OPENROUTER_API_KEY not found. Please ensure it is set in your .env file."
    )

# Initialize OpenAI client with OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    default_headers={"HTTP-Referer": "http://localhost:5000"}
)

app = Flask(__name__)

def get_openai_response(messages, model="anthropic/claude-3.5-sonnet", temperature=0.7):
    """
    Sends the conversation history to the OpenRouter API and returns the model's response.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred while getting a response from OpenRouter: {e}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_profile = data.get('userProfile', {})
        user_message = data.get('message', '')
        
        # Create system message for career guidance
        system_message = """You are a helpful and encouraging career guidance assistant. 
        The user has provided their interests, skills, and favorite subjects. 
        Provide tailored career suggestions and explain why they might be a good fit, 
        based on the information provided. Keep responses concise, friendly, and focused on career advice.
        Be encouraging and provide actionable next steps when possible."""
        
        # Create user message with profile context
        if user_profile:
            profile_summary = f"""
            User Profile:
            - Interests: {user_profile.get('interests', 'Not specified')}
            - Skills: {user_profile.get('skills', 'Not specified')}
            - Favorite Subjects: {user_profile.get('favorite_subjects', 'Not specified')}
            """
            
            if user_message:
                full_user_message = f"Here is my profile: {profile_summary}\n\nUser question: {user_message}"
            else:
                full_user_message = f"Here is my profile: {profile_summary}. Can you suggest some career paths that might be a good fit for me?"
        else:
            full_user_message = user_message if user_message else "Hello! I'm looking for career guidance."
        
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": full_user_message}
        ]
        
        # Get AI response from OpenRouter
        ai_response = get_openai_response(messages)
        
        return jsonify({
            'success': True,
            'response': ai_response
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/generate-suggestions', methods=['POST'])
def generate_suggestions():
    try:
        data = request.get_json()
        user_profile = data.get('userProfile', {})
        
        if not user_profile:
            return jsonify({
                'success': False,
                'error': 'User profile is required'
            }), 400
        
        # Create system message for career suggestions
        system_message = """You are a career guidance expert. Based on the user's interests, skills, and favorite subjects, 
        provide 3-5 specific career suggestions. For each career, briefly explain why it's a good fit and mention any 
        relevant skills or education paths. Be encouraging and practical."""
        
        profile_summary = f"""
        User Profile:
        - Interests: {user_profile.get('interests', 'Not specified')}
        - Skills: {user_profile.get('skills', 'Not specified')}
        - Favorite Subjects: {user_profile.get('favorite_subjects', 'Not specified')}
        """
        
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": f"Based on this profile: {profile_summary}, suggest 3-5 specific career paths that would be a good fit. For each career, explain why it matches their profile and mention any relevant skills or education paths."}
        ]
        
        # Get AI response from OpenRouter
        ai_response = get_openai_response(messages)
        
        return jsonify({
            'success': True,
            'response': ai_response
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    print("🚀 Starting Career Guidance Chatbot Server...")
    print("📱 Open your browser and go to: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000) 