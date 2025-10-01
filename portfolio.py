import streamlit as st
from PIL import Image
import base64
from pathlib import Path

# --- FONT AWESOME IMPORT ---
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
""", unsafe_allow_html=True)

# --- FUNCTION TO ENCODE IMAGES ---
def image_to_base64(img_path):
    """Converts a local image file to a base64 string."""
    try:
        img_bytes = Path(img_path).read_bytes()
        suffix = Path(img_path).suffix[1:]
        mime_type = "jpeg" if suffix.lower() in ["jpg", "jpeg"] else suffix.lower()
        return f"data:image/{mime_type};base64,{base64.b64encode(img_bytes).decode()}"
    except FileNotFoundError:
        return "https://via.placeholder.com/150?text=Image+Not+Found"

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
    primary_gradient_start = "#FFFFFF"
    primary_gradient_end = "#F0F2F6"
    text_color = "#212529"
    accent_color = "#007BFF"
    button_bg = "linear-gradient(to right, #007BFF, #0056b3)"
    button_text_color = "#FFFFFF"
    card_bg = "rgba(255, 255, 255, 0.7)"
    card_border = "rgba(0, 0, 0, 0.1)"
else: # Dark theme
    primary_gradient_start = "#121212"
    primary_gradient_end = "#121212"
    text_color = "#F8F9FA"
    accent_color = "#08F7FE"
    button_bg = "linear-gradient(to right, #08F7FE, #00BFFF)"
    button_text_color = "#121212"
    card_bg = "rgba(255, 255, 255, 0.07)"
    card_border = "rgba(8, 247, 254, 0.3)"

# --- CUSTOM CSS ---
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap');

    body {{
        font-family: 'Times New Roman', serif !important;
        color: {text_color};
    }}
    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(180deg, {primary_gradient_start}, {primary_gradient_end});
    }}
    [data-testid="stHeader"], footer {{
        display: none;
    }}
    
    h1, h2, h3, p, li, .st-emotion-cache-1629p8f {{
        color: {text_color} !important;
    }}
    h1, h2, h3 {{
        font-family: 'Playfair Display', serif !important;
        font-weight: 700;
    }}
    p, li {{
        font-family: 'Times New Roman', serif !important;
    }}
    h2 {{
        text-align: center;
        width: 100%;
        margin-bottom: 1rem;
    }}
    .header-section {{
        text-align: center;
        width: 100%;
        padding-top: 1rem;
    }}
    .header-section h1 {{
        margin-bottom: 0.5rem;
    }}
    .header-section p {{
        font-family: 'Times New Roman', serif !important;
        font-size: 1.25rem;
    }}

    .card {{
        background-color: {card_bg};
        border-radius: 12px;
        padding: 1.5rem;
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
        color: {accent_color} !important;
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
    }}
    .card-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1rem;
    }}
    
    .flip-card {{
        background-color: transparent;
        min-height: 450px;
        perspective: 1000px;
    }}
    .flip-card-inner {{
        position: relative;
        width: 100%;
        height: 100%;
        transition: transform 0.7s;
        transform-style: preserve-3d;
    }}
    .flip-card:hover .flip-card-inner {{
        transform: rotateY(180deg);
    }}
    .flip-card-front, .flip-card-back {{
        position: absolute;
        width: 100%;
        height: 100%;
        -webkit-backface-visibility: hidden;
        backface-visibility: hidden;
        background-color: {card_bg};
        border-radius: 12px;
        border: 1px solid {card_border};
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        transition: box-shadow 0.3s ease;
    }}
    .flip-card:hover .flip-card-front,
    .flip-card:hover .flip-card-back {{
        box-shadow: 0 12px 24px rgba(0,0,0,0.2);
    }}
    .flip-card-front {{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 1rem;
    }}
    .flip-card-back {{
        transform: rotateY(180deg);
        padding: 1.5rem;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }}
    .company-logo {{
        max-width: 85%;
        max-height: 85%;
        object-fit: contain;
        border-radius: 8px;
    }}
    .experience-content {{
        text-align: left;
        margin-top: 0.5rem;
        line-height: 1.4;
    }}
    .experience-content p {{
        font-size: 0.9rem;
    }}
    
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
        color: {accent_color} !important;
        transform: scale(1.2);
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- ENCODE LOCAL IMAGES ---
amazon_logo_b64 = image_to_base64("amazon-png-logo-vector-6695.png")
cognizant_logo_b64 = image_to_base64("Cognizant().png")
hsbc_logo_b64 = image_to_base64("HSBC().png")
byjus_logo_b64 = image_to_base64("Byjus.png")

# --- HEADER & PROFILE ---
_, col2 = st.columns([0.9, 0.1])
with col2:
    st.button("🌙" if st.session_state["theme"] == "dark" else "☀️", on_click=toggle_theme, key="theme_toggle")

st.markdown(f"""
<div class="header-section">
    <h1>👋 Hey, I'm <strong>Vishal Anand</strong></h1>
    <p>The Amiable Analyst, Catching Bad Apples 🍎</p>
