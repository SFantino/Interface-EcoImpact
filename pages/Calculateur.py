import streamlit as st
import pandas as pd

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
    
# Charger les bases de données
df = pd.read_csv("agribalyse-31-detail-par-etape.csv", delimiter=',', dtype=str)
df_ingredients = pd.read_csv("Agribalyse_Detail ingredient.csv", delimiter=',', dtype=str)
df_synthese = pd.read_csv("agribalyse-31-synthese.csv", delimiter=',', dtype=str)

# Normaliser les noms de colonnes
df.columns = df.columns.str.strip()
df_ingredients.columns = df_ingredients.columns.str.strip()
df_synthese.columns = df_synthese.columns.str.strip()

# Dictionnaire des unités par indicateur
unites_indicateurs = {
    "Changement climatique": "kg CO2 eq",
    "Particules fines": "disease incidence",
    "Épuisement des ressources en eau": "m3 world eq",
    "Épuisement des ressources énergétiques": "MJ",
    "Usage des terres": "point",
    "Épuisement des ressources - minéraux": "kg Sb eq",
    "Appauvrissement de la couche d’ozone": "kg CFC-11 eq",
    "Acidification": "mol H+ eq",
    "Radiation ionisante, effet sur la santé": "kBq U235 eq",
    "Formation photochimique d’ozone": "kg NMVOC eq",
    "Eutrophisation, terrestre": "mol N eq",
    "Eutrophisation, marine": "kg N eq",
    "Eutrophisation, eau douce": "kg P eq",
    "Ecotoxicité d'eau douce": "CTUe",
    "Effets toxicologiques sur la santé humaine - non-cancérogènes": "CTUh",
    "Effets toxicologiques sur la santé humaine - cancérogènes": "CTUh",
}

# Initialiser le panier
if "panier" not in st.session_state:
    st.session_state.panier = []

# Fonction pour calculer les indicateurs du panier
def calculer_indicateurs_panier():
    if not st.session_state.panier:
        return None, None

    codes_ciqual = [item["code_ciqual"] for item in st.session_state.panier]
    produits_synthese = df_synthese[df_synthese["Code CIQUAL"].astype(str).isin(map(str, codes_ciqual))]

    if produits_synthese.empty:
        return None, None

    colonnes_impact = produits_synthese.columns[12:32]  
    produits_synthese[colonnes_impact] = produits_synthese[colonnes_impact].astype(float)

    total_impacts = produits_synthese.groupby("Code CIQUAL")[colonnes_impact].sum()
    total_somme = total_impacts.sum()

    return total_somme, total_impacts

# Interface Streamlit
st.title("Analyse des produits agro-alimentaires")

# Ajout d'un produit
if "ajouter_produit" not in st.session_state:
    st.session_state.ajouter_produit = True

if st.session_state.ajouter_produit:
    search_query = st.text_input("Recherchez un produit par nom")

    if search_query:
        produits_trouves = df_ingredients[df_ingredients["Nom Français"].str.contains(search_query, case=False, na=False)]
        
        if not produits_trouves.empty:
            produit_selectionne = st.selectbox("Sélectionnez un produit", produits_trouves["Nom Français"].unique())

            code_ciqual = produits_trouves[produits_trouves["Nom Français"] == produit_selectionne]["Ciqual  code"].values[0]
            st.success(f"Produit sélectionné : {produit_selectionne} (Code CIQUAL : {code_ciqual})")

            if st.button("Ajouter au panier"):
                st.session_state.panier.append({"nom": produit_selectionne, "code_ciqual": code_ciqual})
                st.session_state.ajouter_produit = False
                st.rerun()

if st.button("Ajouter un autre produit"):
    st.session_state.ajouter_produit = True
    st.rerun()

# Affichage du panier
st.subheader("📦 Votre panier")
if st.session_state.panier:
    for index, item in enumerate(st.session_state.panier):
        st.markdown(f"- {item['nom']}")
else:
    st.warning("Votre panier est vide.")

# Calcul des impacts environnementaux
total_impacts, impacts_detail = calculer_indicateurs_panier()
if total_impacts is not None:
    st.subheader("🔍 Détails des impacts environnementaux")
    st.write("Les impacts environnementaux totaux pour le panier sont :", total_impacts)
    st.write(impacts_detail)
# ========== STRUCTURE ========== 
load_css()
create_navbar()
calculateur_content()
create_footer()
