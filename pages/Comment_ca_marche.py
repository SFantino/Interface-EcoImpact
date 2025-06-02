import streamlit as st
from design import load_css, create_navbar, create_footer


# ========== CONFIGURATION ==========
st.set_page_config(
    page_title="Comment ça marche ? | EcoImpact",
    layout="wide",
    page_icon="📊",
    initial_sidebar_state="collapsed"
)

# ========== CONTENU ==========
def afficher_comment_ca_marche():
    st.title("Comment ça marche ?")

    st.markdown("## 🌱 Analyse du cycle de vie (ACV)")
    st.markdown("""
    Notre outil repose sur **l'Analyse de Cycle de Vie (ACV)**, une méthode normalisée (ISO 14040/44) qui quantifie les impacts environnementaux d’un produit **de sa production à sa fin de vie**.

    Pour un aliment, cela comprend :
    - la culture ou l’élevage
    - la transformation
    - l’emballage
    - le transport
    - la distribution
    - la consommation
    - la gestion des déchets

    Les données utilisées proviennent de la base **Agribalyse** de l’ADEME, qui fournit des indicateurs pour plus de 2 500 produits alimentaires représentatifs de la consommation en France.
    """)

    st.markdown("## 🔬 Indicateurs environnementaux")
    st.markdown("""
    Nous utilisons les **16 indicateurs ACV** définis par Agribalyse. Les principaux affichés dans notre outil sont :

    - **Changement climatique** (kg CO₂ éq.)
    - **Utilisation de l’eau** (m³ monde éq. privation)
    - **Eutrophisation** (eau douce et marine)
    - **Particules fines** (impact santé)
    - **Épuisement des ressources fossiles** (MJ)
    - **Occupation des sols**

    Ces indicateurs sont **pondérés, normalisés et agrégés** pour construire un score unique.
    """)

    st.markdown("## 🧮 Méthodologie de calcul")
    st.markdown("""
    Chaque produit est évalué à partir de ses impacts unitaires (par kg) selon Agribalyse, **ajustés à la portion sélectionnée**. Le score global est obtenu en :

    1. **Normalisant** les impacts par rapport à une base annuelle moyenne d’un Français
    2. **Pondérant** les indicateurs selon leur gravité environnementale (selon ReCiPe 2016)
    3. **Agrégant** le tout en un indice synthétique

    Le score final est **ramené sur une échelle de type A à E** pour faciliter la lecture :
    - **A** = faible impact
    - **E** = impact élevé
    """)

    st.markdown("## 🧺 Fonctionnement du panier")
    st.markdown("""
    Vous pouvez composer un panier alimentaire et visualiser son **impact cumulé**. Chaque produit ajouté est converti en impacts environnementaux, puis agrégé à l’échelle du panier total.

    Cela permet :
    - d’**évaluer l’empreinte d’un repas** ou d’une journée type
    - de **comparer plusieurs scénarios alimentaires**
    - de **simuler l’effet d’un changement d’aliment**

    C’est un outil d’aide à la décision pour **réduire son impact environnemental**, basé sur des données scientifiques.
    """)

    st.markdown("## 📚 Sources")
    st.markdown("""
    - **Agribalyse 3.1**, ADEME (https://agribalyse.ademe.fr)
    - **Méthodologie ReCiPe 2016**
    - **Normes ISO 14040 / 14044**
    """)

# ========== STRUCTURE ==========
load_css()
create_navbar()
methodo_content()
create_footer()
