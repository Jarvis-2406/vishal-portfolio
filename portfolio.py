# Vishal Anand - Streamlit Portfolio App (Modern Design)

import streamlit as st
from PIL import Image
import base64
import time

# Initialize theme
if "theme" not in st.session_state:
    st.session_state["theme"] = "light"

def toggle_theme():
    st.session_state["theme"] = "dark" if st.session_state["theme"] == "light" else "light"

# Theme settings
if st.session_state["theme"] == "light":
    bg_gradient = "linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%)"
    text_color = "#1c1c1c"
    accent_color = "#00c6ff"
    card_bg = "rgba(255, 255, 255, 0.5)"
    button_bg = "linear-gradient(to right, #43cea2, #185a9d)"
    button_hover = "linear-gradient(to right, #66e0c2, #3a70c0)"
else:
    bg_gradient = "linear-gradient(135deg, #232526 0%, #414345 100%)"
    text_color = "#f1f1f1"
    accent_color = "#ffafbd"
    card_bg = "rgba(0, 0, 0, 0.5)"
    button_bg = "linear-gradient(to right, #ff512f, #dd2476)"
    button_hover = "linear-gradient(to right, #ff867f, #ff6fbf)"

# Custom styles
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
body {{
    font-family: 'Poppins', sans-serif;
    color: {text_color};
}}
[data-testid="stAppViewContainer"] {{
    background: {bg_gradient};
    min-height: 100vh;
}}
.st-eb {{
    background: {card_bg};
    border-radius: 12px;
    padding: 2rem;
    box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    backdrop-filter: blur(12px);
    transition: all 0.3s ease-in-out;
}}
.st-eb:hover {{
    transform: translateY(-4px);
}}
button[kind="primary"] {{
    background: {button_bg};
    border: none;
    color: white;
    border-radius: 8px;
    padding: 0.6rem 1.2rem;
    font-weight: 600;
    transition: 0.3s;
}}
button[kind="primary"]:hover {{
    background: {button_hover};
    transform: scale(1.05);
}}
.view-resume-link {{
    background: {button_bg};
    color: white;
    padding: 0.7rem 1.5rem;
    font-size: 16px;
    border-radius: 10px;
    text-decoration: none;
    display: inline-block;
    margin-top: 1.5rem;
    transition: 0.3s;
}}
.view-resume-link:hover {{
    background: {button_hover};
    transform: translateY(-3px);
}}
.social-buttons {{
    display: flex;
    justify-content: center;
    gap: 1.2rem;
    margin-top: 2rem;
}}
.social-button {{
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: {button_bg};
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 1.5rem;
    transition: 0.3s;
}}
.social-button:hover {{
    background: {button_hover};
    transform: scale(1.1);
}}
</style>
""", unsafe_allow_html=True)

# Header
st.header("👋 Hey, I'm Vishal Anand")
icon = "🌞" if st.session_state["theme"] == "dark" else "🌙"
st.button(icon, on_click=toggle_theme, key="theme_toggle")

# Image
image = Image.open("vishal.jpg")
st.image(image, width=700, caption="Vishal Anand", use_container_width=True)
st.markdown("<h3 style='margin-bottom: 2rem;'>Aspiring Data Professional</h3>", unsafe_allow_html=True)

# Resume download
with open("Vishal Anand.pdf", "rb") as f:
    PDFbyte = f.read()
st.download_button("📄 Download My Resume", data=PDFbyte, file_name="Vishal Anand.pdf")

# Resume viewer
viewer_url = "https://drive.google.com/file/d/1GuPDBqmRCobDLmr_dmv6Jg5xlPGplONX/preview"
st.markdown(f"""
<a href="{viewer_url}" target="_blank" class="view-resume-link">👀 View My Resume</a>
""", unsafe_allow_html=True)

# About
st.header("🧑‍💼 About Me")
st.write("""
Hi, I’m Vishal Anand, an aspiring data professional passionate about using data to solve problems and drive insights.
With skills in SQL, Python, Excel, and data visualization, I enjoy analyzing and presenting data to help organizations
make informed decisions. Outside of data, I love cooking, traveling, and listening to podcasts. I’m excited to grow
in this field and contribute to data-driven solutions.
""")

# Skills
st.header("🛠️ Skills")
st.markdown("""
- **Languages**: Python, R, SAS
- **Tools**: Excel, SQL, Tableau, Power BI
- **Techniques**: Predictive Modeling, A/B Testing, Data Wrangling
- **Other**: Business Intelligence, KPI Analysis
""")

# Experience
st.header("💼 Experience")
st.subheader("HSBC — Contact Centre Executive")
st.caption("Nov 2022 - Nov 2024")
st.write("""
- Analyzed 10K+ interactions to identify fraud indicators
- Built dashboards with Power BI to monitor KPIs
- Collaborated on predictive analytics for fraud detection
""")

st.subheader("BYJU'S — Business Development Associate")
st.caption("Dec 2020 - Sep 2022")
st.write("""
- Conducted cohort analysis and A/B testing
- Created interactive Tableau dashboards
- Identified high-potential leads using SQL
""")

# Projects
st.header("📁 Projects")
st.write("""
- [AI-powered Financial Audit Assistant](https://github.com/Jarvis-2406/GenAI-for-Financial-Audits)
- [Gold Price Prediction](https://github.com/Jarvis-2406/Gold-Price-Prediction)
- [BellaBeat Data Insights](https://github.com/Jarvis-2406/BellaBeat-Data-Insights)
""")

# Certifications
st.header("📜 Certifications")
st.markdown("""
- Google Professional Data Analytics (Coursera)
- SAS Certified Specialist
- GenAI - Kaggle
""")

# Languages
st.header("🗣️ Languages")
st.write("English, Hindi, Telugu, German (Basic)")

# Contact
st.header("📬 Contact")
st.markdown("""
<div class="social-buttons">
    <a href="https://www.linkedin.com/in/vishal-anand2404/" target="_blank" class="social-button">
        <i class="fab fa-linkedin"></i>
    </a>
    <a href="https://github.com/Jarvis-2406" target="_blank" class="social-button">
        <i class="fab fa-github"></i>
    </a>
    <a href="mailto:vishalanand2406@gmail.com" class="social-button">
        <i class="far fa-envelope"></i>
    </a>
</div>
<p style="text-align: center; margin-top: 1rem;">📞 +91-7989353480</p>
""", unsafe_allow_html=True)
