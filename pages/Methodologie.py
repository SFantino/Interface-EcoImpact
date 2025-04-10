import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Méthodologie | EcoImpact", 
    layout="wide",
    page_icon="📊"
)

# CSS minimal
st.markdown("""
    <style>
        .stApp { background-color: #F3F3F1; }
        .navbar {
            position: fixed;
            top: 0;
            right: 0;
            left: 0;
            background-color: transparent;
            padding: 15px 20px;
            text-align: right;
            z-index: 1000;
        }
        .navbar a {
            color: black;
            text-decoration: none;
            font-size: 20px;
            font-weight: bold;
            margin: 0 15px;
        }
        .navbar a:hover { color: #4CAF50; }
        .content-behind { margin-top: 70px; }
    </style>
""", unsafe_allow_html=True)

# Barre de navigation
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
st.write("Contenu de votre méthodologie ici...")

st.markdown("</div>", unsafe_allow_html=True)
