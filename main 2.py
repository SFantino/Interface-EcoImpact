import streamlit as st

# Configuration initiale
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Accueil'

# CSS complet (identique à votre version)
st.markdown("""
    <style>
        .stApp {
            background: #F3F3F1 url('https://images.unsplash.com/photo-1514995669114-6081e934b693?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat left top / 65% auto;
            min-height: 100vh;
        }
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
            cursor: pointer;
        }
        .navbar a:hover {
            color: #4CAF50;
        }
        .active-page {
            color: #4CAF50 !important;
            font-weight: bolder !important;
        }
        .content-behind {
            position: relative;
            z-index: 0;
            margin-top: 70px;
        }
        .calculator-banner {
            background-color: white;
            padding: 25px;
            border-radius: 0;
            width: 100%;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
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
        /* Masquer les éléments par défaut de Streamlit */
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Fonction de navigation
def switch_page(page_name):
    st.session_state.current_page = page_name

# Barre de navigation personnalisée
st.markdown(f"""
    <div class="navbar">
        <a class="{'active-page' if st.session_state.current_page == 'Accueil' else ''}" 
           onclick="window.streamlitSessionState.set('current_page', 'Accueil')">Accueil</a>
        <a class="{'active-page' if st.session_state.current_page == 'Calculateur' else ''}" 
           onclick="window.streamlitSessionState.set('current_page', 'Calculateur')">Calculateur</a>
        <a class="{'active-page' if st.session_state.current_page == 'Ressources' else ''}" 
           onclick="window.streamlitSessionState.set('current_page', 'Ressources')">Ressources</a>
        <a class="{'active-page' if st.session_state.current_page == 'Methodologie' else ''}" 
           onclick="window.streamlitSessionState.set('current_page', 'Methodologie')">Méthodologie</a>
    </div>
""", unsafe_allow_html=True)

# Contenu des pages
st.markdown('<div class="content-behind">', unsafe_allow_html=True)

if st.session_state.current_page == 'Accueil':
    # Page Accueil
    col1, col2 = st.columns([3, 1])
    with col2:
        st.image("Logo.jpg", width=300)
    
    st.markdown("""
        <div style="text-align: right; margin-right: 20px;">
            <h1>Bienvenue sur EcoImpact</h1>
            <p>Découvrez votre impact environnemental avec notre calculateur.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Bouton pour le calculateur
    st.markdown("""
        <div style="margin-top: 50px; padding-bottom: 100px;">
            <div class="calculator-banner">
                <div style="font-size: 24px; font-weight: bold; margin-bottom: 15px;">Tester le calculateur</div>
                <button onclick="window.streamlitSessionState.set('current_page', 'Calculateur')" 
                        style="background-color: #23A95C; color: white; border: none; padding: 12px 30px; font-size: 18px; border-radius: 50px; cursor: pointer;">
                    Start
                </button>
            </div>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.current_page == 'Calculateur':
    # Page Calculateur
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
            # Exemple de calcul
            facteurs = {
                "Transport": 0.2,
                "Énergie": 0.5,
                "Alimentation": 2.0,
                "Logement": 1.5
            }
            impact = quantite * facteurs[type_activite]
            st.success(f"Impact estimé: {impact:.2f} kg CO2")

# Footer
st.markdown("""
    <div class="footer-banner">
        <a onclick="window.streamlitSessionState.set('current_page', 'A_propos')">À propos</a>
        <img src="unilasalle_beauvais_logo.jpg" alt="Logo UniLaSalle" style="height: 40px; margin-left: auto;">
    </div>
""", unsafe_allow_html=True)
