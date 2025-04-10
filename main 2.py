import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="EcoImpact",
    layout="wide",
    page_icon="🌱",
    initial_sidebar_state="collapsed"
)

# ========== CSS UNIFIÉ ==========
st.markdown("""
    <style>
        /* Navbar principale */
        .main-nav {
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
        
        .main-nav a {
            color: black !important;
            text-decoration: none;
            font-size: 20px !important;
            font-weight: bold !important;
            margin: 0 15px !important;
        }
        
        .main-nav a:hover {
            color: #4CAF50 !important;
        }
        
        .main-nav a.active {
            color: #4CAF50 !important;
            border-bottom: 3px solid #4CAF50;
        }
        
        /* Espace pour la navbar fixe */
        .stApp {
            margin-top: 70px !important;
            background: #F3F3F1 url('https://images.unsplash.com/photo-1514995669114-6081e934b693?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat left top / 65% auto;
            min-height: calc(100vh - 70px);
        }
        
        /* Cache les éléments Streamlit inutiles */
        section[data-testid="stSidebar"] { display: none !important; }
        header { visibility: hidden !important; }
        footer { visibility: hidden !important; }
        
        /* Styles spécifiques à la page d'accueil */
        .welcome-text {
            color: black;
            text-align: right;
            font-size: 24px;
            margin-right: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# ========== NAVBAR DYNAMIQUE ==========
# Détermine la page active
current_page = st.experimental_get_query_params().get("page", ["home"])[0]

# Crée la navbar
nav_items = {
    "home": "Accueil",
    "Calculateur": "Calculateur",
    "Ressources": "Ressources",
    "Methodologie": "Méthodologie"
}

nav_links = []
for page, name in nav_items.items():
    if page == current_page:
        nav_links.append(f'<a href="?page={page}" class="active" target="_self">{name}</a>')
    else:
        nav_links.append(f'<a href="?page={page}" target="_self">{name}</a>')

st.markdown(
    f'<div class="main-nav">{"".join(nav_links)}</div>', 
    unsafe_allow_html=True
)

# ========== CONTENU DE LA PAGE ==========
if current_page == "home":
    # Contenu de la page d'accueil
    st.markdown('<div class="content-behind">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col2:
        st.image("Logo.jpg", width=300)
    
    st.markdown("""
        <div class="welcome-text">
            <h1>Bienvenue sur EcoImpact</h1>
            <p>Découvrez votre impact environnemental avec notre outil.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="padding-bottom: 100px;">
            <div class="calculator-banner">
                <div class="calculator-title">Tester le calculateur</div>
                <a href="?page=Calculateur" target="_self">
                    <button class="start-button">Start</button>
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ========== FOOTER ==========
st.markdown("""
    <div class="footer-banner">
        <a href="/A_propos" target="_self">À propos</a>
        <img src="unilasalle_beauvais_logo.jpg" alt="Logo UniLaSalle Beauvais">
    </div>
""", unsafe_allow_html=True)
