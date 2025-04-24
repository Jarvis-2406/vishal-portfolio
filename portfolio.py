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

# Define theme colors based on the current state
if st.session_state["theme"] == "light":
    gradient_start = "magenta"
    gradient_mid1 = "white"
    gradient_mid2 = "orange"
    gradient_end = "red"
    text_color = "#191970"        # Midnight Blue
    content_background = "#f5f5dc" # Beige
    button_bg = "linear-gradient(to right, magenta, white, orange, red)"
    button_text_color = "black"
else:
    gradient_start = "#8B008B"  # Dark Magenta
    gradient_mid1 = "#333333"  # Dark Gray
    gradient_mid2 = "#FF8C00"  # Dark Orange
    gradient_end = "#8B0000"    # Dark Red
    text_color = "#ffffff"        # White
    content_background = "#444444" # Slightly lighter dark gray
    button_bg = "linear-gradient(to right, #8B008B, #333333, #FF8C00, #8B0000)"
    button_text_color = "white"

# Custom Theme Configuration
st.markdown(
    f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(to bottom right, {gradient_start}, {gradient_mid1}, {gradient_mid2}, {gradient_end});
        color: {text_color};
        min-height: 100vh; /* Ensure full viewport height for gradient */
    }}
    [data-testid="stHeader"] {{
        background: rgba(255, 255, 255, 0.1); /* Semi-transparent white for header */
        backdrop-filter: blur(10px); /* Add a blur effect */
        color: {text_color};
        padding: 1rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.2);
    }}
    [data-testid="stSidebar"] {{
        background: rgba(255, 255, 255, 0.05); /* Very subtle white for sidebar */
        backdrop-filter: blur(5px);
        color: {text_color};
        padding: 1rem;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
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
    .stDownloadButton > button {{
        background: {button_bg};
        color: {button_text_color};
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        cursor: pointer;
    }}
    .stDownloadButton > button:hover {{
        opacity: 0.8;
    }}
    a {{ /* Style for links */
        color: #ADD8E6; /* Light Sky Blue for links */
    }}
    a:visited {{
        color: #8A2BE2; /* Blue Violet for visited links */
    }}
    a:hover {{
        color: #00FFFF; /* Cyan for hovered links */
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
Hi, I’m Vishal Anand, an aspiring data professional passionate about using data to solve problems and drive insights. 
With skills in SQL, Python, Excel, and data visualization, I enjoy analyzing and presenting data to help organizations make informed decisions. 
Outside of data, I love cooking, traveling, and listening to podcasts. I’m excited to grow in this field and contribute to data-driven solutions.
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
