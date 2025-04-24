import streamlit as st
from PIL import Image

# Initialize theme state in session state if it doesn't exist
if "theme" not in st.session_state:
    st.session_state["theme"] = "light"

# Function to toggle the theme
def toggle_theme():
    st.session_state["theme"] = "dark" if st.session_state["theme"] == "light" else "light"

# Display the toggle switch
st.sidebar.checkbox("Dark Mode", value=(st.session_state["theme"] == "dark"), on_change=toggle_theme)

# Define theme colors based on the current state (more modern gradients)
if st.session_state["theme"] == "light":
    primary_gradient_start = "#667eea"  # Mauve
    primary_gradient_end = "#764ba2"    # Plum
    secondary_gradient_start = "#fbc2eb" # Misty Rose
    secondary_gradient_end = "#a6c0ee"   # Steel Blue
    text_color = "#333333"            # Dark Gray
    accent_color = "#007bff"            # Blue
    content_background = "#f9f9f9"      # Light Gray
    button_bg = "linear-gradient(to right, #667eea, #764ba2)"
    button_text_color = "white"
else:
    primary_gradient_start = "#2c3e50"  # Dark Slate Gray
    primary_gradient_end = "#000000"    # Black
    secondary_gradient_start = "#37474f" # Darker Gray
    secondary_gradient_end = "#263238"   # Deep Gray
    text_color = "#ffffff"            # White
    accent_color = "#5bc0de"            # Cyan
    content_background = "#222222"      # Very Dark Gray
    button_bg = "linear-gradient(to right, #2c3e50, #000000)"
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
        background: rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        color: {text_color};
        padding: 1.5rem 1rem;
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
    .st-eb {{ /* Main content area */
        background-color: {content_background};
        padding: 2rem;
        border-radius: 12px;
        color: {text_color};
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }}
    .css-1adrpsg {{ /* Bold markdown text */
        font-weight: bold;
        color: {text_color};
    }}
    .stDownloadButton > button {{
        background: {button_bg};
        color: {button_text_color};
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        cursor: pointer;
        transition: opacity 0.2s ease-in-out;
    }}
    .stDownloadButton > button:hover {{
        opacity: 0.8;
    }}
    a {{ /* Links */
        color: {accent_color};
        text-decoration: none;
        transition: color 0.2s ease-in-out;
    }}
    a:hover {{
        color: lighten({accent_color}, 20%);
    }}
    div[data-testid="stMarkdownContainer"] > p {{
        color: {text_color};
        line-height: 1.6; /* Improve readability */
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

st.download_button(label="📄 **Download My Resume**",
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

# Skills
st.header("**🛠️ Skills**")
st.markdown("""
- **Programming:** **Python**, **R**, **SAS**
- **Libraries:** **Pandas**, **NumPy**, **Seaborn**, **Matplotlib**, **Scikit-learn**
- **Tools:** **Power BI**, **Tableau**, **Excel**, **SQL**
- **Others:** **Machine Learning**, **Data Wrangling**, **Predictive Modeling**
""", True)

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

# Certifications
st.header("**📜 Certifications**")
st.markdown("""
- **Google Professional Data Analytics** – Coursera
- **SAS Certified Specialist** – Base Programming
- **GenAI** – Kaggle
""", True)

# Languages
st.header("**🗣️ Languages**")
st.markdown("""
- **English**, **Hindi**, **Telugu**, German (Basic)
""", True)
