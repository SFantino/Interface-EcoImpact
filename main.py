import streamlit as st
from home import main as home_page
from methodologie import main as methodologie_page
from ressources import main as ressources_page
from analyse_cycle_vie import main as analyse_cycle_vie_page

# Gestion des routes
page = st.experimental_get_query_params().get("page", ["home"])[0]

if page == "home":
    home_page()
elif page == "methodologie":
    methodologie_page()
elif page == "ressources":
    ressources_page()
elif page == "analyse_cycle_vie":
    analyse_cycle_vie_page()
