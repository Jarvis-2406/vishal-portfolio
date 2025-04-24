import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Vishal Anand Portfolio", layout="wide")

# Header
st.title("👋 Hey, I'm Vishal Anand")
# Load and display image
image = Image.open("vishal.jpg")
st.image(image, width=200, caption="Vishal Anand")
st.markdown("### Data Analyst | Business Intelligence | ML Enthusiast")

# Sidebar
st.sidebar.header("Contact")
st.sidebar.markdown("[📧 anand24061998@gmail.com](mailto:anand24061998@gmail.com)")
st.sidebar.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/vishal-anand2404/)")
st.sidebar.markdown("[💻 GitHub](https://github.com/Jarvis-2406)")

with open("Vishal_Anand_Resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="📄 Download My Resume",
                   data=PDFbyte,
                   file_name="Vishal_Anand_Resume.pdf",
                   mime='application/octet-stream')

# About Me
st.header("🧑‍💼 About Me")
st.write("""
Hello! I'm Vishal, a detail-oriented analyst with a passion for data and machine learning. 
I've helped HSBC and BYJUS streamline operations with analytics, and built tools like a 
financial audit assistant powered by AI.
""")

# Skills
st.header("🛠️ Skills")
st.markdown("""
- **Programming:** Python, R, SAS  
- **Libraries:** Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn  
- **Tools:** Power BI, Tableau, Excel, SQL  
- **Others:** Machine Learning, Data Wrangling, Predictive Modeling
""")

# Experience
st.header("💼 Experience")
st.subheader("HSBC — Contact Centre Executive (Nov 2022 - Nov 2024)")
st.markdown("""
- Built real-time dashboards to monitor service performance  
- Used SQL & Power BI to improve fraud detection  
- Led data reporting for operational efficiency
""")

st.subheader("BYJUS — Business Development Associate (Dec 2020 - Sep 2022)")
st.markdown("""
- Analyzed sales data using SQL  
- Created dashboards with Tableau & Google Analytics  
- Boosted conversion via data-driven lead segmentation
""")

# Projects
st.header("📁 Projects")
st.subheader("1. AI-powered Financial Audit Assistant")
st.markdown("""
- Automated document search using LangChain & OpenAI  
- Implemented FAISS for fast retrieval  
[🔗 GitHub Repo](https://github.com/Jarvis-2406/GenAI-for-Financial-Audits)
""")

st.subheader("2. Gold Price Prediction")
st.markdown("""
- Built predictive ML model with XGBoost  
- EDA using Pandas & Seaborn  
""")

st.subheader("3. BellaBeat Data Insights")
st.markdown("""
- Performed EDA on smart device data  
- Visualized findings with Tableau  
[🔗 GitHub Repo](https://github.com/Jarvis-2406/BellaBeat-Data-Insights)
""")

# Certifications
st.header("📜 Certifications")
st.markdown("""
- Google Professional Data Analytics – Coursera  
- SAS Certified Specialist – Base Programming  
- GenAI – Kaggle  
""")

# Languages
st.header("🗣️ Languages")
st.markdown("""
- English, Hindi, Telugu, German (Basic)
""")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")
