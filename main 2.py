import streamlit as st

# Configuration de base
st.set_page_config(page_title="EcoImpact", layout="wide")

# Style CSS minimal et efficace
st.markdown("""
    <style>
        /* Fond d'écran fixe */
        .stApp {
            background: 
                #F3F3F1 url('https://images.unsplash.com/photo-1514995669114-6081e934b693?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') 
                no-repeat left top / 65% auto;
            min-height: 100vh;
        }
        
        /* Barre de navigation fixe */
        .navbar {
            position: fixed;
            top: 0;
            right: 0;
            left: 0;
            background: white;
            padding: 15px 20px;
            text-align: right;
            z-index: 1000;
            height: 60px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        /* Logo positionné sous la navbar */
        .logo-fixed {
            position: fixed;
            top: 70px;  /* 60px (navbar) + 10px marge */
            left: 20px;
            z-index: 999;
            width: 300px;
        }
        
        /* Contenu principal */
        .main-content {
            padding-top: 120px;  /* Espace pour navbar + logo */
            position: relative;
            z-index: 1;
        }
        
        /* Footer fixe */
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
        
        /* Cacher les éléments par défaut */
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Structure HTML de base
st.markdown("""
    <!-- Barre de navigation -->
    <div class="navbar">
        <a href="/">Accueil</a>
        <a href="/methodologie">Méthodologie</a>
        <a href="/ressources">Ressources</a>
    </div>
    
    <!-- Logo -->
    <img class="logo-fixed" src="Logo.jpg" alt="Logo EcoImpact">
""", unsafe_allow_html=True)

# Zone de contenu principal
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# --- VOTRE CONTENU ICI ---
st.markdown("""
    <div style="text-align: right; padding-right: 20px;">
        <h1>Bienvenue sur EcoImpact</h1>
        <p>Votre plateforme d'analyse environnementale</p>
    </div>
""", unsafe_allow_html=True)

# Bannière calculateur
st.markdown("""
    <div style="padding: 25px; background: white; border-radius: 8px; margin: 20px 0;">
        <h3 style="text-align: center;">Tester le calculateur</h3>
        <div style="text-align: center;">
            <button style="
                background: #23A95C;
                color: white;
                border: none;
                padding: 10px 25px;
                border-radius: 25px;
                font-size: 16px;
                cursor: pointer;
            ">Commencer</button>
        </div>
    </div>
""", unsafe_allow_html=True)
# --- FIN DE VOTRE CONTENU ---

# Footer
st.markdown("""
    <div class="footer">
        <span>À propos</span>
        <img src="unilasalle_beauvais_logo.jpg" style="height: 40px; float: right;">
    </div>
""", unsafe_allow_html=True)

# Fermeture de la div main-content
st.markdown('</div>', unsafe_allow_html=True)
