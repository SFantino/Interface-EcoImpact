import streamlit as st
import pandas as pd
import plotly.express as px

# Fonction pour calculer l'impact environnemental
def calculate_eco_impact(data):
    # Effectuer les calculs en fonction des données
    impact_score = data['Carbon Footprint'] * 0.5 + data['Water Usage'] * 0.3 + data['Energy Consumption'] * 0.2
    return impact_score

# Contenu du calculateur
def main():
    # Définir le style de la page et de la navigation
    st.set_page_config(page_title="Calculateur d'Impact Environnemental", layout="wide")

    # Bandeau de navigation avec la même esthétique que la page d'accueil
    st.markdown("""
    <style>
    .navbar {
        background-color: #ffffff;
        padding: 10px;
        text-align: center;
        font-size: 20px;
        border-bottom: 2px solid #cccccc;
    }
    .navbar a {
        color: black;
        text-decoration: none;
        margin: 0 15px;
        font-weight: bold;
    }
    .navbar a:hover {
        color: #0078d4;
    }
    body {
        background-color: #f0f0f0;
        font-family: 'Arial', sans-serif;
    }
    </style>
    <div class="navbar">
        <a href="#">Accueil</a>
        <a href="#">Calculateur</a>
        <a href="#">Résultats</a>
    </div>
    """, unsafe_allow_html=True)

    # Titre de la page
    st.title("Calculateur d'Impact Environnemental")

    # Affichage d'un texte d'introduction
    st.write("Ce calculateur vous permet d'évaluer l'impact environnemental de vos produits.")

    # Charger les données (exemple)
    data = {
        "Product": ["Produit A", "Produit B", "Produit C"],
        "Carbon Footprint": [2.5, 3.0, 1.8],  # en kg CO2
        "Water Usage": [100, 120, 80],  # en L
        "Energy Consumption": [150, 180, 130]  # en kWh
    }
    
    df = pd.DataFrame(data)

    # Afficher les données dans un tableau
    st.subheader("Données des produits")
    st.dataframe(df)

    # Calculer l'impact environnemental
    df["Eco Impact Score"] = df.apply(calculate_eco_impact, axis=1)

    # Afficher les résultats
    st.subheader("Impact Environnemental Calculé")
    st.dataframe(df)

    # Afficher un graphique
    fig = px.bar(df, x='Product', y='Eco Impact Score', title='Score d\'impact environnemental des produits')
    st.plotly_chart(fig)

# Exécuter le calculateur
if __name__ == "__main__":
    main()
