from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

conversation = [
    {"role": "user", "parts": [{"text": "You are a friendly nutritionist coach. Don't comment on the chat history, just read it and keep it in mind and respond based on it. This is how your conversation with the user has went so far:"}]}
]

while True:
    user_prompt = input("User (Press X to quit): ")
    if user_prompt == 'X':
        break
    
    conversation.append({"role": "user", "parts": [{"text": user_prompt}]})
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = conversation,
    )

    conversation.append({"role": "model", "parts": [{"text": response.text}]})
    print(f"Gemini: {response.text}")