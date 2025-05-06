import streamlit as st
from design import load_css, create_navbar, create_footer

# ========== CONFIGURATION ==========
st.set_page_config(
    page_title="Pourquoi ce projet ? | EcoImpact",
    layout="wide",
    page_icon="🌍",
    initial_sidebar_state="collapsed"
)


# ========== CONTENU ==========
def pourquoi_ce_projet_content():
    st.markdown('<div class="content-behind">', unsafe_allow_html=True)
    
    st.markdown("<h1 style='color:#000000;'>🌍 Pourquoi ce projet ?</h1>", unsafe_allow_html=True)
    
    # Début des questions en accordéon
    with st.expander("1. Quel est l'objectif principal de ce projet ?"):
        st.markdown("""
        L'objectif principal de ce projet est de fournir aux consommateurs un outil qui évalue l'impact environnemental des produits alimentaires, basé sur des données scientifiques fiables.
        Ce projet vise à sensibiliser et à aider les consommateurs à prendre des décisions alimentaires plus responsables, en tenant compte des conséquences environnementales de leurs choix.
        """)
    
    with st.expander("2. Pourquoi est-ce important de connaître l'impact environnemental des produits alimentaires ?"):
        st.markdown("""
        Les produits alimentaires ont un impact considérable sur l'environnement, que ce soit par la production, le transport, l'emballage, ou la gestion des déchets. En étant informé de l'empreinte écologique d'un produit, un consommateur peut adapter ses choix en fonction des enjeux environnementaux.
        L'objectif est de rendre ces informations accessibles pour encourager une consommation plus durable.
        """)

    with st.expander("3. Comment ce calculateur peut-il aider les consommateurs ?"):
        st.markdown("""
        Ce calculateur permet aux consommateurs de connaître l'impact environnemental des produits alimentaires qu'ils choisissent. En fonction des ingrédients et des procédés de fabrication, il calcule des indicateurs tels que les émissions de CO2, l'utilisation de l'eau et l'empreinte énergétique.
        Il permet ainsi d'agir concrètement en faveur de la planète.
        """)

    with st.expander("4. Pourquoi avons-nous choisi de nous baser sur Agribalyse ?"):
        st.markdown("""
        Agribalyse est une base de données officielle qui offre une analyse approfondie de l'impact environnemental des produits alimentaires. Son utilisation garantit la fiabilité et la rigueur scientifique de notre calculateur. En nous appuyant sur ces données, nous assurons aux utilisateurs des résultats précis et conformes aux standards de l'Analyse du Cycle de Vie (ACV).
        """)

    with st.expander("5. Quel est l'impact attendu de ce projet ?"):
        st.markdown("""
        L'impact attendu est de sensibiliser les consommateurs à l'impact environnemental de leurs choix alimentaires, et ainsi encourager une réduction de l'empreinte écologique à l'échelle individuelle et collective. Ce projet vise à favoriser des pratiques alimentaires durables, contribuant ainsi à une prise de conscience générale et à un changement des habitudes.
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)
# ========== STRUCTURE ==========
load_css()
create_navbar()
pourquoi_ce_projet_content()
create_footer()
