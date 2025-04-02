import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Calculateur | EcoImpact",
    layout="wide"
)

# Reprendre le même CSS que main.py
st.markdown("""
    <style>
        /* Style pour le fond d'écran */
        .stApp {
            background: #F3F3F1 url('https://images.unsplash.com/photo-1514995669114-6081e934b693?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat left top / 65% auto;
            min-height: 100vh;
        }
        
        /* Style pour le bandeau de navigation */
        .navbar {
            position: fixed;
            top: 0;
            right: 0;
            left: 0;
            background-color: transparent;
            padding: 15px 20px;
            text-align: right;
            z-index: 1000;
            box-shadow: none;
        }
        .navbar a {
            color: black;
            text-decoration: none;
            font-size: 20px;
            font-weight: bold;
            margin: 0 15px;
        }
        .navbar a:hover {
            color: #4CAF50;
        }
        
        /* Zone de contenu principale */
        .content-behind {
            position: relative;
            z-index: 0;
            margin-top: 70px;
        }
        
        /* Style pour le bandeau en bas de page */
        .footer-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #23A95C;
            padding: 10px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 1001;
        }
        /* [Ajouter le reste de votre CSS] */
    </style>
""", unsafe_allow_html=True)

# Barre de navigation identique
st.markdown("""
    <div class="navbar">
        <a href="/" target="_self">Accueil</a>
        <a href="/Calculateur" target="_self" style="color: #4CAF50; font-weight: bolder;">Calculateur</a>
        <a href="/Ressources" target="_self">Ressources</a>
        <a href="/Methodologie" target="_self">Méthodologie</a>
    </div>
""", unsafe_allow_html=True)

# Contenu spécifique au calculateur
st.markdown('<div class="content-behind">', unsafe_allow_html=True)

st.title("🧮 Calculateur d'Impact Écologique")

# Exemple de formulaire de calcul
with st.form("calcul_form"):
    st.subheader("Entrez vos données")
    
    col1, col2 = st.columns(2)
    with col1:
        type_activite = st.selectbox(
            "Type d'activité",
            ["Transport", "Énergie", "Alimentation", "Logement"]
        )
    with col2:
        quantite = st.number_input("Quantité", min_value=0, step=1)
    
    if st.form_submit_button("Calculer l'impact"):
        st.success(f"Calcul en cours pour {quantite} unités de {type_activite}...")
        # Ici vous ajouteriez votre logique de calcul réelle

# Footer identique
st.markdown("""
    <div class="footer-banner">
        <a href="/A_propos" target="_self">À propos</a>
        <img src="unilasalle_beauvais_logo.jpg" alt="Logo UniLaSalle Beauvais">
    </div>
""", unsafe_allow_html=True)
