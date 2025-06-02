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
def methodo_content():
    st.markdown('<div class="content-behind">', unsafe_allow_html=True)
    
    st.markdown("<h1 style='color:#000000;'>📊 Comment ça marche ?</h1>", unsafe_allow_html=True)
    st.markdown("## 🧪 Méthodologie de calcul environnemental")

    st.markdown("""
    Cette interface évalue l'impact environnemental d'un panier alimentaire selon la méthode d’**Analyse de Cycle de Vie (ACV)**.  
    L’outil utilise la base **Agribalyse 3.1** qui fournit les impacts moyens de plus de 2 500 produits alimentaires.

    Le calcul suit plusieurs étapes successives, combinant normalisation, pondération, agrégation et classification.
    """)

    st.markdown("### 1. Normalisation des indicateurs")

    st.markdown("""
    Chaque indicateur environnemental (par exemple émissions de CO₂, consommation d’eau, pollution des sols) est normalisé par rapport à une valeur de référence nationale issue de la base **Base Empreinte (ADEME)**.  
    Cette normalisation permet d'exprimer chaque impact sur une échelle comparable, sans unité.

    Formellement, pour un indicateur \( i \) et un produit \( p \) :

    $$
    I_{norm}(p,i) = \\frac{I(p,i)}{I_{ref}(i)}
    $$

    où \( I(p,i) \) est l’impact du produit \( p \) sur l’indicateur \( i \), et \( I_{ref}(i) \) la valeur de référence annuelle pour la France.
    """)

    st.markdown("### 2. Agrégation par pondération ReCiPe")

    st.markdown("""
    Chaque indicateur normalisé est multiplié par un facteur de pondération issu de la méthode **ReCiPe 2016 Endpoint H / World**, qui reflète l’importance relative des impacts sur trois catégories de dommages : santé humaine, qualité des écosystèmes et ressources naturelles.

    La pondération \( w_i \) est fixée selon ReCiPe et ne peut pas être modifiée par l’utilisateur.

    Le score pondéré pour chaque indicateur est calculé ainsi :

    $$
    S_i(p) = I_{norm}(p,i) \\times w_i
    $$

    Ces pondérations sont des coefficients scalaires basés sur des modèles d’évaluation d’impacts environnementaux.
    """)

    st.markdown("### 3. Somme des scores pondérés")

    st.markdown("""
    Le score environnemental global d’un produit \( p \) est obtenu par la somme des scores pondérés de ses indicateurs :

    $$
    S_{global}(p) = \\sum_{i=1}^{16} S_i(p) = \\sum_{i=1}^{16} I_{norm}(p,i) \\times w_i
    $$

    Ce score est sans unité et sert uniquement à comparer les impacts relatifs des produits.
    """)

    st.markdown("### 4. Classification en score de A à E")

    st.markdown("""
    Pour faciliter la compréhension, ce score est converti en une note qualitative de **A à E**, basée sur la distribution des scores de 2 497 produits de la base Agribalyse.  
    Cette classification utilise les quintiles de la distribution :

    - **A** : 20 % des produits les moins impactants  
    - **B** : 20 % suivants  
    - **C** : 20 % suivants  
    - **D** : 20 % suivants  
    - **E** : 20 % des plus impactants  

    Cela crée un label similaire au Nutri-Score nutritionnel, mais pour l’impact environnemental.
    """)

    st.markdown("### 5. Traitement des paniers alimentaires")

    st.markdown("""
    Pour un panier contenant plusieurs produits, la méthode se déroule en deux phases :

    1. Calcul des impacts environnementaux pour chaque produit individuellement.  
    2. Agrégation des impacts du panier par addition des valeurs pondérées indicateur par indicateur :

    $$
    S_i(panier) = \\sum_{p \\in panier} S_i(p)
    $$

    La normalisation, pondération et classification s’appliquent ensuite au score total du panier, considéré comme un produit unique virtuel.
    """)

    st.markdown("## 📚 Sources méthodologiques")

    st.markdown("""
    - Base de données **Agribalyse v3.1** (ADEME) : données ACV et impacts moyens des produits  
    - **Base Empreinte** (ADEME) : données de normalisation environnementale nationale  
    - Méthode **ReCiPe 2016 Endpoint H / World** : pour les facteurs de pondération des indicateurs  
    - Modèles et méthodologies ACV validés selon ISO 14040-14044  
    - Inspiré du projet de recherche [Darmon et al., 2021] sur l’évaluation environnementale alimentaire  
    - Les coefficients, pondérations et normalisations sont intégrés dans les fichiers `ponderations.json` et `normalisation.csv` pour adaptations ou scénarios alternatifs.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ========== STRUCTURE ==========
load_css()
create_navbar()
methodo_content()
create_footer()
