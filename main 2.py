import streamlit as st

# Configuration de la page
st.set_page_config(page_title="EcoImpact", layout="wide")

# Style CSS avec fond d'écran et navbar transparente du premier code
st.markdown("""
    <style>
        /* Style pour le fond d'écran (du premier code) */
        .stApp {
            background: #F3F3F1 url('https://images.unsplash.com/photo-1514995669114-6081e934b693?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat left top / 65% auto;
            min-height: 100vh;
        }
        
        /* Navbar transparente (du premier code) */
        .navbar {
            position: fixed;
            top: 0;
            right: 0;
            left: 0;
            background: transparent !important;
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
        
        /* Logo positionnement (du second code) */
        .logo-fixed {
            position: fixed;
            top: 70px;
            left: 20px;
            z-index: 999;
            width: 300px;
        }
        
        /* Contenu principal (du second code) */
        .main-content {
            padding-top: 120px;
            position: relative;
            z-index: 1;
        }
        
        /* Footer (du second code) */
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background: #23A95C;
            color: white;
            padding: 10px 20px;
            z-index: 1001;
        }
        
        /* Styles pour la bannière calculateur (du second code) */
        .calculator-banner {
            background: white;
            padding: 25px;
            border-radius: 8px;
            margin: 20px 0;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Barre de navigation (ordre des liens du premier code)
st.markdown("""
    <div class="navbar">
        <a href="/">Accueil</a>
        <a href="/calculateur">Calculateur</a>
        <a href="/ressources">Ressources</a>
        <a href="/methodologie">Méthodologie</a>
    </div>
    
    <!-- Logo (du second code) -->
    <img class="logo-fixed" src="Logo.jpg" alt="Logo EcoImpact">
""", unsafe_allow_html=True)

# Contenu principal (du second code)
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Texte "Bienvenue" (du second code)
st.markdown("""
    <div style="text-align: right; padding-right: 20px;">
        <h1>Bienvenue sur EcoImpact</h1>
        <p>Votre plateforme d'analyse environnementale</p>
    </div>
""", unsafe_allow_html=True)

# Bannière calculateur (du second code)
st.markdown("""
    <div class="calculator-banner">
        <h3 style="text-align: center;">Tester le calculateur</h3>
        <div style="text-align: center;">
            <button style="
                background: #23A95C;
                color: white;
                border: none;
                padding: 12px 30px;
                border-radius: 25px;
                font-size: 16px;
                cursor: pointer;
                transition: background 0.3s;
            " onmouseover="this.style.background='#1e8c4f'" 
            onmouseout="this.style.background='#23A95C'">Commencer</button>
        </div>
    </div>
""", unsafe_allow_html=True)

# Footer (du second code)
st.markdown("""
    <div class="footer">
        <span>À propos</span>
        <img src="unilasalle_beauvais_logo.jpg" style="height: 40px; float: right;">
    </div>
""", unsafe_allow_html=True)

# Fermeture de la div main-content
st.markdown('</div>', unsafe_allow_html=True)
