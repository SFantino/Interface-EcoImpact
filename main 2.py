import streamlit as st

# Configuration de la page
st.set_page_config(page_title="EcoImpact", layout="wide")

# Style CSS
st.markdown("""
    <style>
        /* Fond d'écran */
        .stApp {
            background: #F3F3F1 url('https://images.unsplash.com/photo-1514995669114-6081e934b693?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat left top / 60% auto;
            min-height: 100vh;
        }
        
        /* Navigation */
        .navbar {
            position: fixed;
            top: 0;
            right: 0;
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
        .navbar a:hover {
            color: #4CAF50;
        }
        
        /* Contenu principal */
        .main-content {
            padding: 120px 40px 40px;
            position: relative;
        }
        .welcome-text {
            color: black;
            margin-bottom: 40px;
        }
        
        /* Calculator Banner */
        .calculator-banner {
            background-color: white;
            padding: 25px;
            border-radius: 10px;
            width: 100%;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .calculator-title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 15px;
        }
        .start-button {
            background-color: #23A95C;
            color: white;
            border: none;
            padding: 12px 30px;
            font-size: 18px;
            border-radius: 50px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .start-button:hover {
            background-color: #1e8c4f;
        }
        
        /* Logo */
        .logo-container {
            position: absolute;
            top: 100px;
            right: 40px;
            z-index: 2;
        }
        
        /* Footer */
        .footer-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #23A95C;
            padding: 10px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 1000;
        }
        .footer-banner a {
            color: white;
            text-decoration: none;
            font-size: 20px;
            font-weight: bold;
        }
        
        /* Masquer éléments par défaut */
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Barre de navigation
st.markdown("""
    <div class="navbar">
        <a href="/">Accueil</a>
        <a href="/methodologie">Méthodologie</a>
        <a href="/ressources">Ressources</a>
    </div>
""", unsafe_allow_html=True)

# Contenu principal
st.markdown("""
    <div class="main-content">
        <!-- Logo -->
        <div class="logo-container">
            <img src="Logo.jpg" width="300">
        </div>
        
        <!-- Contenu texte -->
        <div class="welcome-text">
            <h1>Bienvenue sur EcoImpact</h1>
            <p>Ceci est la page d'accueil de notre projet.</p>
        </div>
        
        <!-- Calculator Banner -->
        <div class="calculator-banner">
            <div class="calculator-title">Tester le calculateur</div>
            <button class="start-button">Start</button>
        </div>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer-banner">
        <a href="/a_propos">À propos</a>
        <img src="unilasalle_beauvais_logo.jpg" alt="Logo UniLaSalle Beauvais" height="40">
    </div>
""", unsafe_allow_html=True)
