import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Ressources", page_icon="📚", layout="wide")

# Style CSS pour le bandeau et les liens
st.markdown("""
    <style>
        .navbar {
            background-color: #e8e8e8;
            padding: 10px;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
        }
        .navbar a {
            color: black;
            text-decoration: none;
            margin: 0 15px;
        }
        .navbar a:hover {
            color: #4CAF50;
        }
        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f9f9f9;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
        }
        .dropdown:hover .dropdown-content {
            display: block;
        }
        .dropdown-content a {
            color: black;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
            text-align: left;
        }
        .dropdown-content a:hover {
            background-color: #f1f1f1;
        }
    </style>
""", unsafe_allow_html=True)

# Bandeau de navigation
st.markdown("""
    <div class="navbar">
        <a href="/">Accueil</a>
        <div class="dropdown">
            <a href="#">Méthodologie</a>
            <div class="dropdown-content">
                <a href="/Méthodologie/Analyse_du_cycle_de_vie">Analyse du cycle de vie</a>
                <a href="/Méthodologie/Autre_sous_page">Autre sous-page</a>
            </div>
        </div>
        <a href="/Ressources">Ressources</a>
    </div>
""", unsafe_allow_html=True)

# Contenu de la page Ressources
st.title("Ressources")
st.write("Cette page contient des ressources utiles pour notre projet.")
