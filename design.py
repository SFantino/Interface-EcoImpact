import streamlit as st

# ========== STYLE CSS ========== 
def load_css():
    st.markdown("""
        <style>
            .navbar {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 70px;
                background-color: #F3F3F1;
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

            /* Masquer la sidebar, footer et header sur toutes les pages */
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
            <a href="/Pourquoi_ce_projet" target="_self">Pourquoi ce projet ?</a>
            <a href="/Comment_ca_marche" target="_self">Comment ça marche ?</a>
        </div>
    """, unsafe_allow_html=True)

def create_footer():
    st.markdown("""
        <div class="footer-banner">
            <a href="/Equipe" target="_self" style="color: white;">Equipe</a>  <!-- Remplacé "À propos" par "Equipe" -->
            <img src="https://prepeersstorage.blob.core.windows.net/academic/1_400_logo_9f8797ed-c537-418c-9215-a420e600a540.png?sp=r&st=2025-01-30T23:00:00Z&se=2026-01-31T04:06:31Z&spr=https&sv=2022-11-02&sr=c&sig=Mm5p4fZa8%2F4%2BFA04dmK5p259BIm5Y9rzEDR8GPPJTWY%3D">
        </div>
    """, unsafe_allow_html=True)

