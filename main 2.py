import streamlit as st

# Configuration de la page
st.set_page_config(page_title="EcoImpact", layout="wide")

# Style CSS complet
st.markdown("""
    <style>
        .stApp {
            background: #F3F3F1 url('https://images.unsplash.com/photo-1514995669114-6081e934b693?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat left top / 65% auto;
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
            position: relative;
            z-index: 0;
            margin-top: 70px;
        }
        .welcome-text {
            color: black;
            text-align: right;
            font-size: 24px;
            margin-right: 20px;
        }
        .calculator-banner {
            background-color: white;
            padding: 25px;
            border-radius: 0;
            width: 100vw;
            margin: 20px 0;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
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

# Bandeau de navigation
st.markdown("""
    <div class="navbar">
        <a href="/" target="_self" style="color: #4CAF50; font-weight: bolder;">Accueil</a>
        <a href="/Calculateur" target="_self">Calculateur</a>
        <a href="/Ressources" target="_self">Ressources</a>
        <a href="/Methodologie" target="_self">Méthodologie</a>
    </div>
""", unsafe_allow_html=True)

# Contenu de la page d'accueil
st.markdown('<div class="content-behind">', unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])
with col2:
    st.image("Logo.jpg", width=300)

st.markdown("""
    <div class="welcome-text">
        <h1>Bienvenue sur EcoImpact</h1>
        <p>Découvrez votre impact environnemental avec notre calculateur personnalisé.</p>
    </div>
""", unsafe_allow_html=True)

# Bannière calculateur
st.markdown("""
    <div style="padding-bottom: 100px;">
        <div class="calculator-banner">
            <div class="calculator-title">Tester le calculateur</div>
            <a href="/Calculateur" target="_self">
                <button class="start-button">Start</button>
            </a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer-banner">
        <a href="/A_propos" target="_self">À propos</a>
        <img src="unilasalle_beauvais_logo.jpg" alt="Logo UniLaSalle Beauvais">
    </div>
""", unsafe_allow_html=True)
