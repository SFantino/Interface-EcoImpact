import streamlit as st

# ========== CONFIGURATION ========== 
st.set_page_config(
    page_title="Calculateur | EcoImpact",
    layout="wide",
    page_icon="🌱",
    initial_sidebar_state="collapsed"
)

# ========== STYLE CSS ========== 
def load_css():
    st.markdown("""
        <style>
            /* Navbar identique à main.py */
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
            
            .stApp {
                margin-top: 70px !important;
                background-color: #F3F3F1;
                min-height: calc(100vh - 70px);
            }
            
            .content-behind {
                padding: 20px 40px;
            }
            
            h1, h2, h3 {
                color: #000000 !important;
            }
            
            .resource-card {
                background: white;
                border-radius: 10px;
                padding: 20px;
                margin-bottom: 20px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            
            section[data-testid="stSidebar"],
            footer,
            header {
                display: none !important;
            }
        </style>
    """, unsafe_allow_html=True)

# ========== COMPOSANTS ========== 
def create_navbar():
    st.markdown("""
        <div class="navbar">
            <a href="/" target="_self">Accueil</a>
            <a href="/Calculateur" target="_self" style="color: #4CAF50 !important;">Calculateur</a>
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

# ========== CALCULATEUR ========== 
def calculateur_content():
    st.markdown('<div class="content-behind">', unsafe_allow_html=True)
    
    st.markdown("<h1 style='color:#000000;'>🌱 Calculateur d'Impact Environnemental</h1>", unsafe_allow_html=True)
    
    # Formulaire pour le calculateur
    st.markdown("### Entrez les données de votre produit")
    
    # Inputs
    produit_nom = st.text_input("Nom du produit")
    categorie = st.selectbox("Catégorie du produit", ["Alimentaire", "Cosmétique", "Autre"])
    poids = st.number_input("Poids du produit (en kg)", min_value=0.01, value=0.1)
    production_energie = st.number_input("Énergie nécessaire à la production (en kWh)", min_value=0.01, value=1.0)
    transport_km = st.number_input("Distance de transport (en km)", min_value=1, value=100)
    transport_emissions = st.number_input("Émissions de CO2 par km (en g CO2)", min_value=0.1, value=100.0)
    
    # Calcul
    if st.button("Calculer l'impact environnemental"):
        # Calcul des émissions de CO2 pour le produit
        impact_energie = production_energie * 0.5  # Coefficient arbitraire pour l'impact énergie
        impact_transport = transport_km * transport_emissions / 1000  # CO2 total du transport (en kg)
        impact_total = impact_energie + impact_transport
        
        # Affichage du résultat
        st.write(f"**Impact environnemental total pour {produit_nom}** : {impact_total:.2f} kg CO2")
        
        # Afficher un message basé sur l'impact
        if impact_total < 1:
            st.success(f"Le produit {produit_nom} a un impact environnemental faible.")
        elif impact_total < 5:
            st.warning(f"Le produit {produit_nom} a un impact environnemental modéré.")
        else:
            st.error(f"Le produit {produit_nom} a un impact environnemental élevé.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# ========== STRUCTURE ========== 
load_css()
create_navbar()
calculateur_content()
create_footer()


