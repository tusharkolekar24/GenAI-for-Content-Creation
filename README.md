# GenAI for Content Creation

## 📌 Overview

This project is a **Generative AI-based Content Creation Tool** built using Flask, HTML, CSS, and JavaScript. It enables users to generate blogs, articles, social media posts, and creative content using a free GPT model. The application provides an intuitive web interface for users to enter prompts and receive AI-generated content instantly.

> ⚠ **Note:** This project currently uses a *free GPT API/model* which may have limited usage or expire over time. You can easily replace it with another model or API key when needed.

## ✨ Features

* 🧠 AI-powered content generation
* 🌐 Web-based interface with real-time text generation
* 📄 Multiple content formats supported (Blog, Ad Copy, Email, etc.)
* ⚡ Fast response with asynchronous JavaScript handling
* 🔑 Easy integration with different GPT APIs

## 📂 Project Structure

```
📦 Content-Creation-Project/
├── 📁 src/             # Core backend logic for API calls and GPT integration
├── 📁 static/          # CSS, JavaScript, images
├── 📁 templates/       # HTML templates (Home page, Content UI)
├── app.py              # Main Flask application
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

## 🛠️ Tech Stack

| Component  | Technology                 |
| ---------- | -------------------------- |
| Backend    | Flask (Python)             |
| Frontend   | HTML, CSS, JavaScript      |
| AI Model   | Free GPT API (replaceable) |
| Deployment | Local / Cloud compatible   |

## 🚀 Getting Started

### 1️⃣ Installation

```bash
git clone <your-repository-url>
cd Content-Creation-Project

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

### 2️⃣ Configure API Key

Replace your free GPT API key inside `src/config.py` or directly in `app.py`.

```python
API_KEY = "your_free_gpt_api_key_here"
```

### 3️⃣ Run the Application

```bash
python app.py
```

Now open your browser and visit: `http://127.0.0.1:5000/`

## 🧠 How It Works

1. User enters a prompt and selects content type.
2. Frontend sends the request to Flask.
3. Flask sends API call to GPT Model.
4. Response is displayed dynamically on the web UI.

## 🔄 Replacing the GPT Model

Since the free GPT API may expire:

* You can swap it with **OpenAI API**, **HuggingFace Models**, or **Local LLMs**.
* Update API endpoint and key in the backend.

## 🔮 Future Enhancements

* ✅ Add user authentication & content history
* ✅ Support for SEO optimization
* ✅ Download content as PDF or DOCX
* ✅ Integrate with custom fine-tuned LLMs

## 🤝 Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

Licensed under Apache-2.0 License.

---

### ⭐ If this project helps you, please consider giving it a star!
![image](https://github.com/user-attachments/assets/8181aca5-a90e-4bb7-84ce-7f13764f3c9d)
