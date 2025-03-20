import streamlit as st

# Configuration de la page
st.set_page_config(page_title="EcoImpact", layout="wide")

# Style CSS pour le fond d'écran
st.markdown("""
    <style>
        /* Style pour le fond d'écran */
        .stApp {
            position: relative;
            z-index: 1;
        }
        .stApp::before {
            content: "";
            background-image: url('Fond_accueil.png');
            background-size: cover; /* Couvre toute la page */
            background-position: center; /* Centre l'image */
            background-repeat: no-repeat; /* Empêche la répétition */
            background-attachment: fixed; /* Fixe l'image pendant le défilement */
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1; /* Place l'image derrière le contenu */
            opacity: 1; /* Assure que l'image est visible */
        }
        /* Style pour le contenu */
        .content {
            position: relative;
            z-index: 1; /* Place le contenu au-dessus de l'image */
            padding-top: 80px; /* Espace pour le bandeau */
            color: black; /* Couleur du texte */
        }
        /* Masquer le footer et le header par défaut de Streamlit */
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Contenu de la page (texte d'accueil)
st.markdown('<div class="content">', unsafe_allow_html=True)

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

st.markdown('</div>', unsafe_allow_html=True)
