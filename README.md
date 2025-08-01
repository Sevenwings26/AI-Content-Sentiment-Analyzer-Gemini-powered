# ✨ AI Content Generator & Sentiment Analyzer (Gemini-powered)

This project is a lightweight FastAPI application powered by **Google Gemini (gemini-2.5-flash)**. It enables users to:

1. **Generate detailed content** on any topic (e.g., “Django”, “Climate Change”, “AI in Education”).
2. **Analyze the sentiment** and readability of any selected portion of that content — or any custom input.
2. **Generate keywords** on any content for SEOs and marketking campaigns.

---

## 🚀 How It Works

### 1. 📚 Generate Content

* Send a topic to the `/generate/` endpoint.
* The app uses **Gemini API** to generate a well-structured, informative article.
* The generated content is returned and stored in the database.

#### 🔁 Example

**Request:**

```json
{
  "topic": "FastAPI as an option for API development"
}
```

**Response:**

```json
{
  "generated_text": "FastAPI: The Modern Python Powerhouse for Blazing-Fast API Development — In the ever-evolving landscape of web development, building robust..."
}
```

---

### 2. 🧠 Analyze Sentiment

* Select a passage or paragraph from the content (or provide any text).
* Submit it to the `/analyze/` endpoint.
* The model returns:

  * A basic **readability score**.
  * A **sentiment classification** (Positive, Neutral, or Negative).
  * A **brief explanation** for the sentiment label.

#### 💬 Example

**Input:**

```text
"At its core, Django is a powerful, open-source web framework written in Python..."
```

**Response:**

```json
{
  "readability": "Readability Score: Good",
  "sentiment": "The sentiment of the text is **positive**.\n\nHere's why:\n\n* The text uses positive descriptive words like \"powerful\".\n* \"open-source\" is generally viewed positively.\n* \"well-known\" implies acceptance and trust.\n* The tone is clear, technical, and favorable."
}
```

---
### 3. 🗝 Keywords Generator

* Select a passage or paragraph from the content (or provide any text).
* Submit it to the `/keywords/` endpoint.
* The model returns:

  * A detailed group of **keywords**.

#### 💬 Example

**Input:**

```text
" The AI Agent Engineer Roadmap: Charting Your Course in the Autonomous Future..."
```

**Response:**

```json
{
  "generated_keywords": "AI Agent Engineer, AI agents, Autonomous AI systems, AI Agent Engineer roadmap, Become an AI Agent Engineer, AI Agent Engineer career, AI Agent Engineer skills, Python for AI, AI agent maintenance, Machine Learning Engineer vs AI Agent Engineer,..."
}
```

---

## 🧪 Existing Endpoints

| Method | Endpoint     | Description                                |
| ------ | ------------ | ------------------------------------------ |
| GET    | `/`          | Landing form/test page                     |
| POST   | `/generate/` | Generate article content based on topic    |
| POST   | `/analyze/`  | Perform readability and sentiment analysis |
| POST   | `/keywords/`  | Extract keywords and concepts for SEO/tagging |

---

## 🔮 Upcoming Features (Planned Endpoints)

| Method | Endpoint       | Description                                   |
| ------ | -------------- | --------------------------------------------- |
| POST   | `/summarize/`  | Summarize long-form generated content         |
| POST   | `/questions/`  | Auto-generate questions from the content      |
| POST   | `/plagiarism/` | Check for originality or potential plagiarism |

---

## 🧵 Concurrency with Multithreading & Semaphore

This app leverages Python's `threading` module and **semaphore control** to handle multiple concurrent requests efficiently.

### Why Semaphore?

```python
semaphore = threading.Semaphore(5)
```

The semaphore ensures that **only 5 threads** can access the Gemini API at a time — preventing overloads or exceeding rate limits.

### ✅ Benefits:

* ⚡ **Improved Performance** – Allows concurrent handling of tasks.
* 🔒 **Controlled Resource Access** – Avoids API throttling or failure.
* 🧠 **Thread-Safe Gemini Integration** – Manages external calls gracefully.

---

## 🛠️ Tech Stack

* **FastAPI** – Fast, intuitive Python web framework
* **Google Generative AI (Gemini 2.5 Flash)** – For content generation and NLP
* **SQLAlchemy** – ORM for database interactions
* **SQLite / PostgreSQL** – Flexible database support
* **Pydantic** – Schema validation and parsing
* **Threading + Semaphore** – Efficient concurrent processing
* **Alembic** – Flexible DB migration support

---

## 🏡 Database Migration
* Run on terminal:
  `pip install alembic`
  `alembic upgrade head`
  `alembic revision --autogenerate -m "migration"`

---

## 🎓 Inspiration

This project was inspired by **Zakari Yahali**, freecodecamp, whose encouragement sparked the fusion of generative AI with simple, research-focused web tools. Zaks also suggested that this project could expand into broader NLP functionalities like summarization and question generation.

---

## 🧰 Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/Sevenwings26/AI-Content-Generator-Sentiment-Analyzer-Gemini-powered.git
cd AI-Content-Generator-Sentiment-Analyzer-Gemini-powered

# 2. Set up a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create a .env file
echo "GEMINI_API_KEY=your_api_key_here" > .env

# 5. Run the app
uvicorn main:app --reload
```

---

## 🧩 Folder Structure (Optional)

```
.
├── App
|   ├── crud.py
|   ├── database.py
|   ├── main.py
|   ├── models.py
|   ├── schemas.py
|   ├── utility.py
└── .env
└── .gitignore
└── README.md
└── requirements.txt
```

---

## 📬 Contact & Feedback

* 📧 Email: [iarowosola@gmail.com](mailto:iarowosola@gmail.com)
* 🔗 LinkedIn: [linkedin.com/in/iyanuarowosola](http://www.linkedin.com/in/iyanuarowosola)








