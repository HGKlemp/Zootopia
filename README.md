# 🦁 Zootopia

A simple Python application that retrieves and displays animal information using the Animals API.

This project was created as part of the **Masterschool Software Engineering Backend** program to practice working with REST APIs, JSON data, HTML templates, and Python.

---

## 🚀 Features

* Search for animals by name
* Retrieve live data from the Animals API
* Parse JSON responses
* Generate an HTML page with the search results
* Handle invalid searches and API errors gracefully

---

## 🛠️ Technologies

* Python 3
* Requests
* HTML
* REST API
* JSON

---

## 📂 Project Structure

```text
Zootopia/
│
├── animals.py
├── animals_template.html
├── animals.html
├── data_fetcher.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/HGKlemp/Zootopia.git
cd Zootopia
```

Create and activate a virtual environment (optional but recommended):

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key

Create a file named `.env` in the project root.

Add your API key:

```text
API_KEY=YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your personal API key from API Ninjas.

---

## ▶️ Usage

Run the application:

```bash
python animals.py
```

Enter the name of an animal when prompted.

The application will fetch the data from the API and generate an HTML page containing the results.

---

## 📚 What I Learned

This project helped me practice:

* Working with REST APIs
* Sending HTTP requests
* Parsing JSON responses
* Using Python modules
* Error handling
* Generating HTML dynamically
* Organizing a Python project

---

## 📄 License

This project was created for educational purposes as part of the Masterschool Software Engineering Backend program.
