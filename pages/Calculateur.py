import streamlit as st
from design import load_css, create_navbar, create_footer
from calculateur.Panier import gerer_panier
from calculateur.Score_panier import score_panier
from calculateur.Variables import variables
from calculateur.etapes_panier import etapes_panier


# ========== STYLE CSS ==========
def load_css():
    st.markdown("""
        <style>
            /* Identique à ressources.py */
            .navbar {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 70px;
                background-color: #FFFFFF !important;
                padding: 15px 20px;
                z-index: 1000;
                display: flex;
                justify-content: flex-end;
                align-items: center;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
        </style>
    """, unsafe_allow_html=True)


# ========== CONTENU ==========
def methodo_content():
    st.markdown('<div class="content-behind">', unsafe_allow_html=True)
    
    st.markdown("<h1 style='color:#000000;'>📊 Méthodologie Scientifique</h1>", unsafe_allow_html=True)
    

    st.markdown('</div>', unsafe_allow_html=True)

# ========== STRUCTURE ==========
load_css()
create_navbar()
methodo_content()
create_footer()


# ========== CONTENU PRINCIPAL ==========
# Appeler la fonction qui gère tout le panier
gerer_panier()

# Affichage des codes CIQUAL dans le panier
codes_ciqual = [int(produit["code_ciqual"]) for produit in st.session_state.panier]


# Appeler la fonction pour calculer le score du panier
score_panier()

# Appeler la fonction pour afficher les variables environnementales
variables()

# Appeler la fonction pour afficher les comparaison des étapes pour le panier
etapes_panier()
