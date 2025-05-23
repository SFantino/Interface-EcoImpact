import streamlit as st
from calculateur.Panier import gerer_panier
from calculateur.Score_panier import score_panier
from calculateur.Variables import variables
from calculateur.etapes_panier import etapes_panier

# ========== CONFIGURATION ==========
st.set_page_config(
    page_title="Méthodologie | EcoImpact",
    layout="wide",
    page_icon="📊",
    initial_sidebar_state="collapsed"
)

# ========== STYLE CSS ==========
def load_css():
    st.markdown("""
        <style>
            /* Identique à ressources.py */
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
            
            .stApp {
                margin-top: 70px !important;
                background-color: #F3F3F1;
                min-height: calc(100vh - 70px);
            }
            
            .content-behind {
                padding: 20px 40px;
            }
            
            h1, h2, h3 {
                color: #000000 !important;
            }
            
            .methodo-card {
                background: white;
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            
            section[data-testid="stSidebar"],
            footer,
            header {
                display: none !important;
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

# ========== COMPOSANTS ==========
def create_navbar():
    st.markdown("""
        <div class="navbar">
            <a href="/" target="_self">Accueil</a>
            <a href="/Calculateur" target="_self">Calculateur</a>
            <a href="/Ressources" target="_self">Ressources</a>
            <a href="/Methodologie" target="_self" style="color: #4CAF50 !important;">Méthodologie</a>
        </div>
    """, unsafe_allow_html=True)

def create_footer():  # Ajoute les parenthèses ici
    st.markdown("""
        <div class="footer-banner">
            <a href="/Equipe" target="_self" style="color: white;">Equipe</a>  <!-- Remplacé "À propos" par "Equipe" -->
            <img src="https://prepeersstorage.blob.core.windows.net/academic/1_400_logo_9f8797ed-c537-418c-9215-a420e600a540.png?sp=r&st=2025-01-30T23:00:00Z&se=2026-01-31T04:06:31Z&spr=https&sv=2022-11-02&sr=c&sig=Mm5p4fZa8%2F4%2BFA04dmK5p259BIm5Y9rzEDR8GPPJTWY%3D">
        </div>
    """, unsafe_allow_html=True)
# ========== CONTENU ==========
def methodo_content():
    st.markdown('<div class="content-behind">', unsafe_allow_html=True)
    
    st.markdown("<h1 style='color:#000000;'>📊 Méthodologie Scientifique</h1>", unsafe_allow_html=True)
    

    st.markdown('</div>', unsafe_allow_html=True)

# ========== STRUCTURE ==========
load_css()
create_navbar()
methodo_content()
create_footer()


# ========== CONTENU PRINCIPAL ==========
# Appeler la fonction qui gère tout le panier
gerer_panier()

# Affichage des codes CIQUAL dans le panier
codes_ciqual = [int(produit["code_ciqual"]) for produit in st.session_state.panier]


# Appeler la fonction pour calculer le score du panier
score_panier()

# Appeler la fonction pour afficher les variables environnementales
variables()

# Appeler la fonction pour afficher les comparaison des étapes pour le panier
etapes_panier()
