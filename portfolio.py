import streamlit as st
from PIL import Image

# Initialize theme state in session state if it doesn't exist
if "theme" not in st.session_state:
    st.session_state["theme"] = "light"

# Function to toggle the theme
def toggle_theme():
    st.session_state["theme"] = "dark" if st.session_state["theme"] == "light" else "light"

# Display the toggle switch
st.sidebar.checkbox("🌟", value=(st.session_state["theme"] == "dark"), on_change=toggle_theme)

# Define theme colors based on the current state (Modern Gradient Theme)
if st.session_state["theme"] == "light":
    primary_gradient_start = "#f0f2ff"  # Light Lavender
    primary_gradient_end = "#e0eafc"    # Light Periwinkle
    secondary_gradient_start = "#d1c4e9"  # Light Lilac
    secondary_gradient_end = "#b39ddb"    # Medium Purple
    text_color = "#212121"            # Very Dark Gray
    accent_color = "#7e57c2"            # Deep Purple
    content_background = "#ffffff"      # White
    button_bg = "linear-gradient(to right, #7e57c2, #5e35b1)"  # Deep Purple Gradient
    button_text_color = "white"
else:
    primary_gradient_start = "#1a1a2e"  # Very Dark Purple
    primary_gradient_end = "#3f37c9"    # Dark Indigo
    secondary_gradient_start = "#485696"  # Dark Slate Blue
    secondary_gradient_end = "#242424"    # Near Black
    text_color = "#ffffff"            # White
    accent_color = "#90caf9"            # Light Blue
    content_background = "#121212"      # Black
    button_bg = "linear-gradient(to right, #4a148c, #1a237e)"  # Darker Purple Gradient
    button_text_color = "white"

# Custom Theme Configuration
st.markdown(
    f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(to bottom, {primary_gradient_start}, {primary_gradient_end});
        color: {text_color};
        min-height: 100vh;
    }}
    [data-testid="stHeader"] {{
        background: rgba(0, 0, 0, 0.05);
        backdrop-filter: blur(12px);
        color: {text_color};
        padding: 2rem 1rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }}
    [data-testid="stSidebar"] {{
        background: linear-gradient(to bottom, {secondary_gradient_start}, {secondary_gradient_end});
        color: {text_color};
        padding: 1rem;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: {text_color};
    }}
    .st-eb {{
        background-color: {content_background};
        padding: 2.5rem;
        border-radius: 12px;
        color: {text_color};
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
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
        border: none;
        border-radius: 10px;
        padding: 0.8rem 2rem;
        cursor: pointer;
        transition: background-color 0.3s ease-in-out, transform 0.1s ease;
    }}
    .stDownloadButton > button:hover {{
        background: linear-gradient(to right, darken({button_bg}, 10%), darken({button_bg}, 15%));
        transform: scale(1.05);
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
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }}
    .skill-box {{
        background-color: rgba(255, 255, 255, 0.08);
        border-radius: 10px;
        padding: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease-in-out, transform 0.2s ease;
    }}
    .skill-box:hover {{
        background-color: rgba(255, 255, 255, 0.15);
        transform: translateY(-5px);
    }}
    .skill-box h3 {{
        margin-bottom: 1rem;
        color: {accent_color};
        font-size: 1.4rem;
        font-weight: 600;
    }}
    .skill-box ul {{
        list-style: none;
        padding: 0;
        margin: 0;
        font-size: 1.1rem;
    }}
    .skill-box li {{
        margin-bottom: 0.75rem;
        opacity: 0.9;
    }}
    .certifications-section {{
        margin-top: 2rem;
        overflow-x: auto;
        white-space: nowrap;
        padding-bottom: 1rem;
        display: flex;
        gap: 1rem;
    }}
    .certification-button {{
        background: {button_bg};
        color: {button_text_color};
        border: none;
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        cursor: pointer;
        transition: background-color 0.3s ease-in-out, transform 0.1s ease;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-width: 180px;
        white-space: nowrap;
        font-size: 1.1rem;
    }}
    .certification-button:hover {{
        background: linear-gradient(to right, darken({button_bg}, 10%), darken({button_bg}, 15%));
        transform: scale(1.05);
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.title(f"👋 Hey, I'm **Vishal Anand**")
# Load and display image (increased width)
image = Image.open("vishal.jpg")
st.image(image, width=250, caption="Vishal Anand")
st.markdown(f"### **Aspiring Data Professional**")

# Sidebar
st.sidebar.header("**Contact**")
st.sidebar.markdown("[📧 anand24061998@gmail.com](mailto:anand24061998@gmail.com)")
st.sidebar.markdown("[🔗 **LinkedIn**](https://www.linkedin.com/in/vishal-anand2404/)")
st.sidebar.markdown("[💻 **GitHub**](https://github.com/Jarvis-2406)")

with open("Vishal Anand .pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="📄 **My Resume**",
                    data=PDFbyte,
                    file_name="Vishal Anand .pdf",
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
- Built real-time dashboards to monitor service performance
- Used SQL & Power BI to improve fraud detection
- Led data reporting for operational efficiency
""", True)

st.subheader("**BYJUS — Business Development Associate (Dec 2020 - Sep 2022)**")
st.markdown("""
- Analyzed sales data using SQL
- Created dashboards with Tableau & Google Analytics
- Boosted conversion via data-driven lead segmentation
""", True)

# Projects
st.header("**📁 Projects**")
st.subheader("**1. AI-powered Financial Audit Assistant**")
st.markdown("""
- Automated document search using LangChain & OpenAI
- Implemented FAISS for fast retrieval
[🔗 **GitHub Repo**](https://github.com/Jarvis-2406/GenAI-for-Financial-Audits)
""", True)

st.subheader("**2. Gold Price Prediction**")
st.markdown("""
- Built predictive ML model with XGBoost
- EDA using Pandas & Seaborn
[🔗 **GitHub Repo**](https://github.com/Jarvis-2406/Gold-Price-Prediction)
""", True)

st.subheader("**3. BellaBeat Data Insights**")
st.markdown("""
- Performed EDA on smart device data
- Visualized findings with Tableau
[🔗 **GitHub Repo**](https://github.com/Jarvis-2406/BellaBeat-Data-Insights)
""", True)

# Certifications (Scrolling Buttons)
st.header("**📜 Certifications**")
st.markdown(
    """
    <div class="certifications-section">
        <div class="certification-button">Google Professional Data Analytics – Coursera</div>
        <div class="certification-button">SAS Certified Specialist – Base Programming</div>
        <div class="certification-button">GenAI – Kaggle</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Languages
st.header("**🗣️ Languages**")
st.markdown("""
- **English**, **Hindi**, **Telugu**, German (Basic)
""", True)
