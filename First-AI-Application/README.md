
````markdown
## 🚀 Setup Instructions

### 1. Copy the example environment file
In your project folder, run:
```bash
cp .env.example .env
````

*(On Windows PowerShell, use: `copy .env.example .env`)*

---

### 2. Get your Google Generative AI API key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **Create API Key**
4. Copy the generated key

---

### 3. Add your API key to `.env`

Open `.env` in any text editor and replace `your_api_key_here` with your actual key:

```
GEMINI_API_KEY=your_actual_key_here
```

---

### 4. Install dependencies

Run the following command:

```bash
pip install google-genai python-dotenv
```

---

### 5. Run the script

```bash
python NutritionAI.py
```

```

This version is clean, GitHub-friendly, and copy-paste ready.  

Do you also want me to make the **`.env.example`** file to go along with it so users can just copy and edit? That would make your repo even more user-friendly.
```
