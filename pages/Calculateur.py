import streamlit as st

st.set_page_config(page_title="Calculateur | EcoImpact", layout="wide")

# MÊME CSS QUE MAIN.PY (copier-collez exactement le même <style>)

# Barre de navigation (identique)
st.markdown("""
    <div class="navbar">
        <a href="/" target="_self">Accueil</a>
        <a href="/Calculateur" target="_self" style="color: #4CAF50; font-weight: bolder;">Calculateur</a>
        <a href="/Ressources" target="_self">Ressources</a>
        <a href="/Methodologie" target="_self">Méthodologie</a>
    </div>
""", unsafe_allow_html=True)

# Contenu calculateur
st.markdown('<div class="content-behind">', unsafe_allow_html=True)
st.title("🧮 Calculateur d'Impact Écologique")

with st.form("calcul_form"):
    col1, col2 = st.columns(2)
    with col1:
        type_activite = st.selectbox(
            "Type d'activité",
            ["Transport", "Énergie", "Alimentation", "Logement"]
        )
    with col2:
        quantite = st.number_input("Quantité", min_value=0, step=1)
    
    if st.form_submit_button("Calculer l'impact"):
        st.success(f"Calcul pour {quantite} unités de {type_activite}")

# Même footer que main.py
