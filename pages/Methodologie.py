import streamlit as st

# Configuration
st.set_page_config(
    page_title="Méthodologie | EcoImpact",
    layout="wide",
    page_icon="📊"
)

# ========== CSS COPIÉ DE MAIN.PY ==========
st.markdown("""
    <style>
        .stApp {
            background-color: #F3F3F1;
            min-height: 100vh;
        }
        .navbar {
            position: fixed;
            top: 0;
            right: 0;
            left: 0;
            background-color: transparent;
            padding: 15px 20px;
            text-align: right;
            z-index: 1000;
            box-shadow: none;
        }
        .navbar a {
            color: black;
            text-decoration: none;
            font-size: 20px;
            font-weight: bold;
            margin: 0 15px;
        }
        .navbar a:hover {
            color: #4CAF50;
        }
        .content-behind {
            margin-top: 70px;
        }
        header {visibility: hidden;}
        /* Ajout pour forcer les titres en noir */
        h1 {
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)

# ========== BARRE DE NAVIGATION IDENTIQUE À MAIN.PY ==========
st.markdown("""
    <div class="navbar">
        <a href="/" target="_self">Accueil</a>
        <a href="/Calculateur" target="_self">Calculateur</a>
        <a href="/Ressources" target="_self">Ressources</a>
        <a href="/Methodologie" target="_self" style="color: #4CAF50; font-weight: bolder;">Méthodologie</a>
    </div>
    <div class="content-behind">
""", unsafe_allow_html=True)

# Contenu
st.title("📊 Méthodologie Scientifique")
# Votre contenu ici...

st.markdown("</div>", unsafe_allow_html=True)
