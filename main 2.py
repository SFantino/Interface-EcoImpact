import streamlit as st

# Configuration de la page
st.set_page_config(page_title="EcoImpact", layout="wide")

# Style CSS avec effet de fond disparaissant
st.markdown("""
    <style>
        /* Navbar fixe */
        .navbar {
            position: fixed;
            top: 0;
            right: 0;
            left: 0;
            background-color: white;
            padding: 15px 20px;
            text-align: right;
            z-index: 1000;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            height: 60px;
        }
        .navbar a {
            color: black;
            text-decoration: none;
            font-size: 20px;
            font-weight: bold;
            margin: 0 15px;
        }
        .navbar a:hover {
            color: #4CAF50;
        }

        /* Conteneur pour l'image de fond */
        .background-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 65%;
            height: 100vh;
            z-index: -1;
            overflow: hidden;
        }
        
        /* Image de fond avec transition d'opacité */
        .background-image {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: url('https://images.unsplash.com/photo-1514995669114-6081e934b693?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat left top / cover;
            transition: opacity 0.8s ease;
        }

        /* Fond principal */
        .stApp {
            background-color: #F3F3F1 !important;
            min-height: 100vh;
        }

        /* Contenu */
        .content {
            padding-top: 80px;
            color: black;
        }

        /* Footer */
        .footer-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #23A95C;
            padding: 10px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 1001;
        }
        
        /* Masquer les éléments par défaut de Streamlit */
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>

    <!-- Structure HTML pour l'image de fond -->
    <div class="background-container">
        <div class="background-image" id="bg-image"></div>
    </div>
""", unsafe_allow_html=True)

# Script pour l'effet de disparition
st.markdown("""
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const bgImage = document.getElementById('bg-image');
            const fadeStart = 100;  // Commence à disparaître après 100px
            const fadeLength = 300; // Disparaît complètement après 300px
            
            window.addEventListener('scroll', function() {
                const scrollPos = window.scrollY;
                let opacity = 1;
                
                if (scrollPos > fadeStart) {
                    opacity = 1 - (scrollPos - fadeStart) / fadeLength;
                    opacity = Math.max(0, opacity);
                }
                
                bgImage.style.opacity = opacity;
            });
        });
    </script>
""", unsafe_allow_html=True)

# Barre de navigation
st.markdown("""
    <div class="navbar">
        <a href="/">Accueil</a>
        <a href="/methodologie">Méthodologie</a>
        <a href="/ressources">Ressources</a>
    </div>
""", unsafe_allow_html=True)

# Contenu principal
st.markdown('<div class="content">', unsafe_allow_html=True)

# ... Votre contenu existant ici ...

# Footer
st.markdown("""
    <div class="footer-banner">
        <a href="/a_propos">À propos</a>
        <img src="unilasalle_beauvais_logo.jpg" alt="Logo UniLaSalle Beauvais">
    </div>
""", unsafe_allow_html=True)
