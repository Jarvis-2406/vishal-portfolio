import streamlit as st
from PIL import Image

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Vishal Anand's Portfolio",
    page_icon="👋",
    layout="wide",
)

# --- THEME MANAGEMENT ---
if "theme" not in st.session_state:
    st.session_state["theme"] = "dark"

def toggle_theme():
    st.session_state["theme"] = "light" if st.session_state["theme"] == "dark" else "dark"

# --- THEME COLORS ---
if st.session_state["theme"] == "light":
    primary_gradient_start = "#f8f8f8"
    primary_gradient_end = "#e0e0e0"
    text_color = "#212121"
    accent_color = "#558b2f"
    content_background = "#ffffff"
    button_bg = "linear-gradient(to right, #81c784, #66bb6a)"
    button_text_color = "#ffffff"
    card_bg = "rgba(0, 0, 0, 0.03)"
    card_border = "rgba(0, 0, 0, 0.1)"
else: # Dark theme
    primary_gradient_start = "#1e1e1e"
    primary_gradient_end = "#2c3e50"
    text_color = "#ffffff"
    accent_color = "#f1c40f"
    content_background = "#1a1a1a"
    button_bg = "linear-gradient(to right, #424242, #1e1e1e)"
    button_text_color = "white"
    card_bg = "rgba(255, 255, 255, 0.05)"
    card_border = "rgba(255, 255, 255, 0.2)"


