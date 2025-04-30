import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="EcoImpact",
    layout="wide",
    page_icon="🌱",
    initial_sidebar_state="collapsed"  # Désactive le sidebar par défaut
)

# ========== CSS MODIFIÉ ==========
st.markdown("""
    <style>   
        /* Navbar horizontale fixe */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 70px;
            background-color: #F3F3F1 !important;
            padding: 15px 20px;
            z-index: 1000;
            display: flex;
            justify-content: flex-end;
            align-items: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        /* Style des liens de la navbar */
        .navbar a {
            color: black !important;
            text-decoration: none;
            font-size: 20px !important;
            font-weight: bold !important;
            margin: 0 15px !important;
        }
        .navbar a:hover {
            color: #4CAF50 !important;
        }
        
        /* Espace pour la navbar fixe */
        .stApp {
            margin-top: 70px !important;
            background: #F3F3F1 url('https://images.unsplash.com/photo-1514995669114-6081e934b693?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat left top / 65% auto;
            min-height: calc(100vh - 70px);
        }
        
        /* Cache l'ancienne navbar */
        section[data-testid="stSidebar"] { display: none !important; }
        
        /* Styles existants conservés */
        .content-behind {
            position: relative;
            z-index: 0;
        }
        
        .welcome-text {
            color: black;
            text-align: right;
            font-size: 24px;
            margin-right: 20px;
            margin-top: -13px;
        }
        
        .calculator-banner {
            background-color: white;
            padding: 25px;
            border-radius: 0;
            width: 100vw;
            margin: 20px 0;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            position: fixed;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            margin-top: -13px;
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

# ========== NAVBAR NATIVE STREAMLIT ==========
st.markdown("""
    <div class="navbar">
        <a href="/" target="_self">Accueil</a>
        <a href="/Calculateur" target="_self">Calculateur</a>
        <a href="/Ressources" target="_self">Ressources</a>
        <a href="/Methodologie" target="_self">Méthodologie</a>
    </div>
""", unsafe_allow_html=True)

# ========== CONTENU PRINCIPAL ==========
st.markdown('<div class="content-behind">', unsafe_allow_html=True)

# Colonnes pour logo + texte
col1, col2 = st.columns([3, 1])
with col2:
    st.image("Logo.jpg", width=300)

# Texte de bienvenue
st.markdown("""
    <div class="welcome-text">
        <h1>Bienvenue sur EcoImpact</h1>
        <p>Découvrez votre impact environnemental avec notre outil.</p>
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

# ========== FOOTER ==========
st.markdown("""
    <div class="footer-banner">
        <a href="/A_propos" target="_self">À propos</a>
        <img src="https://prepeersstorage.blob.core.windows.net/academic/1_400_logo_9f8797ed-c537-418c-9215-a420e600a540.png?sp=r&st=2025-01-30T23:00:00Z&se=2026-01-31T04:06:31Z&spr=https&sv=2022-11-02&sr=c&sig=Mm5p4fZa8%2F4%2BFA04dmK5p259BIm5Y9rzEDR8GPPJTWY%3D">
    </div>
""", unsafe_allow_html=True)


       
