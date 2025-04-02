import streamlit as st

st.set_page_config(page_title="Calculateur | EcoImpact", layout="wide")

st.markdown("""
    <style>
        /* [Reprendre le même CSS que main.py si nécessaire] */
    </style>
""", unsafe_allow_html=True)

st.title("🔢 Calculateur d'Impact Environnemental")
st.write("""
Cette page contient notre outil de calcul d'impact environnemental.
         
(Insérez ici votre formulaire de calcul)
""")

# Exemple de composant de calcul
with st.form("calcul_form"):
    st.selectbox("Type d'activité", ["Transport", "Énergie", "Alimentation"])
    st.number_input("Quantité", min_value=0)
    submitted = st.form_submit_button("Calculer")
    if submitted:
        st.success("Calcul effectué!")
