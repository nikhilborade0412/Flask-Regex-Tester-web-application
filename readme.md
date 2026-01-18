
# 🔍 Regex Tester (Flask)

A simple and attractive **Regex Tester web application** built using **Flask**, inspired by the core functionality of **regex101.com**.

The application allows users to enter a **regular expression** and a **test string**, and upon clicking **Submit**, all matching parts of the text are **highlighted inside the test string**.

---
## ⚙️ Application Link
```bash
https://flask-regex-tester-web-application.onrender.com/
```

---

## ✨ Features

- Enter a **Regular Expression**
- Enter a **Test String**
- Click **Submit** to test the regex
- **Highlights all matched strings** inside the text
- Handles **invalid regex errors** gracefully
- Clean, modern, and responsive UI
- Lightweight & beginner-friendly Flask project

---

## 🛠️ Technologies Used

- **Python 3**
- **Flask**
- **HTML5**
- **CSS3**
- **Regular Expressions (re module)**

---

## 📁 Project Structure

```

regex-highlighter/
│── app.py
│── requirements.txt
│── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

````

---

## 🚀 How to Run the Project

### 1️⃣ Clone or Download the Project
```bash
git clone <your-repository-url>
cd regex-highlighter
````

---

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Flask Application

```bash
python app.py
```

---

### 5️⃣ Open in Browser

Visit:

```
http://127.0.0.1:5000
```

---

## 🧪 Example Usage

### Regex:

```
\bparagraph\b
```

### Test String:

```
A paragraph is a series of sentences.
Another paragraph is here.
```

### Output:

* Both occurrences of **paragraph** will be **highlighted** in the displayed text.

---

## 📦 requirements.txt

```txt
Flask==3.1.2
```

---

## 🎓 Use Cases

* Learning and practicing **Regular Expressions**
* Flask mini-project
* Web Technologies / Python practical assignment
* Portfolio project

---

## 📌 Future Enhancements (Optional)

* Regex flags support (i, m, s)
* Match counter
* Regex examples dropdown
* Copy highlighted text
* Live matching (AJAX)
* Deployment on Render / Railway

---

## 👨‍💻 Author

**Nikhil Borade**
Flask Mini Project – Regex Tester

---

## 🏁 License

This project is for **educational purposes** and is free to use and modify.

```
