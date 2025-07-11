# ✨ AI Content Generator & Sentiment Analyzer (Gemini-powered)

This project is a lightweight FastAPI application powered by **Google Gemini (gemini-2.5-flash)**. It allows users to:

1. **Generate detailed content** based on a topic (e.g., "Django", "Climate Change", "AI in Education").
2. **Analyze the sentiment** of any portion of that generated content (or any custom text).

---

## 🚀 How It Works

### 1. Generate Content
- Submit a **topic** via the `/generate/` endpoint.
- The app uses the **Gemini API** to generate a well-structured, detailed article related to the topic.
- The generated article is stored and returned.

#### 🔁 Example
Request:
```json
{
  "topic": "Fastapi as option for API development"
}
````

Response:

```json
{
  "generated_text": "FastAPI: The Modern Python Powerhouse for Blazing-Fast API Development - 
  In the ever-evolving landscape of web development, building robust..."
}
```

---

### 2. Analyze Sentiment

* Select a **portion** of the content (or any free-form paragraph).
* Submit it to the `/analyze/` endpoint.
* The model returns:

  * A **readability score** (basic rating).
  * A **sentiment classification**: Positive, Neutral, or Negative.
  * A short explanation of the result.

#### 🧠 Example

Submitted content:

```text
"At its core, Django is a powerful, open-source web framework written in Python..."
```

Response:

```json
{
  "readability": "Readability Score: Good",
  "sentiment": "The sentiment of the text is overwhelmingly **positive**.

Here's why:

* **Strong Positive Adjectives/Nouns:** Powerhouse," "Blazing-Fast," "robust," "high-performance," "scalable," "paramount," "go-to language," "cutting-edge," "unparalleled," "leading contender."

}
```

---

## 🧪 Endpoints Summary

| Method | Endpoint     | Description                          |
| ------ | ------------ | ------------------------------------ |
| GET   | `/`           | Landing page/Form |
| POST   | `/generate/` | Generate content from a topic        |
| POST   | `/analyze/`  | Analyze sentiment of a given passage |

---

## 🔧 Tech Stack

* **FastAPI** – Lightweight Python web framework
* **Google Generative AI (Gemini 2.5 Flash)** – Content generation and NLP
* **SQLAlchemy** – ORM for data persistence
* **SQLite/PostgreSQL** – Database layer (configurable)
* **Pydantic** – Schema validation

---

## 🎓 Inspiration

This project was inspired by **Zakari Yahali**, whose work encouraged the blending of generative AI with lightweight research and analysis tools.

---

## ⚙️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/Sevenwings26/AI-Content-Generator-Sentiment-Analyzer-Gemini-powered.git

cd gemini-content-analyzer

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Run the app
uvicorn main:app --reload

```

---

## 📬 Contact / Feedback

For feedback or collaboration, feel free to reach out.

---

```

Let me know if you'd like to add screenshots, a frontend client, or deployment instructions (e.g., Render or Docker).
```
