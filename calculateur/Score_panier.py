import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Reprendre df_synthese_finale et obtenir_classe()

def plot_score_bar(score_panier, score_sous_groupes, score_min, score_max):
    classes = {
        "A+": (-np.inf, -0.4),
        "A-": (-0.4, -0.2),
        "B+": (-0.2, 0.05),
        "B-": (0.05, 0.45),
        "C+": (0.45, 1),
        "C-": (1, 2),
        "D+": (2, 3.4),
        "D-": (3.4, 5),
        "E+": (5, 6),
        "E-": (6, np.inf)
    }
    
    # Normaliser les bornes entre 0 et 1
    norm = lambda x: (x - score_min) / (score_max - score_min)
    
    fig, ax = plt.subplots(figsize=(8, 1.5))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    # Dessiner les segments de classes
    for i, (classe, (low, high)) in enumerate(classes.items()):
        left = max(0, norm(low))
        right = min(1, norm(high))
        ax.fill_between([left, right], 0.25, 0.75, color=f"C{i%10}", alpha=0.4)
        ax.text((left + right) / 2, 0.8, classe, ha='center', va='center', fontsize=9)
    
    # Ajouter curseur score panier
    x_panier = np.clip(norm(score_panier), 0, 1)
    ax.plot([x_panier, x_panier], [0.1, 0.9], color='black', linewidth=2, label="Score panier")
    ax.text(x_panier, 0.95, f"Panier: {score_panier:.2f}", ha='center', fontsize=10, fontweight='bold')
    
    # Ajouter curseur score moyen sous-groupes
    x_sous_groupes = np.clip(norm(score_sous_groupes), 0, 1)
    ax.plot([x_sous_groupes, x_sous_groupes], [0.1, 0.9], color='red', linewidth=2, linestyle='--', label="Moyenne sous-groupes")
    ax.text(x_sous_groupes, 0.05, f"Moyenne SG: {score_sous_groupes:.2f}", ha='center', fontsize=9, color='red')

    ax.legend(loc='upper right', fontsize=8)
    st.pyplot(fig)

def score_panier():
    if "panier" not in st.session_state or not st.session_state.panier:
        st.info("Votre panier est vide.")
        return

    codes_ciqual_panier = [p["code_ciqual"] for p in st.session_state.panier]
    df_panier = df_synthese_finale[df_synthese_finale["Code CIQUAL"].isin(codes_ciqual_panier)]

    if df_panier.empty:
        st.warning("Aucun produit du panier trouvé dans la base.")
        return

    sous_groupes_panier = df_panier["Sous-groupe d'aliment"].dropna().unique()

    score_min = df_synthese_finale["Score Statistique Standardisé"].min()
    score_max = df_synthese_finale["Score Statistique Standardisé"].max()

    score_moyen_panier = df_panier["Score Statistique Standardisé"].mean()

    scores_moyens_sous_groupes = df_synthese_finale.groupby("Sous-groupe d'aliment")["Score Statistique Standardisé"].mean()
    score_moyen_sous_groupes = scores_moyens_sous_groupes.loc[sous_groupes_panier].mean()

    st.subheader("Score moyen du panier vs score moyen des sous-groupes présents")
    plot_score_bar(score_moyen_panier, score_moyen_sous_groupes, score_min, score_max)
