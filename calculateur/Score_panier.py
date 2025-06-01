import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

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

    # Palette de couleurs du vert foncé au rouge foncé
    couleurs = [
        "#00441b",  # A+ vert foncé
        "#006d2c",  # A-
        "#238b45",  # B+
        "#41ab5d",  # B-
        "#74c476",  # C+
        "#a1d99b",  # C-
        "#fdae6b",  # D+
        "#f16913",  # D-
        "#d94801",  # E+
        "#7f2704",  # E- rouge foncé
    ]

    # Normalisation entre score_min et score_max
    norm = lambda x: (x - score_min) / (score_max - score_min)

    fig, ax = plt.subplots(figsize=(9, 1.8))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Tracer les segments de classes colorés
    for i, (classe, (low, high)) in enumerate(classes.items()):
        left = max(0, norm(low))
        right = min(1, norm(high))
        ax.fill_between([left, right], 0.3, 0.7, color=couleurs[i], alpha=0.8)
        ax.text((left + right) / 2, 0.75, classe, ha='center', va='center', fontsize=10, fontweight='bold', color='white')

    # Ajouter les bornes -∞ et +∞ aux extrémités pour le score panier
    ax.text(0, 0.15, "-∞", ha='center', va='center', fontsize=9, fontweight='bold')
    ax.text(1, 0.15, "+∞", ha='center', va='center', fontsize=9, fontweight='bold')

    # Ajouter curseur score panier
    x_panier = np.clip(norm(score_panier), 0, 1)
    ax.plot([x_panier, x_panier], [0.1, 0.9], color='black', linewidth=3, label="Score panier")
    ax.text(x_panier, 0.95, f"Panier: {score_panier:.2f}", ha='center', fontsize=11, fontweight='bold')

    # Ajouter curseur score moyen sous-groupes
    x_sous_groupes = np.clip(norm(score_sous_groupes), 0, 1)
    ax.plot([x_sous_groupes, x_sous_groupes], [0.15, 0.85], color='red', linewidth=2, linestyle='--', label="Moyenne sous-groupes")
    ax.text(x_sous_groupes, 0.05, f"Moyenne SG: {score_sous_groupes:.2f}", ha='center', fontsize=9, color='red')

    ax.legend(loc='upper right', fontsize=9)
    st.pyplot(fig)
