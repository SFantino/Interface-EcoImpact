import streamlit as st
import pandas as pd
import plotly.express as px

# ========== CONFIGURATION DE LA PAGE ==========
st.set_page_config(
    page_title="Calculateur | EcoImpact",
    layout="wide",
    page_icon="🧮",
    initial_sidebar_state="collapsed"
)

# ========== STYLE CSS ==========
def load_css():
    st.markdown("""
        <style>
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
                background: #F3F3F1;
                min-height: calc(100vh - 70px);
            }
            .content-behind {
                position: relative;
                z-index: 0;
                padding: 20px;
            }
            .calculator-container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                margin-bottom: 100px;
            }
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
            section[data-testid="stSidebar"], footer, header {
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

# ========== INITIALISATION ==========
load_css()
create_navbar()
st.markdown('<div class="content-behind">', unsafe_allow_html=True)
st.markdown("<h1 style='color:#000000;'>🧮 Calculateur d'Impact Écologique</h1>", unsafe_allow_html=True)
st.markdown('<div class="calculator-container">', unsafe_allow_html=True)

# ========== CALCULATEUR ==========
# Charger les données
@st.cache_data

def load_data():
    df = pd.read_csv("agribalyse-31-detail-par-etape.csv", delimiter=',', dtype=str)
    df_ingredients = pd.read_csv("Agribalyse_Detail ingredient.csv", delimiter=',', dtype=str)
    df_synthese = pd.read_csv("agribalyse-31-synthese.csv", delimiter=',', dtype=str)
    return df, df_ingredients, df_synthese

df, df_ingredients, df_synthese = load_data()

# Nettoyage
for dataframe in [df, df_ingredients, df_synthese]:
    dataframe.columns = dataframe.columns.str.strip()

unites_indicateurs = { ... }  # À compléter avec le même dictionnaire que précédemment

if "panier" not in st.session_state:
    st.session_state.panier = []

# Ajout produit
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

# Panier
st.subheader("📦 Votre panier")
if st.session_state.panier:
    for index, item in enumerate(st.session_state.panier):
        col1, col2 = st.columns([4, 1])
        col1.write(f"🔹 {item['nom']}")
        if col2.button("❌", key=f"remove_{index}"):
            del st.session_state.panier[index]
            st.rerun()
else:
    st.info("Votre panier est vide.")

# Calcul indicateurs
...  # Intégrer ici les fonctions de calcul et d'affichage existantes

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
create_footer()
