import streamlit as st
import requests

st.title("Dashboard NLP API")

st.markdown("""
Ce dashboard permet de tester l'API NLP (sentiment, classification, résumé) en envoyant un texte et en affichant le résultat.
""")

# Saisie du texte à analyser
text = st.text_area("Entrez un texte à analyser :", "Votre service est excellent")

# Adresse de l'API (à adapter si besoin)
API_URL = "http://127.0.0.1:8000"

if st.button("Analyser le sentiment"):
    response = requests.post(f"{API_URL}/sentiment/", json={"text": text})
    if response.status_code == 200:
        st.success(f"Résultat : {response.json()}")
    else:
        st.error("Erreur lors de l'appel à l'API")

if st.button("Classer le texte"):
    response = requests.post(f"{API_URL}/classify/", json={"text": text})
    if response.status_code == 200:
        st.success(f"Résultat : {response.json()}")
    else:
        st.error("Erreur lors de l'appel à l'API")

if st.button("Résumer le texte"):
    response = requests.post(f"{API_URL}/summarize/", json={"text": text})
    if response.status_code == 200:
        st.success(f"Résumé : {response.json()}")
    else:
        st.error("Erreur lors de l'appel à l'API")

st.markdown("""
---
*Ce dashboard est un exemple pédagogique pour visualiser les résultats NLP de l'API.*
""")
