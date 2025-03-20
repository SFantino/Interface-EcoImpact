import streamlit as st

# Configuration de la page
st.set_page_config(page_title="EcoImpact", layout="wide")

# Style CSS pour le fond d'écran et le contenu
st.markdown("""
    <style>
        /* Style pour le fond d'écran */
        .stApp {
            background-color: #F3F3F1; /* Couleur de fond de secours */
        }
        /* Style pour le contenu */
        .content {
            position: relative;
            z-index: 1; /* Place le contenu au-dessus de l'image ou du fond */
            padding-top: 80px; /* Espace pour le bandeau */
            color: black; /* Couleur du texte */
        }
        /* Masquer le footer et le header par défaut de Streamlit */
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Afficher l'image en fond d'écran avec st.image
try:
    st.image("Fond_accueil.png", use_column_width=True)
except FileNotFoundError:
    st.warning("L'image 'Fond_accueil.png' n'a pas été trouvée. Utilisation de la couleur de fond #F3F3F1.")

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
