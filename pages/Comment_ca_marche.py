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
    st.markdown("## 🔍 Fondements scientifiques")

    st.markdown("""
    L’outil repose sur l’**Analyse du Cycle de Vie (ACV)**, conformément aux normes ISO 14040 et 14044.  
    Les données d’entrée proviennent de la base **Agribalyse v3.1**, développée par l’ADEME, qui fournit pour chaque produit un profil environnemental complet **en analyse moyenne de marché**.

    Chaque fiche produit contient les **quantités unitaires d’impact environnemental** pour 16 indicateurs, exprimées par kilogramme de produit.
    """)

    st.markdown("## 🧮 Étapes du calcul du score")

    st.markdown("""
    ### 1. **Conversion en impacts absolus par portion**
    Pour chaque produit sélectionné, les données ACV sont multipliées par la **masse (en kg) correspondant à la portion renseignée par l’utilisateur.**

    Exemple :  
    Un yaourt de 125 g → tous les impacts sont multipliés par 0,125.

    ### 2. **Normalisation par rapport à l’empreinte annuelle moyenne d’un Français**
    Les 16 indicateurs sont **normalisés** en divisant les valeurs par les valeurs de référence annuelles fournies par l’ADEME (cf. fichier *basefootprint.csv*).

    Formule :  
    \\[
    I_{norm,i} = \\frac{I_i}{N_i}
    \\]  
    où :
    - \\( I_i \\) = impact brut de l’indicateur \\( i \\) pour le produit (exprimé par portion)  
    - \\( N_i \\) = valeur de référence annuelle française pour l’indicateur \\( i \\)

    Résultat : un **vecteur de scores sans unité**, comparable entre indicateurs.

    ### 3. **Pondération selon ReCiPe 2016 Endpoint**
    Chaque indicateur est multiplié par un **poids spécifique** issu de la méthode ReCiPe 2016 Endpoint (version Hiérarchiste, moyenne mondiale, midpoints → endpoints).

    Formule :  
    \\[
    I_{pondéré,i} = I_{norm,i} \\times w_i
    \\]  
    où :
    - \\( w_i \\) = facteur de pondération de l’indicateur \\( i \\)

    Ces coefficients traduisent le **poids relatif** de chaque indicateur dans l’impact global (santé humaine, écosystèmes, ressources).

    ### 4. **Agrégation en score unique**
    La somme pondérée des indicateurs donne un **score environnemental global** pour le produit ou le panier.

    Formule :  
    \\[
    Score = \\sum_{i=1}^{16} I_{pondéré,i}
    \\]

    Le résultat est un **nombre adimensionné** qui permet la comparaison inter-produits et intra-panier.

    ### 5. **Classification sur une échelle A à E**
    Le score est ensuite **classé en quintiles** sur la base de la distribution des scores de 2 497 produits alimentaires de la base Agribalyse.  
    Cette classification suit une logique **statistique de rang**, non normative.

    Répartition :
    - **A** = 20 % des produits les moins impactants
    - **E** = 20 % les plus impactants

    Cela permet une **interprétation simple et comparative**, tout en conservant la rigueur des données sous-jacentes.
    """)

    st.markdown("## 🧺 Fonctionnement pour un panier")

    st.markdown("""
    Lorsqu’un utilisateur compose un panier, les impacts sont **sommés produit par produit**, en suivant les mêmes étapes (portion → normalisation → pondération → agrégation).

    Le score total du panier est ensuite **classé** selon la même grille de répartition A–E.

    Cela permet de :
    - quantifier les conséquences d’un choix alimentaire complet
    - identifier les aliments les plus déterminants
    - comparer plusieurs régimes simulés
    """)

    st.markdown("## 📂 Données utilisées")

    st.markdown("""
    - **Agribalyse v3.1** : profils ACV moyens (ADEME)
    - **Base Empreinte** : valeurs de normalisation annuelles par indicateur
    - **ReCiPe 2016 Endpoint** : pondérations environnementales
    - **Distribution Agribalyse** : pour le classement statistique

    Tous les calculs sont reproductibles, transparents et modifiables si vous souhaitez tester d'autres hypothèses (régionales, pondérations alternatives, etc.).
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ========== STRUCTURE ==========
load_css()
create_navbar()
methodo_content()
create_footer()
