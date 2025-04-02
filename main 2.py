import streamlit as st

# Configuration de base
st.set_page_config(page_title="EcoImpact", layout="wide")

# Style CSS optimisé
st.markdown("""
    <style>
        /* Reset Streamlit */
        .stApp { background: #F3F3F1; min-height: 100vh; }
        
        /* Navbar transparente */
        .transparent-nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: transparent !important;
            padding: 25px 40px;
            display: flex;
            gap: 40px;
            z-index: 1000;
        }
        
        .nav-item {
            color: #000 !important;
            font-size: 1.1rem;
            font-weight: 600;
            text-decoration: none;
            transition: color 0.3s;
            text-shadow: 0 0 2px rgba(255,255,255,0.8);
        }
        
        .nav-item:hover { color: #23A95C !important; }
        
        /* Image de fond */
        .bg-cover {
            position: fixed;
            top: 0;
            left: 0;
            width: 60%;
            height: 100vh;
            background: url('https://images.unsplash.com/photo-1514995669114-6081e934b693?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat left top/cover;
            z-index: -1;
        }
        
        /* Contenu */
        .main-content { margin-top: 100px; }
        
        /* Footer */
        .page-footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background: #23A95C;
            padding: 15px 40px;
            z-index: 900;
        }
        
        /* Masquer éléments par défaut */
        header, footer { visibility: hidden !important; }
    </style>
""", unsafe_allow_html=True)

# Structure HTML
st.markdown("""
    <!-- Background -->
    <div class="bg-cover"></div>
    
    <!-- Navbar Transparente -->
    <nav class="transparent-nav">
        <a href="/" class="nav-item">Accueil</a>
        <a href="/calculateur" class="nav-item">Calculateur</a>
        <a href="/ressources" class="nav-item">Ressources</a>
        <a href="/methodologie" class="nav-item">Méthodologie</a>
    </nav>
    
    <!-- Logo -->
    <img src="Logo.jpg" style="
        position: fixed;
        top: 85px;
        left: 40px;
        width: 250px;
        z-index: 999;
    ">
""", unsafe_allow_html=True)

# Contenu principal
with st.container():
    st.markdown("""
        <div class="main-content">
            <!-- Votre contenu ici -->
            <div style="text-align: right; padding-right: 5%;">
                <h1 style="color: #000;">Bienvenue sur EcoImpact</h1>
                <p style="color: #333;">Plateforme d'analyse environnementale</p>
            </div>
        </div>
        
        <!-- Footer -->
        <div class="page-footer">
            <span style="color: #FFF;">À propos</span>
            <img src="unilasalle_beauvais_logo.jpg" style="height: 35px; float: right;">
        </div>
    """, unsafe_allow_html=True)
