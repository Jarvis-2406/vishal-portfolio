import streamlit as st
from PIL import Image
import base64

# Initialize theme state
if "theme" not in st.session_state:
    st.session_state["theme"] = "light"

# Toggle theme
def toggle_theme():
    st.session_state["theme"] = "dark" if st.session_state["theme"] == "light" else "light"

# Theme colors
if st.session_state["theme"] == "light":
    primary_gradient_start = "#f8f8f8"
    primary_gradient_end = "#ffffff"
    secondary_gradient_start = "#f8f8f8"
    secondary_gradient_end = "#ffffff"
    text_color = "#212121"
    accent_color = "#558b2f"
    content_background = "#ffffff"
    button_bg = "linear-gradient(to right, #81c784, #66bb6a)"
    button_text_color = "#ffffff"
else:
    primary_gradient_start = "#2c3e50"
    primary_gradient_end = "#34495e"
    secondary_gradient_start = "#3498db"
    secondary_gradient_end = "#2980b9"
    text_color = "#ffffff"
    accent_color = "#f1c40f"
    content_background = "#1a1a1a"
    button_bg = "linear-gradient(to right, #424242, #1e1e1e)"
    button_text_color = "white"

# --- CUSTOM CSS THEME ---
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Arial:wght@400;700&family=Open+Sans:wght@400;700&family=Lato:wght@400;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');

    body {{
        font-family: 'Lato', sans-serif;
        color: {text_color};
    }}
    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(to bottom, {primary_gradient_start}, {primary_gradient_end});
        color: {text_color};
        min-height: 100vh;
        padding-bottom: 5rem;
    }}
    [data-testid="stHeader"] {{
        background: rgba(0, 0, 0, 0.05);
        backdrop-filter: blur(12px);
        color: {text_color};
        padding: 2rem 1rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: sticky;
        top: 0;
        z-index: 100;
    }}
    [data-testid="stSidebar"] {{
        background: linear-gradient(to bottom, {secondary_gradient_start}, {secondary_gradient_end});
        color: {text_color};
        padding: 1rem;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: {text_color};
        font-family: 'Times New Roman', serif;
        font-weight: 700;
        margin-bottom: 1.5rem;
        line-height: 1.2;
    }}
    p {{
        color: {text_color};
        line-height: 1.7;
        font-size: 1.1rem;
        margin-bottom: 1rem;
    }}
    .st-eb {{
        background-color: {content_background};
        padding: 2.5rem;
        border-radius: 12px;
        color: {text_color};
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        margin-bottom: 2rem;
    }}
    .st-eb:hover {{
        transform: translateY(-4px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }}
    .project-card, .certification-card {{
        background-color: rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease-in-out, transform 0.2s ease, box-shadow 0.3s ease;
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 200px;
    }}
    .project-card:hover, .certification-card:hover {{
        background-color: rgba(255, 255, 255, 0.15);
        transform: translateY(-5px);
        box-shadow: 0 10px 12px rgba(0, 0, 0, 0.2);
    }}
    .project-card h3 {{
        margin-bottom: 0.75rem;
        color: {accent_color};
        font-size: 1.3rem;
        font-weight: 600;
        letter-spacing: 0.5px;
    }}
    .project-card p {{
        font-size: 1.1rem;
        color: {text_color};
        margin-bottom: 0.5rem;
    }}
    .project-card .github-button {{
        background: {button_bg};
        color: {button_text_color};
        border: 1px solid rgba(255,255,255,0.3);
        border-radius: 10px;
        padding: 0.5rem 1rem;
        cursor: pointer;
        transition: background-color 0.3s ease-in-out, transform 0.1s ease;
        margin-top: 1rem;
        text-decoration: none;
        display: inline-block;
        font-size: 1rem;
    }}
    .project-card .github-button:hover {{
        background: linear-gradient(to right, #9ccc65, #8bc34a);
        transform: scale(1.05);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }}
    .projects-section {{
        margin-top: 2rem;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2.5rem;
    }}
    .certifications-section {{
        margin-top: 2rem;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2.5rem;
    }}
    
    /* --- CORRECTED SKILLS SECTION STYLES --- */
    .skills-section {{
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        padding: 30px;
        border-radius: 15px;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }}
    .skills-section h2 {{
        font-size: 28px;
        text-align: center;
        margin-bottom: 20px;
    }}
    .skills-category {{
        font-size: 20px;
        margin-top: 15px;
        font-weight: bold;
        text-decoration: underline;
    }}
    .skill-list {{
        margin-left: 20px;
        font-size: 16px;
        line-height: 1.8;
    }}

    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.header("👋 Hey, I'm **Vishal Anand**")
st.button("🌙", on_click=toggle_theme, key="theme_toggle")

# Profile Image
image = Image.open("vishal.jpg")
st.image(image, width=700, caption="Vishal Anand", use_container_width=True)
st.markdown("<h3 style='margin-bottom: 2rem;'>Aspiring Data Professional</h3>", unsafe_allow_html=True)

# Resume Download
with open("Vishal Anand.pdf", "rb") as f:
    PDFbyte = f.read()

st.download_button(
    label="📄 Download My Resume",
    data=PDFbyte,
    file_name="Vishal Anand.pdf",
    mime="application/octet-stream",
)

# Resume View
google_drive_file_id = "1GuPDBqmRCobDLmr_dmv6Jg5xlPGplONX"
viewer_url = f"https://drive.google.com/file/d/{google_drive_file_id}/preview"
st.markdown(f'<a href="{viewer_url}" target="_blank">👀 View My Resume</a>', unsafe_allow_html=True)

# About Me
st.header("🧑‍💼 About Me")
st.write("""
Hi, I’m Vishal Anand, an aspiring data professional passionate about using data to solve problems and drive insights.
With skills in SQL, Python, Excel, and data visualization, I enjoy analyzing and presenting data to help organizations
make informed decisions. Outside of data, I love cooking, traveling, and listening to podcasts.
""")

# --- REMOVED THE REDUNDANT CSS INJECTION THAT WAS HERE ---

# Add HTML content
st.markdown("""
<div class="skills-section">
    <h2>🛠 Skills</h2>
    
    <div class="skills-category">Programming</div>
    <div class="skill-list">
        Python (Pandas, NumPy, Matplotlib, Seaborn)<br>
        R<br>
        SAS
    </div>
    
    <div class="skills-category">Data Analysis</div>
    <div class="skill-list">
        Excel (PivotTables, Power Query, DAX)<br>
        SQL (Joins, Aggregations, Subqueries)
    </div>
    
    <div class="skills-category">Visualization</div>
    <div class="skill-list">
        Tableau<br>
        Power BI
    </div>
    
    <div class="skills-category">Machine Learning</div>
    <div class="skill-list">
        Predictive Modeling<br>
        Data Mining
    </div>
</div>
""", unsafe_allow_html=True)

# Experience
st.header("💼 Experience")
st.subheader("HSBC — Contact Centre Executive (Nov 2022 - Nov 2024)")
st.markdown("""
- Analyzed 10,000+ customer interactions using SQL and Excel, reducing false positives by 20%.  
- Developed Power BI dashboards to monitor KPIs, improving SLA adherence by 15%.  
- Consistently maintained >95% QA scores, reducing AHT by 18%.  
- Collaborated with Risk teams on predictive analytics models.  
""")

st.subheader("BYJUS — Business Development Associate (Dec 2020 - Sep 2022)")
st.markdown("""
- Conducted cohort analysis & A/B testing across 100K+ users, improving retention by 15%.  
- Built Tableau dashboards on engagement, reducing churn by 10%.  
- Leveraged SQL for lead targeting, boosting conversion by 20%.  
- Achieved ₹1 Cr+ in revenue via strategic sales.  
""")

# Projects
st.header("📁 Projects")
st.markdown(
    """
    <div class="projects-section">
        <div class="project-card">
            <h3>AI-powered Financial Audit Assistant</h3>
            <p>Automated document search using LangChain & OpenAI</p>
            <a href="https://github.com/Jarvis-2406/GenAI-for-Financial-Audits" target="_blank" class="github-button">GitHub Repo</a>
        </div>
        <div class="project-card">
            <h3>Gold Price Prediction</h3>
            <p>Built predictive ML model with XGBoost</p>
            <p>EDA using Pandas & Seaborn</p>
            <a href="https://github.com/Jarvis-2406/Gold-Price-Prediction" target="_blank" class="github-button">GitHub Repo</a>
        </div>
        <div class="project-card">
            <h3>BellaBeat Data Insights</h3>
            <p>EDA on smart device data</p>
            <p>Visualized with Tableau</p>
            <a href="https://github.com/Jarvis-2406/BellaBeat-Data-Insights" target="_blank" class="github-button">GitHub Repo</a>
        </div>
        <div class="project-card">
            <h3>Counterfeit Fraud Analysis</h3>
            <p>Detects counterfeit transactions using ML on e-commerce dataset.</p>
            <p>Includes preprocessing, modeling, evaluation, explainability.</p>
            <a href="https://github.com/Jarvis-2406/Counterfeit-Transaction-Detection" target="_blank" class="github-button">GitHub Repo</a>
        </div>
        <div class="project-card">
            <h3>Financial Planner</h3>
            <p>Single-page web app for personal finance tracking, analysis, forecasting.</p>
            <p>Interactive platform with visualization, AI-powered analysis, PDF reporting.</p>
            <a href="https://github.com/Jarvis-2406/Financial-Planner" target="_blank" class="github-button">GitHub Repo</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Certifications
st.header("📜 Certifications")
st.markdown(
    """
    <div class="certifications-section">
        <div class="certification-card"><h3>Google Data Analytics</h3><p>Coursera</p></div>
        <div class="certification-card"><h3>SAS Certified Specialist</h3><p>Base Programming</p></div>
        <div class="certification-card"><h3>GenAI</h3><p>Kaggle</p></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Languages
st.header("🗣️ Languages")
st.markdown("- **English**, **Hindi**, **Telugu**, **German (Basic)**")

# Contact
st.header("📬 Contact")
st.markdown(
    """
    <div class="social-buttons">
        <a href="https://www.linkedin.com/in/vishal-anand2404/" target="_blank" class="social-button"><i class="fab fa-linkedin"></i></a>
        <a href="https://github.com/Jarvis-2406" target="_blank" class="social-button"><i class="fab fa-github"></i></a>
        <a href="https://www.instagram.com/vishalanand2404/?hl=en" target="_blank" class="social-button"><i class="fab fa-instagram"></i></a>
        <a href="mailto:vishalanand2406@gmail.com" class="social-button"><i class="far fa-envelope"></i></a>
    </div>
    <div class="phone-info"><p>+91-7989353480</p></div>
    """,
    unsafe_allow_html=True,
)
