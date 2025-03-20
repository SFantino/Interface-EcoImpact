import streamlit as st

# Configuration de la page
st.set_page_config(page_title="EcoImpact", layout="wide")

# Style CSS pour le bandeau, les liens et le fond d'écran
st.markdown("""
    <style>
        /* Style pour le bandeau */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: transparent;
            padding: 15px 0;
            text-align: center;
            z-index: 1000;
        }
        .navbar a {
            color: black;
            text-decoration: none;
            font-size: 20px;
            font-weight: bold;
            margin: 0 25px;
        }
        .navbar a:hover {
            color: #4CAF50;
        }
        /* Style pour le fond d'écran */
        .stApp {
            background-image: url('Fond_accueil.png');
            background-size: cover;
            background-position: center;
        }
        /* Masquer le footer et le header par défaut de Streamlit */
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Testez l'image
try:
    st.image("Fond_accueil.png", use_column_width=True)
except FileNotFoundError:
    st.error("L'image 'Fond_accueil.png' n'a pas été trouvée. Vérifiez le chemin.")

# Bandeau de navigation
st.markdown("""
    <div class="navbar">
        <a href="/">Accueil</a>
        <a href="/methodologie">Méthodologie</a>
        <a href="/ressources">Ressources</a>
    </div>
""", unsafe_allow_html=True)

# Gestion des pages avec st.query_params
page = st.query_params.get("page", ["home"])[0]

if page == "home":
    st.title("Bienvenue sur EcoImpact")
    st.write("Ceci est la page d'accueil de notre projet.")
elif page == "methodologie":
    st.title("Méthodologie")
    st.write("Cette page présente la méthodologie utilisée dans notre projet.")
elif page == "ressources":
    st.title("Ressources")
    st.write("Cette page contient des ressources utiles pour notre projet.")
