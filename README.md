# SWISS CYBERGUARD — Swiss Cyber Assistant

Swiss CyberGuard is a Streamlit-powered intelligence layer engineered to operationalize Swiss cybersecurity information, regulatory insights, and compliance documentation. The solution integrates a conversational AI interface with real-time retrieval of content from the Swiss National Cyber Security Centre (NCSC), enabling users to query laws, guidelines, and threat advisories with precision.

---

## 🚀 Key Capabilities

### **🔎 Conversational Cyber Assistant**
Interactive chatbot powered by free AI API integrations (Gemini / OpenRouter).  
Automatically augments responses with live-scraped NCSC insights.

### **📡 Live NCSC Context Integration**
The application scrapes and extracts relevant text from the official NCSC public portal to enrich responses with Switzerland-specific cyber intelligence.

### **📁 Compliance Circulars & Timeline Viewer**
A dedicated module to view simulated circulars and regulatory time-series artifacts for streamlined compliance tracking.

### **📊 Streamlit Web Interface**
Clear, interactive UI with two major operational modes:
- Cyber Assistant  
- Compliance Documentation Dashboard  

---

## 📦 Repository Structure

/.gitattributes
/LICENSE
/README.md
/requirements.txt
/switzerland_cyber_bot.py

yaml
Copy code

---

## ⚙️ Installation & Setup

### **1. Clone Repository**
```bash
git clone <your-repository-url>
cd <your-folder>
2. Create & Activate Virtual Environment
bash
Copy code
python -m venv .venv

# macOS & Linux
source .venv/bin/activate

# Windows
.venv\Scripts\Activate.ps1
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure API Keys
The prototype contains a hardcoded API key.
Remove it immediately and use environment variables or Streamlit secrets.

Example:

bash
Copy code
export GEMINI_API_KEY="your_gemini_key"
export OPENAI_API_KEY="your_openai_key"
5. Launch the App
bash
Copy code
streamlit run switzerland_cyber_bot.py
Application will start at:

arduino
Copy code
http://localhost:8501
🧩 Technical Architecture
Core Functional Modules
Module	Description
Gemini/Generative AI Interface	Generates conversational responses using free AI APIs
NCSC Scraper	Real-time extraction of Swiss cybersecurity advisories
Context Engine	Prioritizes scraped data for improved answer precision
Compliance Dashboard	Loads static/simulated circular documents
Streamlit UI	Frontend interface with multi-tab layout

Tech Stack
Python

Streamlit

Google Generative AI / Gemini API

BeautifulSoup (NCSC scraping)

Pandas

Plotly (timeline visualization)

🛡️ Security Best Practices
Rotate all credentials before deployment.

Use Streamlit Secrets or environment variables for sensitive configuration.

Avoid logging PII or storing chat history without user consent.

Validate that scraping respects NCSC’s public access rules.

Add rate-limiting if deploying for large user volume.

📈 Roadmap Enhancements
Feature	Status
Replace simulated circulars with real PDFs	Planned
Conversation memory (secure)	Planned
Multi-country cyber law support	Planned
Role-Based Access Control (RBAC)	Under evaluation
Vector search for scraped content	Future release

🤝 Contributing
Fork repository

Create feature branch

Make improvements

Submit Pull Request with detailed summary

📄 License
This repository is distributed under the terms defined in the LICENSE file.
