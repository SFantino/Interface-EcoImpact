import streamlit as st

# ========== CONFIGURATION DE LA PAGE ==========
st.set_page_config(
    page_title="Calculateur | EcoImpact",
    layout="wide",
    page_icon="🧮",
    initial_sidebar_state="collapsed"
)

# ========== STYLE CSS (identique à main.py) ==========
def load_css():
    st.markdown("""
        <style>
            /* Navbar principale */
            .navbar {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 70px;
                background-color: #F3F3F1 !important;
                padding: 15px 20px;
                z-index: 1000;
                display: flex;
                justify-content: flex-end;
                align-items: center;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            
            .navbar a {
                color: black !important;
                text-decoration: none;
                font-size: 20px !important;
                font-weight: bold !important;
                margin: 0 15px !important;
            }
            
            .navbar a:hover {
                color: #4CAF50 !important;
            }
            
            /* Mise en page principale */
            .stApp {
                margin-top: 70px !important;
                background: #F3F3F1;
                min-height: calc(100vh - 70px);
            }
            
            /* Contenu */
            .content-behind {
                position: relative;
                z-index: 0;
                padding: 20px;
            }
            
            /* Styles spécifiques au calculateur */
            .calculator-container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                margin-bottom: 100px;
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
            
            /* Masquer éléments par défaut */
            section[data-testid="stSidebar"],
            footer,
            header {
                display: none !important;
            }
        </style>
    """, unsafe_allow_html=True)

# ========== COMPOSANTS COMMUNS ==========
def create_navbar():
    st.markdown("""
        <div class="navbar">
            <a href="/" target="_self">Accueil</a>
            <a href="/Calculateur" target="_self">Calculateur</a>
            <a href="/Ressources" target="_self">Ressources</a>
            <a href="/Methodologie" target="_self">Méthodologie</a>
        </div>
    """, unsafe_allow_html=True)

def create_footer():
    st.markdown("""
        <div class="footer-banner">
            <a href="/A_propos" target="_self">À propos</a>
            <img src="unilasalle_beauvais_logo.jpg" alt="Logo UniLaSalle Beauvais">
        </div>
    """, unsafe_allow_html=True)

# ========== CONTENU SPÉCIFIQUE AU CALCULATEUR ==========
def calculator_content():
    st.markdown('<div class="content-behind">', unsafe_allow_html=True)
    
    st.markdown("<h1 style='color:#000000;'>🧮 Calculateur d'Impact Écologique</h1>", unsafe_allow_html=True)
    
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
    st.markdown('</div>', unsafe_allow_html=True)

# ========== STRUCTURE PRINCIPALE ==========
load_css()
create_navbar()
calculator_content()
create_footer()
