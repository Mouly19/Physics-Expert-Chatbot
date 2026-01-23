# 🌌 Physics Expert AI Chatbot

A **professional full-stack AI-powered web application** designed to deliver **rigorous, first-principles explanations of physics concepts**.
The system is strictly **primed to behave like a physics professor**, refusing non-physics queries to maintain **academic integrity and domain focus**.

This project leverages **Google Gemini AI** with carefully engineered system prompts to emulate expert-level reasoning using the **Feynman Technique**.

---

## 🚀 Features

* **Expert Physics Persona**
  The AI responds only to physics-related queries and explains concepts from fundamental principles, similar to a university professor.

* **Feynman Technique-Based Explanations**
  Complex topics are broken down into simple, intuitive steps for deep conceptual understanding.

* **LaTeX Mathematical Rendering**
  Supports professional scientific notation and equations using LaTeX formatting.

* **Modern Full-Stack Architecture**
  Decoupled backend (Django REST Framework) and frontend (React + Vite) for scalability and maintainability.

* **Secure API Management**
  Sensitive credentials are stored using environment variables and excluded from version control.

---

## 🛠️ Tech Stack

### Frontend

* React.js (Vite)
* Axios

### Backend

* Django 6.0
* Django REST Framework

### AI Engine

* Google Gemini Pro API

### Database

* SQLite (Development)

---

## 📂 Project Structure

```
├── backend/                 # Django 6.0 backend
│   ├── chatbot/             # Core chatbot logic & Gemini integration
│   └── services.py          # AI system prompting and persona control
│
├── frontend/                # React application
│   └── src/api/             # Axios API configuration
│
└── .gitignore               # Prevents sensitive files from being committed
```

---

## ⚙️ Installation & Setup

### 1. Backend Setup

Navigate to the backend directory:

```
cd backend
```

Create a `.env` file and add your Gemini API key:

```
GOOGLE_API_KEY=your_key_here
```

Install dependencies, apply migrations, and start the server:

```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

### 2. Frontend Setup

Navigate to the frontend directory:

```
cd frontend
```

Install dependencies and start the development server:

```
npm install
npm run dev
```

---

## 🔐 Security

* API keys are stored securely using environment variables.
* `.env` files are excluded via `.gitignore`.
* Backend and frontend remain fully decoupled for safer deployments.

---

## 🎯 Use Cases

* Conceptual understanding of physics topics
* Academic revision and learning
* AI-assisted teaching tools
* Educational and research-based projects

---

## 📌 Future Enhancements

* User authentication and query history
* Support for additional academic domains
* Cloud deployment and Docker integration
* Enhanced mathematical visualization support

---
## 👤 Author

Mouly Sikdar
B.Tech Student | Full-Stack Developer | AI & Physics Enthusiast

🔗 GitHub: [@Mouly19]( https://github.com/Mouly19)

---

## 📜 License

This project is intended for educational and research purposes.
You are free to modify and extend it with proper attribution.

---


“True understanding begins when complex ideas can be explained simply ✨⚛️.”



