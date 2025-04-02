import streamlit as st

# Configuration de la page (identique à l'original)
st.set_page_config(page_title="EcoImpact", layout="wide")

# Style CSS original avec UNIQUEMENT la navbar rendue transparente
st.markdown("""
    <style>
        /* Style pour le fond d'écran (identique) */
        .stApp {
            background: #F3F3F1 url('https://images.unsplash.com/photo-1514995669114-6081e934b693?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat left top / 65% auto;
            min-height: 100vh;
        }
        
        /* Navbar rendue transparente (SEUL CHANGEMENT : background: transparent) */
        .navbar {
            position: fixed;
            top: 0;
            right: 0;
            left: 0;
            background: transparent !important;  /* UNIQUE MODIFICATION */
            padding: 15px 20px;
            text-align: right;
            z-index: 1000;
            height: 60px;
        }
        
        /* Tout le reste du CSS original est conservé */
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
        
        .logo-fixed {
            position: fixed;
            top: 70px;
            left: 20px;
            z-index: 999;
            width: 300px;
        }
        
        .content {
            padding-top: 80px;
            color: black;
        }
        
        .calculator-banner {
            background-color: white;
            padding: 25px;
            border-radius: 10px;
            width: 100%;
            margin: 20px 0;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        .calculator-title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 15px;
            color: #333;
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
            z-index: 1001;
        }
        
        .footer-banner a {
            color: white;
            text-decoration: none;
            font-size: 20px;
            font-weight: bold;
        }
        
        .footer-banner a:hover {
            color: #F3F3F1;
        }
        
        .footer-banner img {
            height: 40px;
            margin-left: auto;
        }
        
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Barre de navigation (identique à l'original)
st.markdown("""
    <div class="navbar">
        <a href="/">Accueil</a>
        <a href="/methodologie">Méthodologie</a>
        <a href="/ressources">Ressources</a>
    </div>
""", unsafe_allow_html=True)

# Logo (identique à l'original)
st.markdown("""
    <img class="logo-fixed" src="Logo.jpg" alt="Logo EcoImpact">
""", unsafe_allow_html=True)

# Contenu principal (identique à l'original)
st.markdown('<div class="content">', unsafe_allow_html=True)

# Gestion des pages (identique à l'original)
page = st.query_params.get("page", ["home"])[0]

if page == "home":
    st.markdown("""
        <div style="text-align: right; padding-right: 20px;">
            <h1>Bienvenue sur EcoImpact</h1>
            <p>Ceci est la page d'accueil de notre projet.</p>
        </div>
    """, unsafe_allow_html=True)

    # Bannière calculateur (identique à l'original)
    st.markdown("""
        <div style="padding-bottom: 100px;">
            <div class="calculator-banner">
                <div class="calculator-title">Tester le calculateur</div>
                <button class="start-button">Start</button>
            </div>
        </div>
    """, unsafe_allow_html=True)

elif page == "methodologie":
    st.title("Méthodologie")
    st.write("Cette page présente la méthodologie utilisée dans notre projet.")

elif page == "ressources":
    st.title("Ressources")
    st.write("Cette page contient des ressources utiles pour notre projet.")

# Footer (identique à l'original)
st.markdown("""
    <div class="footer-banner">
        <a href="/a_propos">À propos</a>
        <img src="unilasalle_beauvais_logo.jpg" alt="Logo UniLaSalle Beauvais">
    </div>
""", unsafe_allow_html=True)

# Fermeture de la div content (identique à l'original)
st.markdown('</div>', unsafe_allow_html=True)
