import streamlit as st
import google.generativeai as genai
import os
import time
import requests
from bs4 import BeautifulSoup

HARDCODED_API_KEY = "your_api_key"
TARGET_URL = "https://www.ncsc.admin.ch/ncsc/en/home.html"

st.set_page_config(
    page_title="Swiss CyberBot",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data(show_spinner=False)
def scrape_website(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for script in soup(["script", "style", "nav", "footer"]):
            script.extract()
            
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        cleaned_text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return cleaned_text[:15000] 
    except Exception as e:
        return f"Error scraping website: {e}"

PORTAL_DATA = """
PRIMARY PORTAL: National Cyber Security Centre (NCSC)
- Link: https://www.ncsc.admin.ch/ncsc/en/home.html
- Purpose: The NCSC is the Swiss federal government's competence centre for cybersecurity. It serves as the first point of contact for businesses, public services, educational institutions, and the general population regarding cyber issues.
- Key Features:
  1. Incident Reporting Form: Centralized tool to report phishing, malware, ransomware, and fraud.
  2. Cyber Security Hub (CSH): A secure platform for critical infrastructure to share threat intelligence.
  3. Situational Analysis: Publishes semi-annual reports on the Swiss threat landscape.
  4. Awareness: Provides guides for SMEs, IT specialists, and individuals.
- Cyber Function: It coordinates the implementation of the National Cyberstrategy (NCS), issues public warnings, and supports operators of critical infrastructure in managing cyber incidents.
"""

SWISS_LAWS_AND_CONTEXT = """
SWISS LAWS & REGULATIONS:
1. Federal Act on Data Protection (FADP/nFADP):
   - Revised act entered into force September 1, 2023.
   - Aligns with EU GDPR but retains Swiss identity.
   - Key elements: Privacy by design/default, mandatory breach reporting to FDPIC if high risk.
   
2. NCSC (National Cyber Security Centre) Mandates:
   - The central hub for cyber reporting in Switzerland.
   - Mandatory Reporting: From April 2025, critical infrastructure operators must report cyberattacks to NCSC within 24 hours.

3. FINMA Circular 2023/1:
   - Applicable to banks and financial institutions.
   - Requires management of ICT risks and cyber resilience.
"""

if "live_context" not in st.session_state:
    with st.spinner(f"Connecting to NCSC Live Data ({TARGET_URL})..."):
        scraped_data = scrape_website(TARGET_URL)
        if "Error" not in scraped_data:
            st.session_state.live_context = scraped_data
        else:
            st.session_state.live_context = "" 

with st.sidebar:
    st.title("🛡️ Menu")
    
    app_mode = st.selectbox(
        "Select View", 
        ["🤖 Chat Assistant", "📡 Compliance Docs"],
    )
    st.divider()

    if HARDCODED_API_KEY != "YOUR_API_KEY_HERE":
        api_key = HARDCODED_API_KEY
        genai.configure(api_key=api_key)
    else:
        api_key = st.text_input("Enter Gemini API Key", type="password")
        if api_key:
            genai.configure(api_key=api_key)
    
    if st.session_state.live_context:
        st.success("🟢 NCSC Connected")
    else:
        st.error("🔴 Offline Mode")

    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = [
            {"role": "assistant", "content": "Conversation cleared. How can I help you with Swiss cybersecurity?"}
        ]
        st.rerun()

    st.divider()
    st.caption("Developed for Swiss Cyber Research")
    st.link_button("Open NCSC Portal", TARGET_URL, use_container_width=True)

if app_mode == "🤖 Chat Assistant":
    st.subheader("🇨🇭 Swiss Cyber Assistant")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Grüezi! I am connected to the NCSC live feed. How can I help you with Swiss cybersecurity today?"}
        ]

    for message in st.session_state.messages:
        avatar = "🛡️" if message["role"] == "assistant" else "👤"
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    if prompt := st.chat_input("Type your question here..."):
        if not api_key:
            st.error("Please enter your Gemini API Key in the sidebar.")
        else:
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user", avatar="👤"):
                st.markdown(prompt)

            with st.chat_message("assistant", avatar="🛡️"):
                message_placeholder = st.empty()
                message_placeholder.markdown("Analyzing...")
                
                try:
                    model = genai.GenerativeModel('gemini-2.5-flash-preview-09-2025')
                    chat = model.start_chat(history=[])
                    
                    live_data_section = ""
                    if st.session_state.live_context:
                        live_data_section = f"\nDATA SOURCE 3 (LIVE WEB SCRAPE - {TARGET_URL}):\n{st.session_state.live_context}\n"
                    
                    FULL_CONTEXT = f"""
                    You are an advanced Cybersecurity Assistant specialized in the Swiss Digital Landscape.

                    DATA SOURCE 1 (PRIMARY PORTAL):
                    {PORTAL_DATA}

                    DATA SOURCE 2 (SWISS LAWS & REGULATIONS):
                    {SWISS_LAWS_AND_CONTEXT}
                    
                    {live_data_section}

                    INSTRUCTIONS:
                    1. Answer questions based on the provided context.
                    2. Prioritize Source 3 (Live Data) for current events.
                    3. Be professional, concise, and helpful.
                    """
                    
                    full_prompt = f"{FULL_CONTEXT}\n\nUser Question: {prompt}"
                    
                    response = chat.send_message(full_prompt)
                    full_response = response.text
                    
                    message_placeholder.markdown(full_response)
                    st.session_state.messages.append({"role": "assistant", "content": full_response})
                    
                except Exception as e:
                    st.error(f"⚠️ AI Error: {e}")

elif app_mode == "📡 Compliance Docs":
    st.title("📡 Cyber Circulars")
    st.markdown("Fetch compliance documents and view timelines.")
    
    st.info("Select an authority to retrieve the latest simulated documents.")

    target_authority = st.selectbox("Authority", ["NCSC", "FINMA", "FDPIC"], label_visibility="collapsed")
    
    if st.button("Fetch Documents", use_container_width=True):
        progress_text = "Connecting..."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        st.success("Retrieved.")
        
        if "NCSC" in target_authority:
            st.markdown("### 📄 NCSC Reports")
            st.markdown("""
            - **NCSC Semi-Annual Report 2024.pdf** (2.4 MB)
            """)
        elif "FINMA" in target_authority:
             st.markdown("### 📄 FINMA Circulars")
             st.markdown("""
            - **Circular 2023/1 Ops Risks.pdf** (3.5 MB)
            """)
        else:
              st.markdown("### 📄 FDPIC Guides")
              st.markdown("""
            - **nFADP Implementation Checklist.pdf** (1.2 MB)
            """)

    st.divider()
    st.subheader("📊 Timeline")
    st.write("📅 **Sept 2023:** FADP Entry into Force")
    st.write("📅 **Jan 2024:** ISA Updates")
    st.write("📅 **Apr 2025:** NCSC Mandatory Reporting")
