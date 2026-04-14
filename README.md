# 🛡️ SWISS CYBERGUARD — Swiss Cyber Assistant

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Prototype-orange?style=for-the-badge)

**Swiss CyberGuard** is a Streamlit-driven cybersecurity intelligence layer engineered to deliver authoritative insights on Swiss cyber laws, guidelines, and real-time advisories.

It fuses a conversational AI interface with contextual knowledge retrieved from the **Swiss National Cyber Security Centre (NCSC)**, enabling users to access actionable, regulation-aligned information instantly.

---

## 🚀 Core Value Proposition

### **🤖 AI-Enhanced Cyber Assistant**
* A conversational engine powered by free AI APIs (Gemini / OpenRouter).
* Provides concise, context-aware responses to cybersecurity queries.

### **🌐 Real-Time NCSC Intelligence Sync**
* Scrapes and aggregates publicly available content from the Swiss NCSC portal.
* Injects fresh regulatory and threat-advisory data into every response.

### **📁 Compliance Documentation Hub**
* Dedicated interface to surface simulated circulars, directives, and regulatory timelines.
* Enables rapid compliance readiness and traceability.

### **🖥️ Streamlit UX**
* Interactive, modular interface supporting:
    * Cyber Assistant Mode
    * Compliance Documentation Dashboard

---

## 📦 Repository Structure

```text
/
├── .gitattributes
├── LICENSE
├── README.md
├── requirements.txt
└── switzerland_cyber_bot.py
```
## ⚙️ Deployment Guide

Follow these steps to set up the environment locally.

### 1. Clone Repository
```bash
git clone <your-repo-url>
cd <your-folder>
```
### 2. Initialize Virtual Environment
# Create the virtual environment
```text 
python -m venv .venv
```

# Activate environment (macOS / Linux)
```text
source .venv/bin/activate
```

# Activate environment (Windows)
```text
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```text
pip install -r requirements.txt
```

### 4. Configure Secrets (Mandatory)
```text
API keys = "your_gemini_key_here"
```

### 5. Run Application
```text
streamlit run switzerland_cyber_bot.py
```
The app will launch automatically at: http://localhost:8501

### **🧩 Architectural Overview**
System Components
Component	Description
AI Model Interface	Uses Gemini / OpenRouter for text generation
NCSC Scraper	Pulls live data from Swiss NCSC public pages
Context Engine	Merges scraped intelligence into chat responses
Compliance Viewer	Displays simulated circular documents & timelines
Streamlit UI Layer	Frontend interaction surface

### **Technology Stack**

* Python
* Streamlit
* Google Generative AI SDK
* BeautifulSoup4
* Pandas
* Plotly

### **🛡️ Security & Operational Controls**

* Enforce environment-based key management

* Ensure zero logging of user PII

* Run scraper within acceptable access constraints

* Add rate-limiting and user throttling in production

* Perform periodic key rotation and secret scanning

### **📈 Product Roadmap**
* Enhancement	Status
* Replace simulated circulars with real PDF ingestion	Upcoming
* Role-based access management	Under analysis
* Vector search for NCSC content	Future iteration
* Multi-country cyber intelligence expansion	Planned
* Persistent conversation history with anonymization	In pipeline
### 🤝 Contribution Model

* Fork the repository

* Create a feature branch

* Implement enhancements / fixes

* Submit a pull request with detailed notes

### **📄 Licensing**

* Refer to the MIT LICENSE file for usage and distribution terms.

## Disclaimer
### This tool accesses only publicly available information and complies with the NCSC’s public usage policies.
### This project is an educational prototype.
### It does not provide legal advice.
### It is not affiliated with any government authority. 
