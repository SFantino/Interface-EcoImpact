import streamlit as st
import pandas as pd

# Charger la base de données
df_synthese_finale = pd.read_csv("Synthese_finale.csv")

def obtenir_classe(score):
    if score < -0.4:
        return "A+"
    elif score < -0.2:
        return "A-"
    elif score < 0.05:
        return "B+"
    elif score < 0.45:
        return "B-"
    elif score < 1:
        return "C+"
    elif score < 2:
        return "C-"
    elif score < 3.4:
        return "D+"
    elif score < 5:
        return "D-"
    elif score < 6:
        return "E+"
    else:
        return "E-"

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

    # Score Statistique Standardisé
    if "Score Statistique Standardisé" in df_synthese_finale.columns:
        score_col = "Score Statistique Standardisé"
        score_min = df_synthese_finale[score_col].min()
        score_max = df_synthese_finale[score_col].max()
        score_moyen = df_panier[score_col].mean()

        scores_sg = df_synthese_finale.groupby("Sous-groupe d'aliment")[score_col].mean()
        sg_panier = df_panier["Sous-groupe d'aliment"].unique()
        score_moyen_sg = scores_sg.loc[sg_panier].mean()

        classe_panier = obtenir_classe(score_moyen)
        classe_sg = obtenir_classe(score_moyen_sg)

        st.markdown(f"**Score moyen panier (Standardisé):** {score_moyen:.2f}  \n"
                            f"Classe panier: {classe_panier}  \n"
                            f"Score moyen sous-groupes: {score_moyen_sg:.2f}  \n"
                            f"Classe sous-groupes: {classe_sg}")
        
        # Définir les bornes des classes et leurs couleurs associées
        classes = [
            ("A+", "#1a7f37"), ("A-", "#33a04f"),
            ("B+", "#c4d82c"), ("B-", "#e6de26"),
            ("C+", "#f4bc1c"), ("C-", "#f89f1b"),
            ("D+", "#f36b1c"), ("D-", "#ea3223"),
            ("E+", "#d32f2f"), ("E-", "#a10e0e")
        ]
        
        borne_totale = score_max - score_min
        segments = []
        valeur_relative = (score_moyen - score_min) / borne_totale
        
        segments = []
        
        for i, (classe, couleur) in enumerate(classes):
            debut = i / len(classes)
            fin = (i + 1) / len(classes)
            if valeur_relative > fin:
                segments.append(f'<div style="flex:1; background:{couleur}; height:100%;"></div>')
            elif valeur_relative > debut:
                largeur = (valeur_relative - debut) * len(classes)
                segments.append(f'<div style="flex:{largeur}; background:{couleur}; height:100%;"></div>')
                segments.append(f'<div style="flex:{1 - largeur}; background:#eee; height:100%;"></div>')
                break
            else:
                segments.append(f'<div style="flex:1; background:#eee; height:100%;"></div>')
        
        # Générer le curseur UNE SEULE FOIS après la boucle
        curseur_position = f"{valeur_relative * 100:.2f}%"
        curseur_html = f"""
        <div style="position: absolute; left: {curseur_position}; top: 0; bottom: 0; width: 2px; background: black;"></div>
        """
        
        # Générer la barre complète une seule fois
        bar_html = f"""
        <div style="position: relative; height: 30px; border-radius: 5px; display: flex; overflow: hidden;">
            {''.join(segments)}
            {curseur_html}
            <span style="position: absolute; left: 0; top: 5px; font-weight: bold;">{score_min:.2f}</span>
            <span style="position: absolute; right: 0; top: 5px; font-weight: bold;">{score_max:.2f}</span>
        </div>
        """
        
        # Affichage
        st.markdown(bar_html, unsafe_allow_html=True)


        

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

