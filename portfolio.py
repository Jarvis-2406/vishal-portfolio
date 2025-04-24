import streamlit as st
from PIL import Image

# Initialize theme state in session state if it doesn't exist
if "theme" not in st.session_state:
    st.session_state["theme"] = "light"

# Function to toggle the theme
def toggle_theme():
    st.session_state["theme"] = "dark" if st.session_state["theme"] == "light" else "light"

# Display the toggle button
st.sidebar.button("Toggle Theme", on_click=toggle_theme)

# Define theme colors based on the current state
if st.session_state["theme"] == "light":
    background_color = "#f0f8ff"  # Light Blue
    header_color = "#ADD8E6"      # Light Sky Blue
    sidebar_color = "#E0FFFF"     # Light Cyan
    text_color = "#191970"        # Midnight Blue
    content_background = "#f5f5dc" # Beige
else:
    background_color = "#1e1e1e"  # Dark Gray
    header_color = "#333333"      # Darker Gray
    sidebar_color = "#222222"     # Even Darker Gray
    text_color = "#ffffff"        # White
    content_background = "#444444" # Slightly lighter dark gray

# Custom Theme Configuration
st.markdown(
    f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-color: {background_color};
        color: {text_color};
    }}
    [data-testid="stHeader"] {{
        background-color: {header_color};
        color: {text_color};
    }}
    [data-testid="stSidebar"] {{
        background-color: {sidebar_color};
        color: {text_color};
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: {text_color};
    }}
    .st-eb {{ /* Style for the main content area */
        background-color: {content_background};
        padding: 20px;
        border-radius: 10px;
        color: {text_color}; /* Ensure text in content area is also themed */
    }}
    .css-1adrpsg {{ /* Style for markdown text to make it bold */
        font-weight: bold;
        color: {text_color}; /* Ensure bold text is also themed */
    }}
    .stDownloadButton {{
        color: {text_color};
        border-color: {text_color};
    }}
    .stDownloadButton:hover {{
        background-color: {header_color};
        color: {text_color};
    }}
    a {{ /* Style for links */
        color: #007bff; /* Default link color */
    }}
    a:visited {{
        color: #663ab7; /* Visited link color */
    }}
    a:hover {{
        color: #0056b3; /* Hovered link color */
    }}
    div[data-testid="stMarkdownContainer"] > p {{
        color: {text_color};
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.title(f"👋 Hey, I'm **Vishal Anand**")
# Load and display image
image = Image.open("vishal.jpg")
st.image(image, width=200, caption="Vishal Anand")
st.markdown(f"### **Data Analyst | Business Intelligence | ML Enthusiast**")

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

# About Me
st.header("**🧑‍💼 About Me**")
st.write("""
Hello! I'm Vishal, a detail-oriented analyst with a passion for data and machine learning.
I've helped HSBC and BYJUS streamline operations with analytics, and built tools like a
financial audit assistant powered by AI.
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
