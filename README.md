# Physics Expert AI Chatbot

A specialized AI assistant built with **Django** and **Google Gemini AI** designed to solve complex physics problems using first principles.

## Features
- Provides step-by-step derivations.
- Formats math using LaTeX.
- Built-in "Physics Only" filter (refuses non-physics questions).

## Credits
This project was developed as part of a learning module based on the initial architecture by [Sir's Name/Link]. I have extended the logic to include custom system prompting and [mention any other change you made].

## Setup Instructions
1. Clone the repo: `git clone <repo-url>`
2. Install requirements: `pip install -r requirements.txt`
3. Add your `GOOGLE_API_KEY` to a `.env` file.
4. Run server: `python manage.py runserver`