# --- CUSTOM CSS ---
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Roboto+Slab:wght@700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');

    body {{
        font-family: 'Lato', sans-serif;
        color: {text_color};
    }}

    /* Main container background */
    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(180deg, {primary_gradient_start}, {primary_gradient_end});
    }}

    /* Hide Streamlit's default header and footer */
    [data-testid="stHeader"], footer {{
        display: none;
    }}
    
    /* General Typography */
    h1, h2, h3 {{
        font-family: 'Roboto Slab', serif;
        font-weight: 700;
        color: {text_color};
    }}

    /* Project and Certification Cards */
    .card {{
        background-color: {card_bg};
        border-radius: 12px;
        padding: 2rem;
        border: 1px solid {card_border};
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 100%;
    }}
    .card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    }}
    .card h3 {{
        color: {accent_color};
        font-size: 1.3rem;
        margin-bottom: 0.75rem;
    }}
    .card p {{
        font-size: 1rem;
        color: {text_color};
        flex-grow: 1;
    }}

    /* Grid layout for cards */
    .card-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1.5rem;
    }}

    /* GitHub Button on Project Cards */
    .github-button {{
        background: {button_bg};
        color: {button_text_color} !important;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        cursor: pointer;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        margin-top: 1rem;
        text-decoration: none;
        display: inline-block;
        font-size: 0.9rem;
        font-weight: bold;
    }}
    .github-button:hover {{
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }}

    /* Skills Section Styling */
    .skills-section {{
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        padding: 2.5rem;
        border-radius: 15px;
        color: white;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }}
    .skills-section h2 {{
        text-align: center;
        margin-bottom: 2rem;
        color: white;
    }}
    .skills-category {{
        font-size: 1.25rem;
        margin-top: 1.5rem;
        font-weight: bold;
        text-decoration: underline;
    }}
    .skill-list {{
        padding-top: 0.5rem;
        padding-left: 1.2rem;
        font-size: 1rem;
        line-height: 1.8;
    }}
    
    /* Contact Section Styling */
    .social-buttons {{
        text-align: center;
        margin-top: 1rem;
    }}
    .social-button {{
        color: {text_color};
        margin: 0 15px;
        font-size: 2rem;
        transition: color 0.3s ease, transform 0.3s ease;
    }}
    .social-button:hover {{
        color: {accent_color};
        transform: scale(1.2);
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# --- HEADER & PROFILE ---
col1, col2 = st.columns([0.85, 0.15])
with col1:
    st.header("👋 Hey, I'm **Vishal Anand**")
    st.subheader("Aspiring Data Professional")
with col2:
    st.button("🌙" if st.session_state["theme"] == "dark" else "☀️", on_click=toggle_theme, key="theme_toggle")

st.image("vishal.jpg", use_container_width=True)


# --- RESUME BUTTONS ---
with open("Vishal Anand.pdf", "rb") as f:
    pdf_bytes = f.read()

google_drive_file_id = "1GuPDBqmRCobDLmr_dmv6Jg5xlPGplONX"
viewer_url = f"https://drive.google.com/file/d/{google_drive_file_id}/preview"

col1, col2 = st.columns(2)
with col1:
    st.download_button(
        label="📄 Download My Resume",
        data=pdf_bytes,
        file_name="VishalAnand_Resume.pdf",
        mime="application/pdf",
        use_container_width=True,
    )
with col2:
    st.markdown(f'<a href="{viewer_url}" target="_blank"><button style="width:100%; padding: 0.25rem 0.5rem; border-radius: 0.5rem; border-width: 1px; border-style: solid; border-color: rgb(222, 222, 228); color: {text_color}; background-color: transparent;">👀 View My Resume</button></a>', unsafe_allow_html=True)


# --- ABOUT ME ---
st.header("🧑‍💼 About Me")
st.write("""
Hi, I’m Vishal Anand, a data professional passionate about using data to solve problems and drive insights. With skills in SQL, Python, Excel, and data visualization, I enjoy analyzing and presenting data to help organizations make informed decisions. Outside of data, I love cooking, traveling, and listening to podcasts.
""")


# --- SKILLS (CORRECTED) ---
st.markdown("""
<div class="skills-section">
    <h2>🛠️ Skills</h2>
    
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


# --- EXPERIENCE ---
st.header("💼 Experience")
st.subheader("HSBC — Contact Centre Executive (Nov 2022 - Nov 2024)")
st.markdown("""
- Analyzed 10,000+ customer interactions using SQL and Excel, reducing false positives by 20%.
- Developed Power BI dashboards to monitor KPIs, improving SLA adherence by 15%.
- Maintained >95% QA scores while reducing Average Handling Time (AHT) by 18%.
""")
st.subheader("BYJUS — Business Development Associate (Dec 2020 - Sep 2022)")
st.markdown("""
- Conducted cohort analysis & A/B testing across 100K+ users, improving retention by 15%.
- Built Tableau dashboards on engagement metrics, contributing to a 10% reduction in churn.
- Leveraged SQL for targeted lead generation, boosting conversion rates by 20%.
""")

# --- PROJECTS (CORRECTED - ALL 5 PROJECTS RESTORED) ---
st.header("📁 Projects")
st.markdown(
    """
    <div class="card-grid">
        <div class="card">
            <h3>AI-powered Financial Audit Assistant</h3>
            <p>Automated document search and verification using LangChain and OpenAI to improve audit efficiency.</p>
            <a href="https://github.com/Jarvis-2406/GenAI-for-Financial-Audits" target="_blank" class="github-button">GitHub Repo</a>
        </div>
        <div class="card">
            <h3>Gold Price Prediction</h3>
            <p>Built a predictive ML model with XGBoost to forecast gold prices, including comprehensive EDA with Pandas & Seaborn.</p>
            <a href="https://github.com/Jarvis-2406/Gold-Price-Prediction" target="_blank" class="github-button">GitHub Repo</a>
        </div>
        <div class="card">
            <h3>BellaBeat Data Insights</h3>
            <p>Performed an in-depth EDA on smart device usage data to provide strategic business recommendations, visualized with Tableau.</p>
            <a href="https://github.com/Jarvis-2406/BellaBeat-Data-Insights" target="_blank" class="github-button">GitHub Repo</a>
        </div>
        <div class="card">
            <h3>Counterfeit Fraud Analysis</h3>
            <p>Detects counterfeit transactions using ML on an e-commerce dataset. Includes preprocessing, modeling, and evaluation.</p>
            <a href="https://github.com/Jarvis-2406/Counterfeit-Transaction-Detection" target="_blank" class="github-button">GitHub Repo</a>
        </div>
        <div class="card">
            <h3>Financial Planner</h3>
            <p>A single-page web app for personal finance tracking, analysis, and forecasting with interactive visualizations.</p>
            <a href="https://github.com/Jarvis-2406/Financial-Planner" target="_blank" class="github-button">GitHub Repo</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- CERTIFICATIONS ---
st.header("📜 Certifications")
st.markdown(
    """
    <div class="card-grid">
        <div class="card"><h3>Google Data Analytics</h3><p>Coursera</p></div>
        <div class="card"><h3>SAS Certified Specialist</h3><p>Base Programming</p></div>
        <div class="card"><h3>GenAI Concepts</h3><p>Kaggle</p></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- LANGUAGES ---
st.header("🗣️ Languages")
st.markdown("- **English** (Fluent), **Hindi** (Native), **Telugu** (Native), **German** (Basic)")

# --- CONTACT ---
st.header("📬 Contact")
st.markdown(
    """
    <div class="social-buttons">
        <a href="https://www.linkedin.com/in/vishal-anand2404/" target="_blank" class="social-button"><i class="fab fa-linkedin"></i></a>
        <a href="https://github.com/Jarvis-2406" target="_blank" class="social-button"><i class="fab fa-github"></i></a>
        <a href="mailto:vishalanand2406@gmail.com" class="social-button"><i class="far fa-envelope"></i></a>
    </div>
    <p style="text-align: center; margin-top: 1rem;">+91-7989353480</p>
    """,
    unsafe_allow_html=True,
)
