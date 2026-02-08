🌍 AI Travel Planner - Smart Itinerary Generator
An intelligent travel planning application that leverages Google Gemini AI to create personalized, budget-friendly, and detailed travel itineraries based on user preferences.

🚀 Features
🤖 AI-Driven Planning: Generates realistic itineraries using the Gemini 3 (Flash) model based on city, duration, and budget.

🌓 Modern UI & Dark Mode: Sleek design built with Tailwind CSS, featuring full dark mode support based on system or user preference.

💾 Persistent History: Saves previous trips using LocalStorage so you can revisit your plans anytime without re-generating.

📋 Copy to Clipboard: Export your travel plan as a clean text format with a single click.

📍 Smart Maps: Each activity includes a direct link to Google Maps for easy navigation.

🛠️ Tech Stack
Backend: Python, FastAPI

AI Engine: Google Gemini API (google-genai)

Frontend: HTML5, Tailwind CSS, JavaScript (Fetch API)

Environment Management: Python-dotenv

📂 Project Structure
main.py: The core FastAPI application handling routes and server logic.

seyahat.py: AI logic that communicates with the Gemini API and parses JSON responses.

index.html: The main user interface and frontend logic.

.env: Secure storage for your API keys (excluded from version control).

.gitignore: Configured to prevent sensitive files and temporary folders from being uploaded.

📦 Getting Started
Clone the repository:

Bash
git clone https://github.com/berkaygayretli/AI-Seyahat-Planlayici.git
Install dependencies:

Bash
pip install -r requirements.txt
Setup Environment Variables: Create a .env file in the root directory and add your API key:

Plaintext
GEMINI_API_KEY=your_google_api_key_here
Run the application:

Bash
uvicorn main:app --reload
Open http://127.0.0.1:8000 in your browser.
