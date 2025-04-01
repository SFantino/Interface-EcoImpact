import streamlit as st

# Configuration de la page
st.set_page_config(page_title="EcoImpact", layout="wide")

# Style CSS
st.markdown("""
    <style>
        /* Fond d'écran */
        .stApp {
            background: #F3F3F1;
            min-height: 100vh;
        }
        
        /* Image de fond */
        .background-image {
            position: absolute;
            left: 0;
            top: 0;
            width: 60%;
            height: 300px;
            background: url('https://images.unsplash.com/photo-1514995669114-6081e934b693?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat left top;
            background-size: cover;
            z-index: 0;
        }
        
        /* Navigation */
        .navbar {
            position: fixed;
            top: 0;
            right: 0;
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
        
        /* Conteneur principal */
        .main-container {
            position: relative;
            z-index: 1;
            padding-top: 80px;
        }
        
        /* Colonnes */
        .columns-container {
            display: flex;
            width: 100%;
        }
        .left-column {
            flex: 3;
            padding-right: 40px;
        }
        .right-column {
            flex: 1;
        }
        
        /* Calculator Banner */
        .calculator-banner {
            background: white;
            padding: 25px;
            border-radius: 10px;
            margin-top: 30px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .start-button {
            background-color: #23A95C;
            color: white;
            border: none;
            padding: 12px 30px;
            font-size: 18px;
            border-radius: 50px;
            cursor: pointer;
        }
        
        /* Footer */
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background: #23A95C;
            padding: 10px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
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
    
    <div class="background-image"></div>
""", unsafe_allow_html=True)

# Contenu principal
st.markdown("""
    <div class="main-container">
        <div class="columns-container">
            <div class="left-column">
                <h1>Bienvenue sur EcoImpact</h1>
                <p>Ceci est la page d'accueil de notre projet.</p>
                
                <div class="calculator-banner">
                    <div style="font-size: 24px; font-weight: bold; margin-bottom: 15px;">Tester le calculateur</div>
                    <button class="start-button">Start</button>
                </div>
            </div>
            
            <div class="right-column">
                <img src="Logo.jpg" width="100%">
            </div>
        </div>
    </div>
    
    <div class="footer">
        <a href="/a_propos" style="color: white; text-decoration: none; font-weight: bold;">À propos</a>
        <img src="unilasalle_beauvais_logo.jpg" height="40">
    </div>
""", unsafe_allow_html=True)
