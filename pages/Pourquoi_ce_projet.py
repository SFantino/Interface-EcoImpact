import streamlit as st
from design import load_css, create_navbar, create_footer

# ========== CONFIGURATION ==========
st.set_page_config(
    page_title="Pourquoi ce projet ? | EcoImpact",
    layout="wide",
    page_icon="🌍",
    initial_sidebar_state="collapsed"
)


# ========== CONTENU ==========
def ressources_content():
    st.markdown('<div class="content-behind">', unsafe_allow_html=True)
    
    st.markdown("<h1 style='color:#000000;'>🌍 Pourquoi ce projet ?", unsafe_allow_html=True)
    

    st.markdown('</div>', unsafe_allow_html=True)

# ========== STRUCTURE ==========
load_css()
create_navbar()
ressources_content()
create_footer()
