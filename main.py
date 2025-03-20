import streamlit as st

# Configuration de la page
st.set_page_config(page_title="EcoImpact", layout="wide")

# Style CSS pour le fond d'écran et le contenu
st.markdown("""
    <style>
        /* Style pour le fond d'écran */
        .stApp {
            background-color: #F3F3F1; /* Couleur de fond de secours */
            position: relative;
            z-index: 1;
        }
        .stApp::before {
            content: "";
            background-image: url('https://images.unsplash.com/photo-1514995669114-6081e934b693?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
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
            z-index: 1; /* Place le contenu au-dessus de l'image ou du fond */
            padding-top: 80px; /* Espace pour le bandeau */
            color: black; /* Couleur du texte */
        }
        /* Style pour le bandeau */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: transparent;
            padding: 15px 0;
            text-align: center;
            z-index: 1000; /* Assure que le bandeau est au-dessus de l'image */
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
        /* Masquer le footer et le header par défaut de Streamlit */
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Bandeau de navigation
st.markdown("""
    <div class="navbar">
        <a href="/">Accueil</a>
        <a href="/methodologie">Méthodologie</a>
        <a href="/ressources">Ressources</a>
    </div>
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
