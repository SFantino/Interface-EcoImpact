import streamlit as st

# ========== CONFIGURATION ==========
st.set_page_config(
    page_title="Ressources | EcoImpact",
    layout="wide",
    page_icon="📚",
    initial_sidebar_state="collapsed"
)

# ========== STYLE CSS ==========
def load_css():
    st.markdown("""
        <style>
            /* Navbar identique à main.py */
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
            
            .resource-card {
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
        </style>
    """, unsafe_allow_html=True)

# ========== COMPOSANTS ==========
def create_navbar():
    st.markdown("""
        <div class="navbar">
            <a href="/" target="_self">Accueil</a>
            <a href="/Calculateur" target="_self">Calculateur</a>
            <a href="/Ressources" target="_self" style="color: #4CAF50 !important;">Ressources</a>
            <a href="/Methodologie" target="_self">Méthodologie</a>
        </div>
    """, unsafe_allow_html=True)

def create_footer():
    st.markdown("""
        <div class="footer-banner">
            <a href="/A_propos" target="_self">À propos</a>
            <img src="unilasalle_beauvais_logo.jpg" alt="Logo UniLaSalle Beauvais">
        </div>
    """, unsafe_allow_html=True)

# ========== CONTENU ==========
def ressources_content():
    st.markdown('<div class="content-behind">', unsafe_allow_html=True)
    
    st.markdown("<h1 style='color:#000000;'>📚 Ressources Utiles</h1>", unsafe_allow_html=True)
    

    st.markdown('</div>', unsafe_allow_html=True)

# ========== STRUCTURE ==========
load_css()
create_navbar()
ressources_content()
create_footer()
