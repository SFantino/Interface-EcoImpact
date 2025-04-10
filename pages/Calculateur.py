import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Calculateur | EcoImpact", 
    layout="wide",
    page_icon="🧮"
)

# ========== CSS IDENTIQUE À MAIN.PY ==========
st.markdown("""
    <style>
        /* Style pour le fond d'écran */
        .stApp {
            background: #F3F3F1;
            min-height: 100vh;
        }
        
        /* Style pour le bandeau de navigation */
        .navbar {
            position: fixed;
            top: 0;
            right: 0;
            left: 0;
            background-color: transparent;
            padding: 15px 20px;
            text-align: right;
            z-index: 1000;
            box-shadow: none;
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
        
        /* Zone de contenu principale */
        .content-behind {
            position: relative;
            z-index: 0;
            margin-top: 70px;
            padding: 20px;
        }
        
        /* Style pour le contenu du calculateur */
        .calculator-container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin-bottom: 100px;
        }
        
        /* Style pour le bandeau en bas de page */
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
        .footer-banner a {
            color: white;
            text-decoration: none;
            font-size: 20px;
            font-weight: bold;
        }
        .footer-banner a:hover {
            color: #F3F3F1;
        }
        .footer-banner img {
            height: 40px;
            margin-left: auto;
        }
        
        /* Masquer le footer et le header par défaut de Streamlit */
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ========== BARRE DE NAVIGATION ==========
st.markdown("""
    <div class="navbar">
        <a href="/" target="_self">Accueil</a>
        <a href="/Calculateur" target="_self" style="color: #4CAF50; font-weight: bolder;">Calculateur</a>
        <a href="/Ressources" target="_self">Ressources</a>
        <a href="/Methodologie" target="_self">Méthodologie</a>
    </div>
""", unsafe_allow_html=True)

# ========== CONTENU PRINCIPAL ==========
st.markdown('<div class="content-behind">', unsafe_allow_html=True)

# Titre et description
st.title("🧮 Calculateur d'Impact Écologique")
st.markdown("""
    <div style="margin-bottom: 30px;">
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
