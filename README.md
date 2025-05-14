
# 🧠 JEE Questions Database

A structured, extensible, and database-agnostic system to store and manage JEE questions using LaTeX formatting for precise mathematical representation. Built using Python and SQLAlchemy for ORM-based database interaction, with current support for SQLite (and PostgreSQL in the future).

---

## 📌 Features

- Store **JEE-level questions** with metadata:
  - Year
  - Shift
  - Subject
  - Topic
- Questions and options are written in **LaTeX**, allowing:
  - Integrals: `\int`
  - Derivatives: `\frac{d}{dx}`
  - Square roots: `\sqrt{}`
  - Summation: `\sum`
  - And much more!
- Add questions:
  - Through interactive CLI
  - From JSON files
  - From CSV files
- ORM-powered using **SQLAlchemy**: DB-agnostic design.
- Uses **SQLite** for local development (PostgreSQL-ready for production).

---

## 🏗️ Database Schema

Each question entry includes the following fields:

```python
year = Column(Integer)
shift = Column(String)
subject = Column(String)
topic = Column(String)
question_latex = Column(Text)
option_a = Column(Text)
option_b = Column(Text)
option_c = Column(Text)
option_d = Column(Text)
correct_option = Column(String)
solution_latex = Column(Text, nullable=True)
````

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/R-Kri/QuestionsDB.git
cd QuestionsDB
```

### 2️⃣ Create a Virtual Environment (in VS Code or terminal)

```bash
python3 -m venv .venv
source .venv/bin/activate     # On Linux/macOS
.venv\Scripts\activate        # On Windows
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python main.py
```

---

## 📥 Adding Questions

### 📟 Option 1: CLI-based Input

Run `main.py` and follow the prompts to enter questions interactively via terminal.

### 📄 Option 2: JSON Import

Place your questions in a `questions.json` file with the following format:

```json
[
  {
    "year": 2024,
    "shift": "Morning",
    "subject": "Math",
    "topic": "Calculus",
    "question_latex": "What is \\( \\int x^2 dx \\)?",
    "option_a": "\\( x^3 + C \\)",
    "option_b": "\\( \\frac{x^3}{3} + C \\)",
    "option_c": "\\( 2x + C \\)",
    "option_d": "\\( x^2 + C \\)",
    "correct_option": "B",
    "solution_latex": "Using power rule: \\( \\int x^n dx = \\frac{x^{n+1}}{n+1} + C \\)"
  }
]
```

### 📊 Option 3: CSV Import

Add questions in a `.csv` file with appropriate headers:

```
year,shift,subject,topic,question_latex,option_a,option_b,option_c,option_d,correct_option,solution_latex
```

Example:

```csv
2024,Morning,Math,Calculus,"What is \(\int x^2 dx\)?","\(\frac{x^3}{3} + C\)","\(\int x^3 dx\)","\(\int x dx\)","\(\int x^2 dx\)",B,"Using power rule: \(\int x^n dx = \frac{x^{n+1}}{n+1} + C\)"
```

---

## 🔄 Future Improvements

* Switch from SQLite to **PostgreSQL** for production environments.
* Web-based UI for managing questions.
* Admin panel for bulk editing and approval.
* API for integration with external platforms.

---

## 🧪 Example LaTeX Usage

Question:

```latex
What is the derivative of \( \sin x \)?
```

Options:

* $\cos x$
* $-\cos x$
* $\sin x$
* $-\sin x$

---

## 📂 Suggested Project Structure

```
JEE_QUESTIONS/
├── __pycache__/
├── .venv/
├── venv/
├── data_entry.py
├── database.py
├── exampleQ.json
├── jee_questions.db
├── main.py
├── models.py
├── query_utils.py
├── requirements.txt
├── seed_data.py
├── view_db.py
```

---

## 📜 License

MIT License — use freely, but give credit where due.

---

## 🤝 Contributions

Contributions are welcome! Open issues, suggest features, or create a pull request.

---

## 📧 Contact

Maintainer: [R-Kri](https://github.com/R-Kri)

```

---

Let me know if you'd like help generating the actual `requirements.txt`, project structure, or code templates (`main.py`, `models.py`, etc.).
```
