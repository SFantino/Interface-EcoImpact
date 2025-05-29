import streamlit as st
from calculateur.Panier import gerer_panier
from calculateur.Score_panier import score_panier
from calculateur.Variables import variables
from calculateur.etapes_panier import etapes_panier
from design import load_css, create_navbar, create_footer



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



# ========== STRUCTURE ==========
load_css()
st.markdown("""
    <style>
    .main {
        background-color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

create_navbar()
create_footer()

