import streamlit as st

# Configuration de la page
st.set_page_config(page_title="EcoImpact", layout="wide")

# Style CSS complet
st.markdown("""
    <style>
        /* Fond d'écran */
        .stApp {
            background: #F3F3F1 url('https://images.unsplash.com/photo-1514995669114-6081e934b693?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat left top / 65% auto;
            min-height: 100vh;
        }
        
        /* Navigation stylisée */
        .stButton>button {
            background: transparent;
            border: none;
            color: black;
            font-size: 20px;
            font-weight: bold;
            margin: 0 15px;
            padding: 0;
            cursor: pointer;
            box-shadow: none;
        }
        .stButton>button:hover {
            color: #4CAF50;
            background: transparent;
        }
        
        /* Masquer éléments Streamlit par défaut */
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Vos styles existants */
        .welcome-text {
            color: black;
            text-align: right;
            font-size: 24px;
            margin-right: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Navigation avec état de session
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Accueil'

# Fonction de changement de page
def change_page(page_name):
    st.session_state.current_page = page_name

# Barre de navigation
cols = st.columns([3, 1, 1, 1, 1])
with cols[0]:
    st.write("")  # Espace vide
with cols[1]:
    if st.button("Accueil"):
        change_page('Accueil')
with cols[2]:
    if st.button("Calculateur"):
        change_page('Calculateur')
with cols[3]:
    if st.button("Ressources"):
        change_page('Ressources')
with cols[4]:
    if st.button("Méthodologie"):
        change_page('Méthodologie')

# Affichage du contenu en fonction de la page
if st.session_state.current_page == 'Accueil':
    st.markdown('<div class="content-behind">', unsafe_allow_html=True)
    
    col_img, col_content = st.columns([1, 3])
    with col_img:
        st.image("Logo.jpg", width=300)
    
    with col_content:
        st.markdown("""
            <div class="welcome-text">
                <h1>Bienvenue sur EcoImpact</h1>
                <p>Ceci est la page d'accueil de notre projet.</p>
            </div>
        """, unsafe_allow_html=True)

elif st.session_state.current_page == 'Calculateur':
    from pages.Calculateur import show_page
    show_page()
    
elif st.session_state.current_page == 'Ressources':
    from pages.Ressources import show_page
    show_page()
    
elif st.session_state.current_page == 'Méthodologie':
    from pages.Methodologie import show_page
    show_page()

# [Votre footer existant]
