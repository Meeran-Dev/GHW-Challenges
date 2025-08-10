# Setup Instructions

1. Copy the example environment file

In your project folder, run:
cp .env.example .env

2. Get your Google Generative AI API key

Go to: Google AI Studio
Sign in with your Google account
Click Create API Key

3. Add your API key to .env

Open .env in any text editor and replace your_api_key_here with your actual key:

GEMINI_API_KEY = Your_api_key_here

4. Install dependencies

google-genai
dotenv

5. Run the script

python NutritionAI.py