</div>
""", unsafe_allow_html=True)

# --- IMAGE ---
img_col1, img_col2, img_col3 = st.columns([1, 2, 1])
with img_col2:
    st.image("IMG_0217.JPG")

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
st.write(f"""
<div style="text-align: center; color: {text_color};">
    Hi, I’m Vishal Anand, a data professional passionate about using data to solve problems and drive insights. With skills in SQL, Python, Excel, and data visualization, I enjoy analyzing and presenting data to help organizations make informed decisions. Outside of data, I love cooking, traveling, and listening to podcasts.
</div>
""", unsafe_allow_html=True)

# --- EDUCATION ---
st.header("🎓 Education")
st.markdown(f"""
<div style="text-align: center;">
    <h3>MBA in Business Analytics (WILP)</h3>
    <p><strong>BITS Pilani</strong> | 2024 - 2026 (Pursuing)</p>
    <br>
    <h3>B.Tech in Computer Science & Engineering</h3>
    <p><strong>Jawaharlal Nehru Technological University</strong>, Hyderabad | 2016 - 2020</p>
</div>
""", unsafe_allow_html=True)

# --- SKILLS ---
st.header("🛠️ Skills")
st.markdown("""
<div class="card-grid">
    <div class="card"><h3>Programming</h3><p>Python (Pandas, NumPy)<br>R<br>SAS</p></div>
    <div class="card"><h3>Data Analysis</h3><p>Excel (PivotTables, Power Query)<br>SQL (Joins, Subqueries)</p></div>
    <div class="card"><h3>Visualization</h3><p>Tableau<br>Power BI</p></div>
    <div class="card"><h3>Machine Learning</h3><p>Predictive Modeling<br>Data Mining</p></div>
</div>
""", unsafe_allow_html=True)

# --- EXPERIENCE ---
st.header("💼 Experience")
st.markdown(f"""
<div class="card-grid">
    <div class="flip-card">
        <div class="flip-card-inner">
            <div class="flip-card-front"><img src="{amazon_logo_b64}" alt="Amazon Logo" class="company-logo"></div>
            <div class="flip-card-back">
                <h3>Risk Specialist - Abuse Risk Mining</h3>
                <p><strong>Amazon</strong> | Oct 2025 - Present</p>
                <div class="experience-content"><p>As a Risk Specialist in Amazon’s Abuse Risk Mining team, I detect and mitigate fraud and high-risk activities by analyzing data patterns, investigating emerging abuse trends, and driving process improvements. I collaborate across teams to enhance risk strategies, automate detection, and uphold customer trust and marketplace integrity.</p></div>
            </div>
        </div>
    </div>
    <div class="flip-card">
        <div class="flip-card-inner">
            <div class="flip-card-front"><img src="{cognizant_logo_b64}" alt="Cognizant Logo" class="company-logo"></div>
            <div class="flip-card-back">
                <h3>Process Specialist</h3>
                <p><strong>Cognizant</strong> | Sep 2025 - Sep 2025</p>
                <div class="experience-content"><p>Supported US clients on the DocuSign platform, assisting with key features like eSignatures, templates, and envelope workflows, and helped them resolve issues and optimize processes.</p></div>
            </div>
        </div>
    </div>
    <div class="flip-card">
        <div class="flip-card-inner">
            <div class="flip-card-front"><img src="{hsbc_logo_b64}" alt="HSBC Logo" class="company-logo"></div>
            <div class="flip-card-back">
                <h3>Contact Centre Executive</h3>
                <p><strong>HSBC</strong> | Nov 2022 - Nov 2024</p>
                <div class="experience-content"><p>Delivered banking support to UK customers, managing accounts, high-value payments, fraud alerts, and disputes with >93% quality scores. Supported chat process (38–45 WPM), maintained AHT/ACW targets, and ranked among top NPS performers. Collaborated with backend teams to improve processes, reduce escalations, and enhance first-time resolution..</p></div>
            </div>
        </div>
    </div>
    <div class="flip-card">
        <div class="flip-card-inner">
            <div class="flip-card-front"><img src="{byjus_logo_b64}" alt="BYJUS Logo" class="company-logo"></div>
            <div class="flip-card-back">
                <h3>Business Development Associate</h3>
                <p><strong>BYJUS</strong> | Dec 2020 - Sep 2022</p>
                <div class="experience-content"><p>Drove ₹1Cr+ in sales through personalized demos and parent counseling. Promoted to Interim Manager, led 7-member team to ₹50L in 2 months. Consistently awarded “Best Performer,” trained new hires, optimized CRM pipelines, and boosted conversions with tailored strategies.</p></div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- PROJECTS ---
