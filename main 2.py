import streamlit as st

# Configuration de la page
st.set_page_config(page_title="EcoImpact", layout="wide")

# Style CSS pour le fond d'écran et le contenu
st.markdown("""
    <style>
        /* Style pour le fond d'écran */
        .stApp {
            background: #F3F3F1 url('https://images.unsplash.com/photo-1514995669114-6081e934b693?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat left top / 60% auto;
            min-height: 100vh;
        }
        /* Pour décaler le contenu sous l'image */
        .content {
            padding-top: 30vh;
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

        .calculator-banner {
            background-color: white;
            padding: 25px;
            border-radius: 10px;
            width: 80%;
            margin: 20px auto;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .calculator-title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 15px;
            color: #333;
        }
        .start-button {
            background-color: #23A95C;
            color: white;
            border: none;
            padding: 12px 30px;
            font-size: 18px;
            border-radius: 50px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .start-button:hover {
            background-color: #1e8c4f;
        }
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

st.markdown("""
    <div class="calculator-banner">
        <div class="calculator-title">Tester le calculateur</div>
        <button class="start-button">Start</button>
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
    # Style CSS pour le texte de la page d'accueil
    st.markdown("""
        <style>
            /* Style pour le texte de la page d'accueil */
            .welcome-text {
                color: black; /* Couleur du texte en noir */
                text-align: right; /* Aligner le texte à droite */
                font-size: 24px; /* Taille de la police */
                margin-right: 20px; /* Marge à droite pour décaler le texte */
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Contenu de la page d'accueil
    st.markdown("""
        <div class="welcome-text">
            <h1>Bienvenue sur EcoImpact</h1>
            <p>Ceci est la page d'accueil de notre projet.</p>
        </div>
    """, unsafe_allow_html=True)

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
            padding: 10px 20px; /* Espacement interne */
            display: flex;
            justify-content: space-between; /* Espace les éléments à gauche et à droite */
            align-items: center; /* Centre verticalement */
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
        .footer-banner img {
            height: 40px; /* Hauteur de l'image */
            margin-left: auto; /* Pousse l'image à droite */
        }
    </style>
""", unsafe_allow_html=True)

# Afficher le bandeau en bas de la page avec "À propos" à gauche et l'image à droite
st.markdown("""
    <div class="footer-banner">
        <a href="/a_propos">À propos</a>
        <img src="unilasalle_beauvais_logo.jpg" alt="Logo UniLaSalle Beauvais">
    </div>
""", unsafe_allow_html=True) 
