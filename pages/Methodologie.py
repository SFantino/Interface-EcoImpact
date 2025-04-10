import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Méthodologie | EcoImpact", 
    layout="wide",
    page_icon="📊"
)

# ========== CSS IDENTIQUE À MAIN.PY ==========
# [Même CSS que dans Calculateur.py]

# ========== BARRE DE NAVIGATION ==========
st.markdown("""
    <div class="navbar">
        <a href="/" target="_self">Accueil</a>
        <a href="/Calculateur" target="_self">Calculateur</a>
        <a href="/Ressources" target="_self">Ressources</a>
        <a href="/Methodologie" target="_self" style="color: #4CAF50; font-weight: bolder;">Méthodologie</a>
    </div>
""", unsafe_allow_html=True)

# ========== CONTENU PRINCIPAL ==========
st.markdown('<div class="content-behind">', unsafe_allow_html=True)

# Titre et introduction
st.title("📊 Méthodologie Scientifique")
st.markdown("""
    <div style="margin-bottom: 30px;">
        Découvrez les fondements scientifiques de notre calculateur d'impact environnemental.
    </div>
""", unsafe_allow_html=True)

# Conteneur du contenu
st.markdown('<div class="calculator-container">', unsafe_allow_html=True)

# Sections de méthodologie
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔍 Sources de données")
    st.markdown("""
    - **Base Carbone® ADEME**: Référence française
    - **Données INSEE**: Statistiques nationales
    - **Études scientifiques**: Publications peer-reviewed
    - **Données sectorielles**: Rapports d'entreprises
    """)

with col2:
    st.subheader("🧪 Méthodes de calcul")
    st.markdown("""
    - Approche cycle de vie (ACV)
    - Facteurs d'émission standardisés
    - Méthodologie GHG Protocol
    - Calculs en équivalent CO2
    """)

# Section détaillée
st.subheader("📝 Détail des calculs")
with st.expander("Voir la méthodologie complète"):
    st.markdown("""
    ### Formule générale:
    ```
    Emission = Activité × Facteur d'émission × Coefficient
    ```
    
    ### Exemple pour le transport:
    ```python
    def calcul_transport(km, type_vehicule):
        facteurs = {
            "Voiture": 0.12,
            "Bus": 0.06,
            "Train": 0.02
        }
        return km * facteurs[type_vehicule]
    ```
    
    ### Coefficients utilisés:
    | Catégorie | Coefficient |
    |-----------|------------|
    | Transport | 0.12 kg/km |
    | Électricité | 0.45 kg/kWh |
    """)

st.markdown('</div>', unsafe_allow_html=True)

# ========== FOOTER ==========
# [Identique au footer de Calculateur.py]
