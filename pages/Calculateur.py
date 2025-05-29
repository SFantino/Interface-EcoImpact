import streamlit as st
from calculateur.Panier import gerer_panier
from calculateur.Score_panier import score_panier
from calculateur.Variables import variables
from calculateur.etapes_panier import etapes_panier
from design import load_css, create_navbar, create_footer

with st.container():
    st.markdown("""
        <div style="background-color: white; padding: 2rem; min-height: 100vh;">
    """, unsafe_allow_html=True)

    # Ton code principal ici
    gerer_panier()
    codes_ciqual = [int(produit["code_ciqual"]) for produit in st.session_state.panier]
    score_panier()
    variables()
    etapes_panier()

    st.markdown("</div>", unsafe_allow_html=True)



# ========== STRUCTURE ==========
load_css()
create_navbar()
create_footer()
