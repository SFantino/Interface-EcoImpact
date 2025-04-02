import streamlit as st

# Configuration de la page
st.set_page_config(page_title="EcoImpact", layout="wide")

# Style CSS pour le fond d'écran et le contenu
st.markdown("""
    <style>
        /* Style pour le fond d'écran */
        .stApp {
            background: #F3F3F1 url('https://images.unsplash.com/photo-1514995669114-6081e934b693?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat left top / 65% auto;
            min-height: 100vh;
        }
        
        /* Style pour le bandeau de navigation */
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
        
        /* Zone de contenu principale */
        .content-behind {
            position: relative;
            z-index: 0;
            margin-top: 70px;
        }
        
        /* Style pour le texte de la page d'accueil */
        .welcome-text {
            color: black;
            text-align: right;
            font-size: 24px;
            margin-right: 20px;
        }
        
        /* Style pour la bannière du calculateur */
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
        
        /* Style pour le bandeau en bas de page */
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
        
        /* Masquer le footer et le header par défaut de Streamlit */
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Bandeau de navigation
st.markdown("""
    <div class="navbar">
        <a href="/">Accueil</a>
        <a href="/calculateur">Calculateur</a>
        <a href="/ressources">Ressources</a>
        <a href="/methodologie">Méthodologie</a>
    </div>
""", unsafe_allow_html=True)

# Début de la zone de contenu (qui passera derrière la navbar au scroll)
st.markdown('<div class="content-behind">', unsafe_allow_html=True)

# Création des colonnes
col1, col2 = st.columns([3, 1])

# Logo dans la colonne de droite
with col2:
    st.image("Logo.jpg", width=300)

# Contenu de la page
page = st.query_params.get("page", ["home"])[0]

if page == "home":
    st.markdown("""
        <div class="welcome-text">
            <h1>Bienvenue sur EcoImpact</h1>
            <p>Ceci est la page d'accueil de notre projet.</p>
        </div>
    """, unsafe_allow_html=True)
elif page == "methodologie":
    st.title("Méthodologie")
    st.write("Cette page présente la méthodologie utilisée dans notre projet.")
elif page == "ressources":
    st.title("Ressources")
    st.write("Cette page contient des ressources utiles pour notre projet.")

# Fin de la zone de contenu principale
st.markdown('</div>', unsafe_allow_html=True)

# Calculator Banner
st.markdown("""
    <div style="padding-bottom: 100px;">
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
        <img src="unilasalle_beauvais_logo.jpg" alt="Logo UniLaSalle Beauvais">
    </div>
""", unsafe_allow_html=True)
