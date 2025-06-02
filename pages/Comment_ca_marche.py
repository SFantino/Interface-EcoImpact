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
    Cette interface évalue l'impact environnemental d'un panier alimentaire sur la base de la méthode d’**Analyse de Cycle de Vie (ACV)**.  
    L’outil s’appuie sur la base **Agribalyse 3.1**, qui fournit les résultats d’impact moyen de plus de 2000 produits.

    Le calcul suit les étapes suivantes :
    """)

    st.markdown("### 1. Agrégation des données par portion")

    st.markdown("""
    Les données Agribalyse sont exprimées pour 1 kg de produit.  
    On les ramène à la portion alimentaire renseignée en multipliant chaque indicateur par la masse en kg.

    Exemple : pour une portion de 125 g de yaourt, tous les impacts sont multipliés par 0,125.
    """)

    st.markdown("### 2. Normalisation par rapport à l’empreinte moyenne annuelle d’un Français")

    st.markdown("""
    Chaque indicateur est normalisé selon la **méthode ReCiPe Endpoint (H)** en le divisant par la **valeur annuelle moyenne française** extraite de la base de données Base Empreinte.

    La formule appliquée est :

    $$
    \\text{Impact normalisé} = \\frac{\\text{Impact absolu (portion)}}{\\text{Valeur de normalisation (France, 1 an)}}
    $$

    Cela permet de comparer les indicateurs entre eux malgré des unités différentes (kg CO₂, kg P eq, MJ, etc.).
    """)

    st.markdown("### 3. Pondération des indicateurs")

    st.markdown("""
    Une pondération est appliquée à chaque indicateur normalisé selon la **méthode ReCiPe Endpoint (H, World, 2016)**.  
    Ces poids traduisent l’importance relative des impacts sur trois catégories de dommage : santé humaine, qualité des écosystèmes, ressources.

    $$
    \\text{Score pondéré} = \\text{Impact normalisé} \\times \\text{Facteur de pondération}
    $$

    Les pondérations sont fixées et issues directement de la méthode ReCiPe. Elles ne sont pas modifiables par l’utilisateur.
    """)

    st.markdown("### 4. Agrégation des scores")

    st.markdown("""
    Les 16 scores pondérés sont **sommés** pour obtenir un score global pour chaque produit (ou chaque panier).

    $$
    \\text{Score final} = \\sum_{i=1}^{16} \\text{Score pondéré}_{i}
    $$

    Ce score n’a pas d’unité mais permet une comparaison relative entre produits.
    """)

    st.markdown("### 5. Attribution d’un score A à E")

    st.markdown("""
    Pour donner une lisibilité au score, une classification est effectuée **par quintiles**, à partir de la distribution des scores de 2497 produits Agribalyse.

    Répartition :
    - A = 20 % des produits les moins impactants
    - E = 20 % les plus impactants

    Cela permet une lecture intuitive, comparable à un Nutri-Score environnemental.
    """)

    st.markdown("### 6. Fonctionnement pour un panier alimentaire")

    st.markdown("""
    Lorsqu’un panier est composé de plusieurs produits, la méthode est strictement la même.  
    Les impacts environnementaux sont d’abord calculés **produit par produit**, puis **additionnés** pour chaque indicateur.

    La normalisation, pondération et classification s’effectuent ensuite sur le total du panier, comme s’il s’agissait d’un unique produit virtuel.
    """)

    st.markdown("## 📚 Sources méthodologiques")

    st.markdown("""
    - Base de données **Agribalyse v3.1** (ADEME)  
    - **Base Empreinte** (ADEME) : valeurs de normalisation annuelles pour la France  
    - Méthode **ReCiPe 2016 Endpoint H / World** : facteurs de pondération  
    - Méthodologie inspirée du projet de recherche [Darmon et al., 2021] et du cadre de l’ACV alimentaire

    Les coefficients, formules et pondérations sont intégrés en dur dans le calcul et peuvent être modifiés dans les fichiers `ponderations.json` et `normalisation.csv` pour tests ou scénarios alternatifs.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ========== STRUCTURE ==========
load_css()
create_navbar()
methodo_content()
create_footer()
