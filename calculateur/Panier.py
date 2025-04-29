import streamlit as st
import pandas as pd

def gerer_panier():
    # Charger la base de données
    df_synthese_finale = pd.read_csv("Synthese_finale.csv")

    # Initialisation du panier
    if "panier" not in st.session_state:
        st.session_state.panier = []

    if "dernier_produit_selectionne" not in st.session_state:
        st.session_state.dernier_produit_selectionne = None

    # Appliquer le style CSS pour changer la couleur du texte et du fond
    st.markdown("""
        <style>
        .stTextInput input {
            color: black !important;
            background-color: white !important;
        }
        .stTextInput label {
            color: black !important;
        }
        .stSelectbox label {
            color: black !important;
        }
        .stSelectbox div[role="combobox"] {
            color: black !important;
            background-color: white !important;
        }
        .stSelectbox div[role="listbox"] {
            color: black !important;
            background-color: white !important;
        }
        .stSelectbox div[role="option"] {
            color: black !important;
            background-color: white !important;
        }
        .stSelectbox div[role="option"]:hover {
            background-color: #f0f0f0 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Afficher le titre
    st.title("🛍️ Gestion du Panier")

    # Barre de recherche pour le produit
    search_query = st.text_input("🔍 Recherchez un produit par nom")

    # Logique de recherche et ajout au panier
    if search_query:
        produits_trouves = df_synthese_finale[df_synthese_finale["Nom du Produit en Français"].str.contains(search_query, case=False, na=False)]

        if not produits_trouves.empty:
            # Afficher un label pour sélectionner un produit
            st.markdown('<p style="color: black;">📌 Sélectionnez un produit :</p>', unsafe_allow_html=True)

            # Liste déroulante pour sélectionner un produit
            produit_selectionne = st.selectbox("", [""] + list(produits_trouves["Nom du Produit en Français"].unique()))

            if produit_selectionne and produit_selectionne != "":
                code_ciqual = df_synthese_finale[df_synthese_finale["Nom du Produit en Français"] == produit_selectionne]["Code CIQUAL"].values[0]

                # Ajouter au panier si ce n'est pas déjà fait
                if not any(p["nom"] == produit_selectionne for p in st.session_state.panier):
                    st.session_state.panier.append({"nom": produit_selectionne, "code_ciqual": code_ciqual})
                    st.session_state.dernier_produit_selectionne = produit_selectionne
                    st.success(f"✅ {produit_selectionne} ajouté au panier.")
                    st.rerun()
        else:
            st.warning("❌ Aucun produit trouvé.")

    # Affichage des produits dans le panier
    st.subheader("📦 Votre panier")
    if st.session_state.panier:
        for index, item in enumerate(st.session_state.panier):
            col1, col2 = st.columns([4, 1])
            col1.write(f"🔹 **{item['nom']}**")
            if col2.button("❌", key=f"remove_{index}"):
                st.session_state.panier.pop(index)
                st.rerun()
    else:
        st.info("🛒 Votre panier est vide.")
