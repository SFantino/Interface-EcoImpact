import streamlit as st

# Configuration de base
st.set_page_config(page_title="EcoImpact", layout="wide")

# Style CSS avec navbar transparente
st.markdown("""
    <style>
        /* Fond d'écran fixe */
        .stApp {
            background: 
                #F3F3F1 url('https://images.unsplash.com/photo-1514995669114-6081e934b693?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') 
                no-repeat left top / 65% auto;
            min-height: 100vh;
        }
        
        /* Barre de navigation transparente */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: transparent;
            padding: 20px 40px;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            z-index: 1000;
            height: 60px;
        }
        
        /* Style des liens */
        .nav-link {
            color: black;
            text-decoration: none;
            font-size: 18px;
            font-weight: 600;
            margin-right: 30px;
            transition: color 0.3s;
            text-shadow: 0 0 2px rgba(255,255,255,0.5);
        }
        .nav-link:hover {
            color: #23A95C;
        }
        
        /* Logo positionné */
        .logo-fixed {
            position: fixed;
            top: 80px;
            left: 40px;
            z-index: 999;
            width: 250px;
        }
        
        /* Contenu principal */
        .main-content {
            padding-top: 120px;
            position: relative;
            z-index: 1;
        }
        
        /* Footer */
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background: #23A95C;
            color: white;
            padding: 12px 40px;
            z-index: 1001;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        /* Cacher les éléments par défaut */
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Structure HTML
st.markdown("""
    <!-- Barre de navigation transparente -->
    <div class="navbar">
        <a href="/" class="nav-link">Accueil</a>
        <a href="/calculateur" class="nav-link">Calculateur</a>
        <a href="/ressources" class="nav-link">Ressources</a>
        <a href="/methodologie" class="nav-link">Méthodologie</a>
    </div>
    
    <!-- Logo -->
    <img class="logo-fixed" src="Logo.jpg" alt="Logo EcoImpact">
""", unsafe_allow_html=True)

# Zone de contenu principal
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# --- VOTRE CONTENU ICI ---
st.markdown("""
    <div style="text-align: right; padding-right: 40px;">
        <h1 style="color: black;">Bienvenue sur EcoImpact</h1>
        <p style="color: black; font-size: 18px;">Votre plateforme d'analyse environnementale</p>
    </div>
""", unsafe_allow_html=True)

# Bannière calculateur
st.markdown("""
    <div style="
        padding: 30px; 
        background: white; 
        border-radius: 10px; 
        margin: 40px auto;
        max-width: 800px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    ">
        <h3 style="text-align: center; margin-bottom: 20px;">Accéder au calculateur d'impact</h3>
        <div style="text-align: center;">
            <button style="
                background: #23A95C;
                color: white;
                border: none;
                padding: 12px 30px;
                border-radius: 30px;
                font-size: 16px;
                cursor: pointer;
                transition: background 0.3s;
            " onmouseover="this.style.background='#1e8c4f'" 
            onmouseout="this.style.background='#23A95C'">Commencer l'analyse</button>
        </div>
    </div>
""", unsafe_allow_html=True)
# --- FIN DE VOTRE CONTENU ---

# Footer
st.markdown("""
    <div class="footer">
        <a href="/a_propos" style="color: white; text-decoration: none;">À propos</a>
        <img src="unilasalle_beauvais_logo.jpg" style="height: 40px;">
    </div>
""", unsafe_allow_html=True)

# Fermeture de la div main-content
st.markdown('</div>', unsafe_allow_html=True)
