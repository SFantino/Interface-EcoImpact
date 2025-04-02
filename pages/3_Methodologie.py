import streamlit as st

st.set_page_config(page_title="Méthodologie | EcoImpact", layout="wide")

st.title("📊 Méthodologie Scientifique")
st.write("""
### Nos sources de données:
1. Base Carbone® ADEME
2. Données INSEE
3. Études peer-reviewed

### Méthodes de calcul:
- Approche cycle de vie
- Facteurs d'émission standardisés
""")

with st.expander("Voir le détail des calculs"):
    st.write("""
    Formule utilisée:
    ```
    Emission = Activité × Facteur d'émission × Coefficient
    ```
    """)
