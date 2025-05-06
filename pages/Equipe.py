import streamlit as st
from design import load_css, create_navbar, create_footer

# ========== CONTENU ==========

def equipe_content():
    st.markdown('<div class="content-behind">', unsafe_allow_html=True)
    
    st.markdown("<h1 style='color:#000000;'>👥 L'Équipe</h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <p style="color: #000000;">Nous sommes un groupe d'étudiants en 4ème année d'ingénierie agroalimentaire à UniLaSalle Beauvais, engagés dans la réduction de l'impact environnemental des produits alimentaires. Notre équipe est composée de :</p>
        <ul style="color: #000000;">
            <li><strong>Yaël BALIABA</strong></li>
            <li><strong>Grégoire BESSON</strong></li>
            <li><strong>Samantha FANTINO</strong></li>
            <li><strong>Quentin GRIZARD</strong></li>
            <li><strong>François JONARD</strong></li>
            <li><strong>Landry MACQUET</strong></li>
        </ul>
    """, unsafe_allow_html=True)

# ========== STRUCTURE ==========

load_css()
create_navbar()
equipe_content()
create_footer()

