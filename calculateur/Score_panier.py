import streamlit as st
import pandas as pd
import streamlit.components.v1 as components  # Import nécessaire

# Charger la base de données
df_synthese_finale = pd.read_csv("Synthese_finale.csv")

# Bornes des classes (min inclus, max exclu sauf dernière classe)
classes_bornes = [
    (-float('inf'), -0.4, "A+", "#1a7f37"),
    (-0.4, -0.2, "A-", "#33a04f"),
    (-0.2, 0.05, "B+", "#c4d82c"),
    (0.05, 0.45, "B-", "#e6de26"),
    (0.45, 1, "C+", "#f4bc1c"),
    (1, 2, "C-", "#f89f1b"),
    (2, 3.4, "D+", "#f36b1c"),
    (3.4, 5, "D-", "#ea3223"),
    (5, 6, "E+", "#d32f2f"),
    (6, float('inf'), "E-", "#a10e0e")
]

def obtenir_classe(score):
    for borne_min, borne_max, classe, couleur in classes_bornes:
        if borne_min <= score < borne_max:
            return classe
    return "E-"

def construire_barre(score):
    # On fixe les bornes min et max globales (visible dans la barre)
    borne_min = -0.4  # borne inférieure réelle (début A+)
    borne_max = 6     # borne supérieure réelle (fin E+)

    # Clamp score entre borne_min et borne_max pour l’affichage
    score_clampe = min(max(score, borne_min), borne_max)

    # Calcule la largeur totale à afficher (borne_max - borne_min)
    largeur_totale = borne_max - borne_min

    segments_html = []
    position_curseur = (score_clampe - borne_min) / largeur_totale

    # Parcours des classes, crée les segments jusqu'à la classe contenant score
    stop_color = False
    somme_largeur_color = 0

    for i, (b_min, b_max, classe, couleur) in enumerate(classes_bornes):
        # Limiter bornes au cadre borne_min / borne_max
        seg_min = max(b_min, borne_min)
        seg_max = min(b_max, borne_max)
        if seg_min >= seg_max:
            continue  # classe hors bornes affichées

        largeur_segment = seg_max - seg_min
        proportion_segment = largeur_segment / largeur_totale

        if stop_color:
            # Segment gris après score panier
            segments_html.append(f'<div style="flex:{proportion_segment}; background:#eee; height:100%;"></div>')
        else:
            # Vérifier si le score est dans cette classe
            if seg_min <= score_clampe < seg_max:
                # Largeur colorée jusqu'au score
                largeur_couleur = (score_clampe - seg_min) / largeur_segment
                largeur_grise = 1 - largeur_couleur
                if largeur_couleur > 0:
                    segments_html.append(f'<div style="flex:{largeur_couleur * proportion_segment}; background:{couleur}; height:100%;"></div>')
                if largeur_grise > 0:
                    segments_html.append(f'<div style="flex:{largeur_grise * proportion_segment}; background:#eee; height:100%;"></div>')
                stop_color = True
            elif seg_max <= score_clampe:
                # Segment complètement coloré (score plus grand)
                segments_html.append(f'<div style="flex:{proportion_segment}; background:{couleur}; height:100%;"></div>')
            else:
                # Score plus petit que cette classe, segment gris
                segments_html.append(f'<div style="flex:{proportion_segment}; background:#eee; height:100%;"></div>')
                stop_color = True

    curseur_position_pct = position_curseur * 100

    curseur_html = f'''
    <div style="position: absolute; left: {curseur_position_pct}%; top: 0; bottom: 0; width: 2px; background: black;"></div>
    '''

    barre_html = f'''
    <div style="position: relative; height: 30px; border-radius: 5px; display: flex; overflow: hidden; border: 1px solid #ccc;">
        {''.join(segments_html)}
        {curseur_html}
        <span style="position: absolute; left: 0; top: 5px; font-weight: bold;">{borne_min:.2f}</span>
        <span style="position: absolute; right: 0; top: 5px; font-weight: bold;">{borne_max:.2f}</span>
    </div>
    '''

    return barre_html

def score_panier():
    if "panier" not in st.session_state or not st.session_state.panier:
        st.info("Votre panier est vide.")
        return

    codes_ciqual_panier = [p["code_ciqual"] for p in st.session_state.panier]
    df_panier = df_synthese_finale[df_synthese_finale["Code CIQUAL"].isin(codes_ciqual_panier)]

    if df_panier.empty:
        st.warning("Aucun produit du panier trouvé dans la base.")
        return

    st.subheader("📊 Résultats du panier")

    if "Score Statistique Standardisé" in df_synthese_finale.columns:
        score_col = "Score Statistique Standardisé"
        score_min = df_synthese_finale[score_col].min()
        score_max = df_synthese_finale[score_col].max()
        score_moyen = df_panier[score_col].mean()

        classe_panier = obtenir_classe(score_moyen)

        st.markdown(
            f"**Score moyen panier (Standardisé):** {score_moyen:.2f}  \n"
            f"Classe panier: {classe_panier}"
        )

        barre_html = construire_barre(score_moyen)

        st.markdown(barre_html, unsafe_allow_html=True)

    # Score unique EF
    if "Score unique EF" in df_synthese_finale.columns:
        score_col = "Score unique EF"
        score_min = df_synthese_finale[score_col].min()
        score_max = df_synthese_finale[score_col].max()
        score_moyen = df_panier[score_col].mean()

        scores_sg = df_synthese_finale.groupby("Sous-groupe d'aliment")[score_col].mean()
        sg_panier = df_panier["Sous-groupe d'aliment"].unique()
        score_moyen_sg = scores_sg.loc[sg_panier].mean()

        st.markdown(f"**Score environnemental moyen (EF):** {score_moyen:.2f}  \n"
                    f"Score moyen sous-groupes EF: {score_moyen_sg:.2f}")

        st.progress((score_moyen - score_min) / (score_max - score_min))
        st.progress((score_moyen_sg - score_min) / (score_max - score_min))

    # Note panier
    if "note_y" in df_synthese_finale.columns:
        note_panier = df_panier["note_y"].mean()
        notes_sg = df_synthese_finale.groupby("Sous-groupe d'aliment")["note_y"].mean()
        sg_panier = df_panier["Sous-groupe d'aliment"].unique()
        note_sg = notes_sg.loc[sg_panier].mean()

        st.markdown(f"**Note moyenne panier:** {note_panier:.2f}  \n"
                    f"Note moyenne sous-groupes: {note_sg:.2f}")
