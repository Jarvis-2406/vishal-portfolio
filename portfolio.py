import streamlit as st
from PIL import Image
import base64

# Initialize theme state in session state if it doesn't exist
if "theme" not in st.session_state:
    st.session_state["theme"] = "light"

# Function to toggle the theme
def toggle_theme():
    st.session_state["theme"] = "dark" if st.session_state["theme"] == "light" else "light"

# Define theme colors based on the current state
if st.session_state["theme"] == "light":
    primary_gradient_start = "#f8f8f8"  # Very light gray
    primary_gradient_end = "#ffffff"    # White
    secondary_gradient_start = "#f8f8f8"  # Very light gray
    secondary_gradient_end = "#ffffff"    # White
    text_color = "#212121"            # Very Dark Gray
    accent_color = "#558b2f"            # Olive Green
    content_background = "#ffffff"      # White
    button_bg = "linear-gradient(to right, #81c784, #66bb6a)"  # Light Green
    button_text_color = "#ffffff"
else:
    primary_gradient_start = "#2c3e50"  # Dark Blue-Gray
    primary_gradient_end = "#34495e"    # Even Darker Blue-Gray
    secondary_gradient_start = "#3498db"  # Bright Blue
    secondary_gradient_end = "#2980b9"  # Darker Blue
    text_color = "#ffffff"            # White
    accent_color = "#f1c40f"            # Yellow
    content_background = "#1a1a1a"      # Near Black
    button_bg = "linear-gradient(to right, #424242, #1e1e1e)"
    button_text_color = "white"

