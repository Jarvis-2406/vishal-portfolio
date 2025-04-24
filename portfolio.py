import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Vishal Anand Portfolio", layout="wide")

# Custom Theme Configuration
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #f0f8ff; /* Light Blue background */
    }
    [data-testid="stHeader"] {
        background-color: #ADD8E6; /* Light Sky Blue header */
    }
    [data-testid="stSidebar"] {
        background-color: #E0FFFF; /* Light Cyan sidebar */
    }
    h1, h2, h3, h4, h5, h6 {
        color: #191970; /* Midnight Blue text for headings */
    }
    .st-eb { /* Style for the main content area */
        background-color: #f5f5dc; /* Beige background for content */
        padding: 20px;
        border-radius: 10px;
    }
    .css-1adrpsg { /* Style for markdown text to make it bold */
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.title("👋 Hey, I'm **Vishal Anand**") # Made name bold
# Load and display image
image = Image.open("vishal.jpg")
st.image(image, width=200, caption="Vishal Anand")
st.markdown("### **Data Analyst | Business Intelligence | ML Enthusiast**", True) # Made title bold

# Sidebar
st.sidebar.header("**Contact**") # Made header bold
st.sidebar.markdown("[📧 anand24061998@gmail.com](mailto:anand24061998@gmail.com)")
st.sidebar.markdown("[🔗 **LinkedIn**](https://www.linkedin.com/in/vishal-anand2404/)") # Made link text bold
st.sidebar.markdown("[💻 **GitHub**](https://github.com/Jarvis-2406)") # Made link text bold

with open("Vishal Anand .pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="📄 **Download My Resume**", # Made button text bold
                    data=PDFbyte,
                    file_name="Vishal Anand .pdf",
                    mime='application/octet-stream')

# About Me
st.header("**🧑‍💼 About Me**") # Made header bold
st.write("""
Hello! I'm Vishal, a detail-oriented analyst with a passion for data and machine learning.
I've helped HSBC and BYJUS streamline operations with analytics, and built tools like a
financial audit assistant powered by AI.
""")

# Skills
st.header("**🛠️ Skills**") # Made header bold
st.markdown("""
- **Programming:** **Python**, **R**, **SAS**
- **Libraries:** **Pandas**, **NumPy**, **Seaborn**, **Matplotlib**, **Scikit-learn**
- **Tools:** **Power BI**, **Tableau**, **Excel**, **SQL**
- **Others:** **Machine Learning**, **Data Wrangling**, **Predictive Modeling**
""", True) # Applied bold using markdown

# Experience
st.header("**💼 Experience**") # Made header bold
st.subheader("**HSBC — Contact Centre Executive (Nov 2022 - Nov 2024)**") # Made subheader bold
st.markdown("""
- Built real-time dashboards to monitor service performance
- Used SQL & Power BI to improve fraud detection
- Led data reporting for operational efficiency
""", True) # Applied bold using markdown

st.subheader("**BYJUS — Business Development Associate (Dec 2020 - Sep 2022)**") # Made subheader bold
st.markdown("""
- Analyzed sales data using SQL
- Created dashboards with Tableau & Google Analytics
- Boosted conversion via data-driven lead segmentation
""", True) # Applied bold using markdown

# Projects
st.header("**📁 Projects**") # Made header bold
st.subheader("**1. AI-powered Financial Audit Assistant**") # Made subheader bold
st.markdown("""
- Automated document search using LangChain & OpenAI
- Implemented FAISS for fast retrieval
[🔗 **GitHub Repo**](https://github.com/Jarvis-2406/GenAI-for-Financial-Audits)
""", True) # Applied bold using markdown

st.subheader("**2. Gold Price Prediction**") # Made subheader bold
st.markdown("""
- Built predictive ML model with XGBoost
- EDA using Pandas & Seaborn
[🔗 **GitHub Repo**](https://github.com/Jarvis-2406/Gold-Price-Prediction)
""", True) # Applied bold using markdown

st.subheader("**3. BellaBeat Data Insights**") # Made subheader bold
st.markdown("""
- Performed EDA on smart device data
- Visualized findings with Tableau
[🔗 **GitHub Repo**](https://github.com/Jarvis-2406/BellaBeat-Data-Insights)
""", True) # Applied bold using markdown

# Certifications
st.header("**📜 Certifications**") # Made header bold
st.markdown("""
- **Google Professional Data Analytics** – Coursera
- **SAS Certified Specialist** – Base Programming
- **GenAI** – Kaggle
""", True) # Applied bold using markdown

# Languages
st.header("**🗣️ Languages**") # Made header bold
st.markdown("""
- **English**, **Hindi**, **Telugu**, German (Basic)
""", True) # Applied bold using markdown
