import streamlit as st

# Configuration de la page
st.set_page_config(page_title="EcoImpact", layout="wide")

# Style CSS pour le fond d'écran et le contenu
st.markdown("""
    <style>
        /* Style pour le fond d'écran */
        .stApp {
            background-image: url('https://images.unsplash.com/photo-1514995669114-6081e934b693?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
            background-size: cover; /* Couvre toute la page */
            background-position: center; /* Centre l'image */
            background-repeat: no-repeat; /* Empêche la répétition */
            background-attachment: fixed; /* Fixe l'image pendant le défilement */
        }
        /* Style pour le contenu */
        .content {
            position: relative;
            z-index: 1; /* Place le contenu au-dessus de l'image */
            padding-top: 80px; /* Espace pour le bandeau */
            color: black; /* Couleur du texte en noir */
        }
        /* Style pour le bandeau */
        .navbar {
            position: fixed;
            top: 0;
            right: 0; /* Aligner à droite */
            background-color: transparent;
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
        /* Masquer le footer et le header par défaut de Streamlit */
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Bandeau de navigation à droite
st.markdown("""
    <div class="navbar">
        <a href="/">Accueil</a>
        <a href="/methodologie">Méthodologie</a>
        <a href="/ressources">Ressources</a>
    </div>
""", unsafe_allow_html=True)

# Créer deux colonnes
col1, col2 = st.columns([3, 1])  # La première colonne est plus large pour le texte, la deuxième pour l'image


# Afficher l'image dans la deuxième colonne (à droite)
with col2:
    st.markdown("""
        <style>
            .custom-image {
                margin-top: 50px; /* Déplace l'image plus bas */
            }
        </style>
    """, unsafe_allow_html=True)
    st.image("Logo.jpg", width=300)  # Ajustez la largeur si nécessaire

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

# Style CSS pour le bandeau en bas de la page
st.markdown("""
    <style>
        /* Style pour le bandeau en bas de la page */
        .footer-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #23A95C; /* Couleur du bandeau */
            padding: 10px 0; /* Espacement interne */
            text-align: center; /* Centrer le texte */
            z-index: 1000; /* Assure que le bandeau est au-dessus de l'image */
        }
        .footer-banner a {
            color: white; /* Couleur du texte en blanc */
            text-decoration: none; /* Supprimer le soulignement */
            font-size: 20px;
            font-weight: bold;
        }
        .footer-banner a:hover {
            color: #F3F3F1; /* Couleur au survol */
        }
    </style>
""", unsafe_allow_html=True)

# Afficher le bandeau en bas de la page avec le lien "À propos"
st.markdown("""
    <div class="footer-banner">
        <a href="/a_propos">À propos</a>
    </div>
""", unsafe_allow_html=True)
