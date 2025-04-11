import streamlit as st
import pandas as pd
import plotly.express as px

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
                background-color: #004b6d;  /* Changer ici la couleur de fond de la navbar */
                padding: 15px 20px;
                z-index: 1000;
                display: flex;
                justify-content: flex-end;
                align-items: center;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            
            .navbar a {
                color: white;  /* Couleur du texte des liens */
                text-decoration: none;
                font-size: 20px;
                font-weight: bold;
                margin: 0 15px;
            }
            
            .navbar a:hover {
                color: #f1f1f1;  /* Changer la couleur du texte lors du survol */
            }
            
            .stApp {
                margin-top: 70px;
                background-color: #f5f7fa;  /* Couleur de fond de l'application */
                min-height: calc(100vh - 70px);
            }
            
            .content-behind {
                padding: 20px 40px;
            }
            
            h1, h2, h3 {
                color: #2c3e50;  /* Changer la couleur des titres */
            }
            
            .methodo-card {
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

            .text {
                color: #333333 !important;  /* Couleur du texte */
            }

            .stButton > button {
                background-color: #004b6d;  /* Changer la couleur de fond des boutons */
                color: white;  /* Changer la couleur du texte des boutons */
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
            }

            .stButton > button:hover {
                background-color: #0177d4;  /* Changer la couleur de fond lors du survol des boutons */
            }

            .stSelectbox > div {
                background-color: #ffffff;  /* Changer la couleur de fond des selectbox */
                border: 1px solid #ddd;
                border-radius: 5px;
            }

            .stSelectbox > div:hover {
                border-color: #004b6d;  /* Changer la couleur du border lors du survol */
            }
        </style>
    """, unsafe_allow_html=True)

# ========== NAVBAR ========== 
def create_navbar():
    st.markdown("""
        <div class="navbar">
            <a href="/" target="_self">Accueil</a>
            <a href="/Calculateur" target="_self">Calculateur</a>
            <a href="/Ressources" target="_self">Ressources</a>
            <a href="/Methodologie" target="_self" style="color: #f1f1f1;">Méthodologie</a>
        </div>
    """, unsafe_allow_html=True)

# ========== CONTENU PRINCIPAL ========== 
def methodo_content():
    st.markdown('<div class="content-behind">', unsafe_allow_html=True)
    
    st.markdown("<h1 class='text' style='color:#333333;'>📊 Méthodologie Scientifique</h1>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ========== STRUCTURE PAGE ========== 
load_css()
create_navbar()

# ========== AFFICHAGE INTERFACE STREAMLIT ========== 
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
        col1, col2 = st.columns([4, 1])
        col1.write(f"🔹 {item['nom']}")
        if col2.button("❌", key=f"remove_{index}"):
            del st.session_state.panier[index]
            st.rerun()
else:
    st.info("Votre panier est vide.")

# Calcul et affichage des indicateurs environnementaux du panier
indicateurs_totaux, details_produits = calculer_indicateurs_panier()

if indicateurs_totaux is not None:
    st.subheader("📊 Indicateurs environnementaux du panier")

    df_indicateurs = pd.DataFrame({
        "Impact environnemental": indicateurs_totaux.index,
        "Valeur totale": indicateurs_totaux.values,
        "Unité": [unites_indicateurs.get(indicateur, "N/A") for indicateur in indicateurs_totaux.index]
    })

    st.dataframe(df_indicateurs.set_index("Impact environnemental"))

    selected_row = st.selectbox(
        "Sélectionnez un indicateur pour voir la contribution des produits",
        indicateurs_totaux.index
    )

    if selected_row:
        detail_impact = details_produits[selected_row]
        st.subheader(f"Contribution des produits pour {selected_row}")
        st.dataframe(detail_impact)
