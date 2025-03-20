import streamlit as st

# Configuration de la page
st.set_page_config(page_title="EcoImpact", layout="wide")

# Style CSS pour le fond d'écran et le contenu
st.markdown("""
    <style>
        /* Style pour le fond d'écran */
        .stApp {
            background-color: #F3F3F1;
        }
        /* Style pour le contenu */
        .content {
            position: relative;
            z-index: 1; /* Place le contenu au-dessus de l'image ou du fond */
            padding-top: 80px; /* Espace pour le bandeau */
            color: black; /* Couleur du texte */
        }
        /* Style pour le bandeau */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%; /* Occupe toute la largeur */
            background-color: #D9D9D9;
            padding: 15px 20px; /* Espacement */
            text-align: right; /* Aligner le texte à droite */
            z-index: 1000; /* Assure que le bandeau est au-dessus de l'image */
        }
        .navbar a {
            color: black; /* Couleur du texte en noir */
            text-decoration: none;
            font-size: 20px;
            font-weight: bold;
            margin: 0 15px; /* Espace entre les liens */
        }
        .navbar a:hover {
            color: #4CAF50; /* Couleur au survol */
        }
          /* Style pour le titre en bas */
        .title {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            text-align: center;
            color: black; /* Couleur du texte en noir */
            font-size: 36px;
            font-weight: bold;
            padding-bottom: 20px; /* Espace en bas */
        }
        /* Style pour les titres et textes */
        h1, h2, h3, h4, h5, h6, p {
            color: black !important; /* Couleur du texte en noir */
        }
        /* Masquer le footer et le header par défaut de Streamlit */
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Afficher l'image en haut à gauche avec st.image
st.image("Fond1.jpg", use_container_width=True)


# Bandeau de navigation à droite
st.markdown("""
    <div class="navbar">
        <a href="/">Accueil</a>
        <a href="/methodologie">Méthodologie</a>
        <a href="/ressources">Ressources</a>
    </div>
""", unsafe_allow_html=True)

# Titre "Bienvenue sur EcoImpact" en bas
st.markdown('<div class="title">Bienvenue sur EcoImpact</div>', unsafe_allow_html=True)

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
