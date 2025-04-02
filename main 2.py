import streamlit as st

# Configuration de la page
st.set_page_config(page_title="EcoImpact", layout="wide")

# Style CSS avec effets de parallaxe
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
        
        /* Conteneur du fond avec effet parallaxe */
        .parallax-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 65%;
            height: 100vh;
            z-index: -1;
            overflow: hidden;
        }
        
        /* Image de fond avec mouvement */
        .parallax-bg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 120%;
            background: url('https://images.unsplash.com/photo-1514995669114-6081e934b693?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat left top / cover;
        }
        
        /* Logo avec mouvement parallaxe */
        .parallax-logo {
            position: fixed;
            top: 80px;
            left: 20px;
            width: 300px;
            z-index: 999;
            transition: transform 0.5s ease-out;
        }
        
        /* Fond principal */
        .stApp {
            background-color: #F3F3F1;
            min-height: 100vh;
        }
        
        /* Contenu */
        .content {
            padding-top: 80px;
            position: relative;
            z-index: 1;
        }
        
        /* Footer fixe */
        .footer-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #23A95C;
            padding: 10px 20px;
            z-index: 1001;
        }
    </style>
    
    <!-- Structure HTML pour les effets -->
    <div class="parallax-container">
        <div class="parallax-bg" id="parallax-bg"></div>
    </div>
    <img class="parallax-logo" id="parallax-logo" src="Logo.jpg">
""", unsafe_allow_html=True)

# Script pour les effets de mouvement
st.markdown("""
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const bg = document.getElementById('parallax-bg');
            const logo = document.getElementById('parallax-logo');
            const startPos = 100; // Délai avant l'effet
            
            window.addEventListener('scroll', function() {
                const scrollY = window.scrollY;
                
                // Mouvement de l'image de fond (parallaxe)
                if (scrollY > startPos) {
                    const bgOffset = (scrollY - startPos) * 0.5;
                    bg.style.transform = `translateY(-${bgOffset}px)`;
                    
                    // Mouvement plus rapide pour le logo
                    const logoOffset = (scrollY - startPos) * 0.8;
                    logo.style.transform = `translateY(-${logoOffset}px)`;
                    logo.style.opacity = 1 - (scrollY - startPos) / 300;
                } else {
                    bg.style.transform = 'translateY(0)';
                    logo.style.transform = 'translateY(0)';
                    logo.style.opacity = 1;
                }
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

# ... Votre contenu existant ...

# Footer
st.markdown("""
    <div class="footer-banner">
        <a href="/a_propos">À propos</a>
        <img src="unilasalle_beauvais_logo.jpg" alt="Logo UniLaSalle Beauvais">
    </div>
""", unsafe_allow_html=True)
