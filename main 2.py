import streamlit as st

# Configuration de la page (inchangée)
st.set_page_config(page_title="EcoImpact", layout="wide")

# Style CSS (seule modification: background: transparent)
st.markdown("""
    <style>
        /* Style pour le fond d'écran */
        .stApp {
            background: #F3F3F1 url('https://images.unsplash.com/photo-1514995669114-6081e934b693?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat left top / 65% auto;
            min-height: 100vh;
        }
        
        /* SEULE MODIFICATION ICI : background: transparent */
        .navbar {
            position: fixed;
            top: 0;
            right: 0;
            left: 0;
            background: transparent !important;  /* Changement ici */
            padding: 15px 20px;
            text-align: right;
            z-index: 1000;
            height: 60px;
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
        
        /* Logo (inchangé) */
        .logo-fixed {
            position: fixed;
            top: 70px;
            left: 20px;
            z-index: 999;
            width: 300px;
        }
        
        /* Contenu (inchangé) */
        .content {
            padding-top: 80px;
            color: black;
        }
        
        /* Footer (inchangé) */
        .footer-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #23A95C;
            padding: 10px 20px;
            z-index: 1001;
        }
        
        /* Masquer éléments Streamlit (inchangé) */
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Barre de navigation (ordre des liens inchangé)
st.markdown("""
    <div class="navbar">
        <a href="/">Accueil</a>
        <a href="/calculateur">Calculateur</a>  <!-- Seul changement: texte du lien -->
        <a href="/ressources">Ressources</a>
        <a href="/methodologie">Méthodologie</a>
    </div>
    
    <!-- Logo (inchangé) -->
    <img class="logo-fixed" src="Logo.jpg">
""", unsafe_allow_html=True)

# Contenu principal (inchangé)
st.markdown('<div class="content">', unsafe_allow_html=True)
# ... (votre contenu existant) ...

# Footer (inchangé)
st.markdown("""
    <div class="footer-banner">
        <a href="/a_propos" style="color: white; text-decoration: none;">À propos</a>
        <img src="unilasalle_beauvais_logo.jpg" style="height: 40px; float: right;">
    </div>
""", unsafe_allow_html=True)
