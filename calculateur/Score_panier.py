import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import plotly.graph_objects as go

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

    colors = [
        "#005e00", "#198c19", "#7cc37c", "#cedf00", "#e6c000",
        "#ffa500", "#ff7f50", "#ff3c00", "#d60000", "#8b0000"
    ]

    norm = lambda x: (x - score_min) / (score_max - score_min)

    fig = go.Figure()

    x0 = 0
    for i, (classe, (low, high)) in enumerate(classes.items()):
        x_start = max(0, norm(low))
        x_end = min(1, norm(high))
        width = x_end - x_start
        if width <= 0:
            continue
        fig.add_trace(go.Bar(
            x=[width],
            y=["Classe"],
            orientation='h',
            marker=dict(color=colors[i % len(colors)]),
            name=classe,
            hovertemplate=f"{classe}<extra></extra>",
            showlegend=True
        ))

    x_panier = np.clip(norm(score_panier), 0, 1)
    x_sg = np.clip(norm(score_sous_groupes), 0, 1)

    fig.add_vline(x=x_panier, line_width=3, line_dash="solid", line_color="black",
                  annotation_text=f"Panier: {score_panier:.2f}", annotation_position="top")
    fig.add_vline(x=x_sg, line_width=2, line_dash="dash", line_color="red",
                  annotation_text=f"Sous-groupes: {score_sous_groupes:.2f}", annotation_position="bottom")

    fig.update_layout(
        barmode='stack',
        xaxis=dict(range=[0,1], showticklabels=False),
        yaxis=dict(showticklabels=False),
        height=150,
        margin=dict(l=20, r=20, t=40, b=20),
        showlegend=True
    )

    st.plotly_chart(fig, use_container_width=True)
