# 🔐 Phishing URL Blocker

Rule-Based + Backend-Supported Browser Extension

[![Python](https://img.shields.io/badge/python-v3.11-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

📌 Project Overview

Phishing URL Blocker is a browser-based security solution designed to detect and block phishing websites in real time.
The system combines a browser extension with a Python backend that uses a rule-based dataset to identify malicious URLs.

This project demonstrates a practical cybersecurity use case, focusing on URL analysis, rule-based detection, and user safety.

🎯 Objectives

Prevent users from accessing known phishing websites

Demonstrate phishing detection using rule-based techniques

Integrate browser extensions with backend logic

Provide a scalable foundation for ML-based enhancements

enhancements

🚀 Features

🚫 Blocks phishing URLs before page load

📜 Rule-based detection using CSV datasets

🌐 Browser extension (Manifest v3 compatible)

🧠 Backend URL validation using Python

⚠️ Warning page shown to users for unsafe sites

📂 Clean and modular project structure

🧠 System Architecture

<img width="260" height="350" alt="image" src="https://github.com/user-attachments/assets/7ab9b6c4-5afd-4317-ab84-e54a7bfdb1f9" />


 🛠️ Tech Stack
 
🔹 Frontend (Browser Extension)

- JavaScript

- HTML, CSS

Chrome Extension (Manifest v3)

🔹 Backend

- Python

CSV-based phishing URL dataset

📂 Project Structure

PHISHING-URL-BLOCKER/

│

├── backend/

│   ├── app.py

│   ├── check_csv.py


│   ├── load_urls.py

│   ├── phishing_site_urls.csv

│   └── __pycache__/

│

├── extension/

│   ├── metadata/

│   ├── background.js

│   ├── manifest.json

│   ├── rules.json

│   ├── style.css

│   ├── warning.html

│   └── warning.js

│

├── README.md

▶️ How to Run the Project

1️⃣ Backend Setup

    cd backend

    python app.py

2️⃣ Load Extension in Browser

- Open Chrome

- Go to chrome://extensions

- Enable Developer Mode

- Click Load Unpacked

- Select the extension/ folder

🧪 How It Works

- User attempts to open a website

- Extension intercepts the request

- URL is checked against phishing rules/dataset

- If phishing detected:

  Website is blocked

  Warning page is displayed

If safe:

  Website loads normally

🎯 Use Cases

- Protect users from phishing attacks

- Academic & hackathon demonstrations

- Cybersecurity learning projects

- Foundation for ML-based phishing detection systems

🔮 Future Enhancements

✅ Machine Learning-based URL classification

📊 Risk scoring system

🌍 Detection of newly emerging phishing sites

📈 Admin dashboard for analytics

🔌 Integration with email & corporate security tools

👤 Author

Nikesh Babu S

B.E Computer Science and Design (CSD)

🔗 GitHub: https://github.com/Nikesh-dev-06

📧 Email: nikes.dev.06gmail@gmail.com


