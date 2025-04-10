import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Ressources | EcoImpact", 
    layout="wide",
    page_icon="📚"
)

# ========== CSS IDENTIQUE À MAIN.PY ==========
# [Même CSS que dans Calculateur.py]

# ========== BARRE DE NAVIGATION ==========
st.markdown("""
    <div class="navbar">
        <a href="/" target="_self">Accueil</a>
        <a href="/Calculateur" target="_self">Calculateur</a>
        <a href="/Ressources" target="_self" style="color: #4CAF50; font-weight: bolder;">Ressources</a>
        <a href="/Methodologie" target="_self">Méthodologie</a>
    </div>
""", unsafe_allow_html=True)

# ========== CONTENU PRINCIPAL ==========
st.markdown('<div class="content-behind">', unsafe_allow_html=True)

# Titre et introduction
st.title("📚 Ressources Utiles")
st.markdown("""
    <div style="margin-bottom: 30px;">
        Retrouvez ici toutes les ressources pour approfondir votre connaissance de l'impact environnemental.
    </div>
""", unsafe_allow_html=True)

# Conteneur du contenu
st.markdown('<div class="calculator-container">', unsafe_allow_html=True)

# Sections de ressources
tab1, tab2, tab3 = st.tabs(["📄 Documents", "🛠 Outils", "🎓 Formations"])

with tab1:
    st.subheader("Documents de référence")
    st.markdown("""
    - [Guide ADEME](https://www.ademe.fr) - Référence française
    - [Rapport IPCC](https://www.ipcc.ch) - Données mondiales
    - [Rapport WWF](https://www.wwf.fr) - Biodiversité
    - [Eurostat](https://ec.europa.eu/eurostat) - Données européennes
    """)

with tab2:
    st.subheader("Outils complémentaires")
    st.markdown("""
    - [Nos Gestes Climat](https://nosgestesclimat.fr) - Calculateur personnel
    - [Global Footprint Network](https://www.footprintnetwork.org) - Empreinte écologique
    - [Carbon Calculator](https://www.carbonfootprint.com) - Calculateur international
    """)
    
    st.image("https://via.placeholder.com/800x400?text=Outils+Visuels", width=800)

with tab3:
    st.subheader("Formations et MOOC")
    st.markdown("""
    - [FUN MOOC](https://www.fun-mooc.fr) - Cours en ligne
    - [Coursera](https://www.coursera.org) - Formations environnement
    - [Udemy](https://www.udemy.com) - Cours pratiques
    """)

st.markdown('</div>', unsafe_allow_html=True)

# ========== FOOTER ==========
# [Identique au footer de Calculateur.py]
