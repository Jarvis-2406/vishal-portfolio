# portfolio.py
# -*- coding: utf-8 -*-
import streamlit as st
from PIL import Image
import os

# ---------- Theme toggle ----------
if "theme" not in st.session_state:
    st.session_state["theme"] = "light"

def toggle_theme():
    st.session_state["theme"] = "dark" if st.session_state["theme"] == "light" else "light"

# ---------- Theme colors ----------
if st.session_state["theme"] == "light":
    page_bg_start = "#f1f8f4"
    page_bg_end = "#eafaf0"
    skills_start = "#27ae60"
    skills_end = "#2ecc71"
    text_color = "#0b2a1a"
    card_bg = "#ffffff"
    card_text = "#173737"
    shadow = "rgba(18, 52, 42, 0.12)"
else:
    page_bg_start = "#0f1720"
    page_bg_end = "#071024"
    skills_start = "#0b3d91"
    skills_end = "#123b6a"
    text_color = "#e6f0ff"
    card_bg = "#091223"
    card_text = "#dfeeff"
    shadow = "rgba(0,0,0,0.6)"

# ---------- CSS + Font Awesome ----------
css = f"""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
/* Page background */
[data-testid="stAppViewContainer"] {{
  background: linear-gradient(180deg, {page_bg_start}, {page_bg_end});
  color: {text_color};
}}

/* Header / small layout tweaks */
h1, h2, h3, h4, h5 {{
  color: {text_color};
}}

/* Skills section container */
.skills-section {{
  width: 96%;
  max-width: 1100px;
  margin: 30px auto;
  padding: 28px;
  border-radius: 18px;
  background: linear-gradient(135deg, {skills_start}, {skills_end});
  box-shadow: 0 10px 30px {shadow};
  color: white;
}}

/* header row with icon */
.skills-header {{
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 18px;
}}
.skills-header .fa-tools {{
  font-size: 36px;
  opacity: 0.95;
  transform: translateY(1px);
}}

/* grid of cards */
.skills-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 18px;
}}

/* card */
.skill-card {{
  background: {card_bg};
  color: {card_text};
  padding: 18px;
  border-radius: 12px;
  min-height: 140px;
  box-shadow: 0 8px 18px rgba(0,0,0,0.12);
  transition: transform 0.28s cubic-bezier(.2,.8,.2,1), box-shadow 0.28s;
  display: flex;
  flex-direction: column;
  gap: 8px;
}}
.skill-card:hover {{
  transform: translateY(-10px) scale(1.02);
  box-shadow: 0 18px 42px rgba(0,0,0,0.20);
}}
.card-top {{
  display:flex;
  align-items:center;
  gap:12px;
}}
.card-icon {{
  width:48px;
  height:48px;
  border-radius:10px;
  display:flex;
  align-items:center;
  justify-content:center;
  background: linear-gradient(180deg, rgba(0,0,0,0.03), rgba(0,0,0,0.05));
  font-size: 22px;
}}
.skill-title {{
  font-weight:700;
  font-size: 1.02rem;
}}
.skill-list {{
  margin-top: 6px;
  font-size: 0.98rem;
  line-height: 1.45;
  color: {card_text};
}}
@media (max-width:600px) {{
  .skills-section {{ padding: 18px; border-radius:12px; }}
  .card-icon {{ width:42px; height:42px; font-size:18px; }}
}}
</style>
"""

# inject CSS
st.markdown(css, unsafe_allow_html=True)

# ---------- Page header ----------
st.title("👋 Hey — I'm Vishal Anand")
st.caption("Aspiring Data Professional")
st.button("Toggle theme 🌙", on_click=toggle_theme, key="theme_toggle_btn")

# ---------- Profile image (optional) ----------
col1, col2 = st.columns([1, 3])
with col1:
    try:
        if os.path.exists("vishal.jpg"):
            img = Image.open("vishal.jpg")
            st.image(img, width=160, caption="Vishal Anand")
        else:
            st.image("https://via.placeholder.com/160x160.png?text=Avatar", width=160)
    except Exception:
        st.image("https://via.placeholder.com/160x160.png?text=Avatar", width=160)

with col2:
    st.markdown("""
    **About me**  
    Data enthusiast with hands-on experience in SQL, Python, Power BI, and building ML pipelines.  
    I enjoy transforming messy data into clear, actionable insights.
    """)

# ---------- Skills section (HTML inside Python string) ----------
skills_html = """
<div class="skills-section" role="region" aria-label="Skills">
  <div class="skills-header">
    <i class="fas fa-tools" aria-hidden="true"></i>
    <h2 style="margin:0; font-size:28px; font-weight:700;">Skills</h2>
  </div>

  <div class="skills-grid">

    <div class="skill-card" aria-label="Programming">
      <div class="card-top">
        <div class="card-icon"><i class="fab fa-python" title="Python"></i></div>
        <div class="skill-title">Programming</div>
      </div>
      <div class="skill-list">
        Python (Pandas, NumPy, Matplotlib, Seaborn)<br>
        R<br>
        SAS
      </div>
    </div>

    <div class="skill-card" aria-label="Data Analysis">
      <div class="card-top">
        <div class="card-icon"><i class="fas fa-database" title="Data"></i></div>
        <div class="skill-title">Data Analysis</div>
      </div>
      <div class="skill-list">
        Excel (PivotTables, Power Query, DAX)<br>
        SQL (Joins, Aggregations, Subqueries)
      </div>
    </div>

    <div class="skill-card" aria-label="Visualization">
      <div class="card-top">
        <div class="card-icon"><i class="fas fa-chart-bar" title="Charts"></i></div>
        <div class="skill-title">Visualization</div>
      </div>
      <div class="skill-list">
        Tableau<br>
        Power BI
      </div>
    </div>

    <div class="skill-card" aria-label="Machine Learning">
      <div class="card-top">
        <div class="card-icon"><i class="fas fa-robot" title="ML"></i></div>
        <div class="skill-title">Machine Learning</div>
      </div>
      <div class="skill-list">
        Predictive Modeling<br>
        Data Mining
      </div>
    </div>

  </div>
</div>
"""

st.markdown(skills_html, unsafe_allow_html=True)

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