st.header("📁 Projects")
st.markdown(
    """
    <div class="card-grid">
        <div class="card">
            <h3>AI-powered Financial Audit Assistant</h3><p>Automated document search and verification using LangChain and OpenAI to improve audit efficiency.</p>
            <a href="https://github.com/Jarvis-2406/GenAI-for-Financial-Audits" target="_blank" class="github-button">GitHub Repo</a>
        </div>
        <div class="card">
            <h3>Gold Price Prediction</h3><p>Built a predictive ML model with XGBoost to forecast gold prices, including EDA with Pandas & Seaborn.</p>
            <a href="https://github.com/Jarvis-2406/Gold-Price-Prediction" target="_blank" class="github-button">GitHub Repo</a>
        </div>
        <div class="card">
            <h3>BellaBeat Data Insights</h3><p>Performed an in-depth EDA on smart device usage data to provide strategic business recommendations.</p>
            <a href="https://github.com/Jarvis-2406/BellaBeat-Data-Insights" target="_blank" class="github-button">GitHub Repo</a>
        </div>
        <div class="card">
            <h3>Counterfeit Fraud Analysis</h3><p>Detects counterfeit transactions using ML on an e-commerce dataset.</p>
            <a href="https://github.com/Jarvis-2406/Counterfeit-Transaction-Detection" target="_blank" class="github-button">GitHub Repo</a>
        </div>
        <div class="card">
            <h3>Financial Planner</h3><p>A single-page web app for personal finance tracking, analysis, and forecasting.</p>
            <a href="https://github.com/Jarvis-2406/Financial-Planner" target="_blank" class="github-button" style="margin-right: 5px;">GitHub Repo</a>
            <a href="https://financial-planner-zwx6rstcdc6czwgjfwcvtt.streamlit.app/" target="_blank" class="github-button" style="margin-left: 5px;">Live App 🚀</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- CERTIFICATIONS ---
st.header("📜 Certifications")
st.markdown("""
<div class="card-grid">
    <div class="card"><h3>Google Data Analytics</h3><p>Coursera</p></div>
    <div class="card"><h3>SAS Certified Specialist</h3><p>Base Programming</p></div>
    <div class="card"><h3>Deloitte Australia</h3><p>Data Analytics Job Simulation (Forage)</p></div>
    <div class="card"><h3>GenAI Concepts</h3><p>Kaggle</p></div>
</div>
""", unsafe_allow_html=True)

# --- LANGUAGES ---
st.header("🗣️ Languages")
st.markdown(f"<div style='text-align: center; color: {text_color};'><strong>English</strong> (Fluent) • <strong>Hindi</strong> (Native) • <strong>Telugu</strong> (Native) • <strong>German</strong> (Basic)</div>", unsafe_allow_html=True)

# --- CONTACT ---
st.header("📬 Contact")
st.markdown("""
<div class="social-buttons">
    <a href="https://www.linkedin.com/in/vishal-anand2404/" target="_blank" class="social-button"><i class="fab fa-linkedin"></i></a>
    <a href="https://github.com/Jarvis-2406" target="_blank" class="social-button"><i class="fab fa-github"></i></a>
    <a href="mailto:vishalanand2406@gmail.com" class="social-button"><i class="far fa-envelope"></i></a>
</div>
<p style="text-align: center; margin-top: 1rem;">+91-7989353480</p>
""", unsafe_allow_html=True)
