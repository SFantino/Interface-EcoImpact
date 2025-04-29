import streamlit as st
import pandas as pd

def gerer_panier():
    df_synthese_finale = pd.read_csv("Synthese_finale.csv")

    if "panier" not in st.session_state:
        st.session_state.panier = []

    if "dernier_produit_selectionne" not in st.session_state:
        st.session_state.dernier_produit_selectionne = None

    st.markdown("""
        <style>
        .stTextInput input {
            color: black !important;
            background-color: white !important;
        }
        .stTextInput label {
            color: black !important;
        }
        div[data-baseweb="select"] * {
            color: black !important;
            background-color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("🛍️ Gestion du Panier")

    search_query = st.text_input("🔍 Recherchez un produit par nom")

    if search_query:
        produits_trouves = df_synthese_finale[df_synthese_finale["Nom du Produit en Français"].str.contains(search_query, case=False, na=False)]

        if not produits_trouves.empty:
            liste_produits = [""] + list(produits_trouves["Nom du Produit en Français"].unique())

            st.markdown("#### 📌 Sélectionnez un produit :", unsafe_allow_html=True)
            produit_selectionne = st.selectbox(label="", options=liste_produits)

            if produit_selectionne and produit_selectionne != "":
                code_ciqual = df_synthese_finale[df_synthese_finale["Nom du Produit en Français"] == produit_selectionne]["Code CIQUAL"].values[0]

                if not any(p["nom"] == produit_selectionne for p in st.session_state.panier):
                    st.session_state.panier.append({"nom": produit_selectionne, "code_ciqual": code_ciqual})
                    st.session_state.dernier_produit_selectionne = produit_selectionne
                    st.success(f"✅ {produit_selectionne} ajouté au panier.")
                    st.rerun()
        else:
            st.warning("❌ Aucun produit trouvé.")

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
