import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Calculateur | EcoImpact",
    layout="wide",
    page_icon="🧮",
    initial_sidebar_state="collapsed"  # <- Important
)

# ========== CSS (COPIER-COLLER DU MAIN.PY) ==========
st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            position: fixed;
            top: 0;
            left: 0;
            width: 100% !important;
            height: 70px !important;
            background: transparent;
            padding: 15px 20px;
            z-index: 1000;
            display: flex;
            justify-content: flex-end;
            align-items: center;
            box-shadow: none;
        }
        .stSidebar a {
            color: black !important;
            text-decoration: none;
            font-size: 20px !important;
            font-weight: bold !important;
            margin: 0 15px !important;
        }
        .stSidebar a:hover {
            color: #4CAF50 !important;
        }
        /* ... (Tout le reste du CSS de main.py) ... */
    </style>
""", unsafe_allow_html=True)

# ========== NAVBAR (identique à main.py) ==========
with st.sidebar:
    st.markdown("""
        <div class="stSidebar">
            <a href="/" target="_self">Accueil</a>
            <a href="/Calculateur" target="_self" style="color: #4CAF50 !important;">Calculateur</a>
            <a href="/Ressources" target="_self">Ressources</a>
            <a href="/Methodologie" target="_self">Méthodologie</a>
        </div>
    """, unsafe_allow_html=True)


# ========== CONTENU PRINCIPAL ==========
st.markdown('<div class="content-behind">', unsafe_allow_html=True)

# Titre et description
st.markdown("""
    <h1 style='color: black;'>🧮 Calculateur d'Impact Écologique</h1>
    <div style="margin-bottom: 30px; color: black;">
        Calculez votre empreinte environnementale en fonction de vos activités quotidiennes.
    </div>
""", unsafe_allow_html=True)

# Conteneur du formulaire
st.markdown('<div class="calculator-container">', unsafe_allow_html=True)

with st.form("calcul_form"):
    col1, col2 = st.columns(2)
    with col1:
        type_activite = st.selectbox(
            "Type d'activité",
            ["Transport", "Énergie", "Alimentation", "Logement", "Numérique"],
            help="Sélectionnez le domaine d'activité à évaluer"
        )
    with col2:
        quantite = st.number_input(
            "Quantité", 
            min_value=0, 
            step=1,
            help="Quantité associée à cette activité (km, kWh, kg, etc.)"
        )
    
    # Bouton de calcul
    if st.form_submit_button("Calculer l'impact", help="Cliquez pour calculer votre impact environnemental"):
        # Ici vous pourriez ajouter votre logique de calcul
        st.success(f"Calcul pour {quantite} unités de {type_activite}")
        # Affichage des résultats
        with st.expander("📊 Voir les résultats détaillés"):
            st.write("""
            **Détail des émissions:**
            - CO2: XX kg
            - Equivalent carbone: XX kg
            - Comparaison: XX arbres nécessaires pour compenser
            """)
            
            # Graphique exemple (à remplacer par vos données)
            st.bar_chart({"Transport": [quantite*0.2], "Moyenne nationale": [quantite*0.15]})

st.markdown('</div>', unsafe_allow_html=True)

# ========== FOOTER ==========
st.markdown("""
    <div class="footer-banner">
        <a href="/A_propos" target="_self">À propos</a>
        <img src="unilasalle_beauvais_logo.jpg" alt="Logo UniLaSalle Beauvais">
    </div>
""", unsafe_allow_html=True)