# Custom Theme Configuration
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
    .css-1adrpsg {{
        font-weight: 600;
        color: {text_color};
    }}
    .stDownloadButton > button {{
        background: {button_bg};
        color: {button_text_color};
        border: 1px solid rgba(255,255,255,0.3);
        border-radius: 10px;
        padding: 0.8rem 2rem;
        cursor: pointer;
        transition: background-color 0.3s ease-in-out, transform 0.1s ease;
        margin-top: 1rem;
    }}
    .stDownloadButton > button:hover {{
        background: linear-gradient(to right, #9ccc65, #8bc34a);
        transform: scale(1.05);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }}
    a {{
        color: {accent_color};
        text-decoration: none;
        transition: color 0.3s ease-in-out;
    }}
    a:hover {{
        color: lighten({accent_color}, 20%);
    }}
    div[data-testid="stMarkdownContainer"] > p {{
        color: {text_color};
        line-height: 1.7;
        font-size: 1.1rem;
    }}
    .skills-section {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2.5rem;
        margin-top: 2rem;
    }}
    .skill-box {{
        background-color: rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease-in-out, transform 0.2s ease, box-shadow 0.3s ease;
    }}
    .skill-box:hover {{
        background-color: rgba(255, 255, 255, 0.15);
        transform: translateY(-5px);
        box-shadow: 0 10px 12px rgba(0, 0, 0, 0.2);
    }}
    .skill-box h3 {{
        margin-bottom: 1.25rem;
        color: {accent_color};
        font-size: 1.5rem;
        font-weight: 600;
        letter-spacing: 0.5px;
    }}
    .skill-box ul {{
        list-style: none;
        padding: 0;
        margin: 0;
        font-size: 1.1rem;
    }}
    .skill-box li {{
        margin-bottom: 0.8rem;
        opacity: 0.9;
    }}
    .certifications-section, .projects-section {{
        margin-top: 2rem;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2.5rem;
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
    .project-card h3, .certification-card h3 {{
        margin-bottom: 0.75rem;
        color: {accent_color};
        font-size: 1.3rem;
        font-weight: 600;
        letter-spacing: 0.5px;
    }}
    .project-card p, .certification-card p{{
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
    .social-buttons {{
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        margin-top: 2rem;
    }}
    .social-button {{
        background: {button_bg};
        color: {button_text_color};
        border: 1px solid rgba(255,255,255,0.3);
        border-radius: 50%;
        width: 60px;
        height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
        cursor: pointer;
        transition: background-color 0.3s ease-in-out, transform 0.1s ease, box-shadow 0.3s ease;
        text-decoration: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }}
    .social-button:hover {{
        background: linear-gradient(to right, #aed581, #7cb342);
        transform: scale(1.1);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
    }}
    .phone-info{{
        margin-top: 1.5rem;
        text-align: center;
        font-size: 1.2rem;
        color: {text_color}
    }}
    .theme-button {{
        background: none;
        border: none;
        color: {text_color};
        cursor: pointer;
        font-size: 1.2rem;
        padding: 0.5rem;
        display: flex;
        align-items: center;
        transition: color 0.3s ease;
    }}
    .theme-button:hover {{
        color: {accent_color};
    }}
    hr {{
        margin: 3rem 0;
        border: 0;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.header(f"👋 Hey, I'm **Vishal Anand**")
# Add dark theme toggle button
st.button("🌙", on_click=toggle_theme, key="theme_toggle")

# Load and display image (increased width)
image = Image.open("vishal.jpg")
st.image(image, width=700, caption="Vishal Anand", use_container_width=True)
st.markdown(f"<h3 style='margin-bottom: 2rem;'>Aspiring Data Professional</h3>", unsafe_allow_html=True)


with open("VISHAL ANAND 2.pdf'f", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="📄 **My Resume**",
                    data=PDFbyte,
                    file_name="'VISHAL ANAND 2.pdf'",
                    mime='application/octet-stream')

# About Me (Updated Content)
st.header("**🧑‍💼 About Me**")
st.write("""
Hi, I’m Vishal Anand, an aspiring data professional passionate about using data to solve problems and drive insights.
With skills in SQL, Python, Excel, and data visualization, I enjoy analyzing and presenting data to help organizations
make informed decisions. Outside of data, I love cooking, traveling, and listening to podcasts. I’m excited to grow
in this field and contribute to data-driven solutions.
""")

# Skills (Detailed and in Columns)
st.header("**🛠️ Skills**")
st.markdown(
    """
    <div class="skills-section">
        <div class="skill-box">
            <h3>Programming</h3>
            <ul>
                <li>Python (Pandas, NumPy, Seaborn, Matplotlib)</li>
                <li>R</li>
                <li>SAS</li>
            </ul>
        </div>
        <div class="skill-box">
            <h3>Data Analysis & Manipulation</h3>
            <ul>
                <li>Excel (PivotTables, Power Query, DAX)</li>
                <li>SQL (Joins, Aggregations, Subqueries)</li>
            </ul>
        </div>
        <div class="skill-box">
            <h3>Data Visualization</h3>
            <ul>
                <li>Tableau</li>
                <li>Power BI</li>
            </ul>
        </div>
        <div class="skill-box">
            <h3>Machine Learning & AI</h3>
            <ul>
                <li>Predictive Modeling</li>
                <li>Data Mining</li>
            </ul>
        </div>
        <div class="skill-box">
            <h3>Business & Analytics Tools</h3>
            <ul>
                <li>KPI Tracking</li>
                <li>Stakeholder Management</li>
                <li>Business Intelligence</li>
            </ul>
        </div>
        <div class="skill-box">
            <h3>Analytical Skills</h3>
            <ul>
                <li>Data Wrangling</li>
                <li>Data Visualization</li>
                <li>Decision-Making with Data</li>
                <li>Data Ethics</li>
            </ul>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Experience
st.header("**💼 Experience**")
st.subheader("**HSBC — Contact Centre Executive (Nov 2022 - Nov 2024)**")
st.markdown("""
•	Analyzed over 10,000+ customer interactions using SQL and Excel to identify fraud indicators, contributing to a 20% reduction in false positives.
•	Developed Power BI dashboards to monitor service KPIs (AHT, CSAT, FCR), leading to a 15% improvement in SLA adherence.
•	Consistently maintained >95% quality assurance scores while handling high-volume customer queries, reducing average handling time by 18%.
•	Delivered data-backed presentations to senior management, driving policy enhancements in fraud handling and customer retention.
•	Collaborated with Risk and Compliance teams on predictive analytics models to detect account takeover and unauthorized transactions.
""", True)

st.subheader("**BYJUS — Business Development Associate (Dec 2020 - Sep 2022)**")
st.markdown("""
•	Conducted cohort analysis and A/B testing across 100K+ users, improving learner retention by 15% on NEET and K-12 learning platforms.
•	Created interactive Tableau dashboards on user engagement, optimizing app features and reducing churn by 10%.
•	Leveraged SQL to identify high-potential leads, increasing sales conversion by 20% through refined targeting.
•	Contributed to UX/product improvements by surfacing actionable user feedback during analytics reviews.
•	Successfully generated sales and revenue exceeding ₹1 crore through strategic client engagement and personalized demo sessions.
""", True)

# Projects
st.header("**📁 Projects**")
st.markdown(
    """
    <div class="projects-section">
        <div class="project-card">
            <h3>AI-powered Financial Audit Assistant</h3>
            <p>Automated document search using LangChain & OpenAI</p>
            <a href="https://github.com/Jarvis-2406/GenAI-for-Financial-Audits" target="_blank" class="github-button">
                GitHub Repo
            </a>
        </div>
        <div class="project-card">
            <h3>Gold Price Prediction</h3>
            <p>Built predictive ML model with XGBoost</p>
            <p>EDA using Pandas & Seaborn</p>
            <a href="https://github.com/Jarvis-2406/Gold-Price-Prediction" target="_blank" class="github-button">
                GitHub Repo
            </a>
        </div>
        <div class="project-card">
            <h3>BellaBeat Data Insights</h3>
            <p>Performed EDA on smart device data</p>
            <p>Visualized findings with Tableau</p>
            <a href="https://github.com/Jarvis-2406/BellaBeat-Data-Insights" target="_blank" class="github-button">
                GitHub Repo
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Certifications (Styled Cards) - No Images
st.header("**📜 Certifications**")
st.markdown(
    """
    <div class="certifications-section">
        <div class="certification-card">
            <h3>Google Professional Data Analytics</h3>
            <p>Coursera</p>
        </div>
        <div class="certification-card">
            <h3>SAS Certified Specialist</h3>
            <p>Base Programming</p>
        </div>
        <div class="certification-card">
            <h3>GenAI</h3>
            <p>Kaggle</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Languages
st.header("**🗣️ Languages**")
st.markdown("""
- **English**, **Hindi**, **Telugu**, **German (Basic)**
""", True)

# Contact Section
st.header("**📬 Contact**")
st.markdown(
    """
    <div class="social-buttons">
        <a href="https://www.linkedin.com/in/vishal-anand2404/" target="_blank" class="social-button">
            <i class="fab fa-linkedin"></i>
        </a>
        <a href="https://github.com/Jarvis-2406" target="_blank" class="social-button">
            <i class="fab fa-github"></i>
        </a>
        <a href="https://www.instagram.com/vishalanand2404/?hl=en" target="_blank" class="social-button">
            <i class="fab fa-instagram"></i>
        </a>
        <a href="mailto:vishalanand2406@gmail.com" class="social-button">
            <i class="far fa-envelope"></i>
        </a>
    </div>
    <div class = "phone-info">
        <p> +91-7989353480</p>
    </div>
    """,
    unsafe_allow_html=True,
)
