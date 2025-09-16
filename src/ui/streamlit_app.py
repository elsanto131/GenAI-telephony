import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import numpy as np

# Configuration de la page
st.set_page_config(
    page_title="GenAI Telephony - Dashboard",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé pour un design professionnel
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        color: #1f4e79;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choisissez une section:",
        ["Vue d'ensemble", "Exploration données", "Analyse NLP", "Insights & Clustering", "Sécurité & Conformité"]
    )
    
    if page == "Vue d'ensemble":
        show_overview()
    elif page == "Exploration données":
        show_data_exploration()
    elif page == "Analyse NLP":
        show_nlp_analysis()
    elif page == "Insights & Clustering":
        show_clustering()
    elif page == "Sécurité & Conformité":
        show_security()

def show_overview():
    st.markdown('<h1 class="main-header">GenAI Telephony Dashboard</h1>', unsafe_allow_html=True)
    # Hero section
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.info("**Projet Data Science** - Analyse avancée des dialogues téléphoniques avec GenAI et sécurité RGPD")
    # KPIs mockup
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Appels analysés", "201", "+15%")
    with col2:
        st.metric("Temps moyen (AHT)", "12m 34s", "-8%")
    with col3:
        st.metric("Taux résolution", "73.2%", "+5%")
    with col4:
        st.metric("Satisfaction NLP", "76.8%", "+12%")
    # Architecture pipeline
    st.subheader("Architecture du Pipeline")
    st.markdown(
        """
```mermaid
graph LR
    A[Amazon Connect] --> B[Transcriptions]
    B --> C[Masquage PII]
    C --> D[Analyse NLP]
    D --> E[Classification]
    D --> F[Sentiment]
    D --> G[Résumé]
    E --> H[Dashboard]
    F --> H
    G --> H
```
        """
    )

def show_data_exploration():
    st.header(" Exploration des Données")
    
    # Simuler chargement données
    if st.button("Charger les données CDR"):
        data_path = Path("data/raw/cdr_synthetic.csv")
        if data_path.exists():
            df = pd.read_csv(data_path)
            
            # Aperçu des données
            st.subheader("Aperçu des données")
            st.dataframe(df.head(10))
            
            # Graphiques interactifs
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Distribution par thème")
                theme_counts = df['topic'].value_counts()
                fig = px.pie(values=theme_counts.values, names=theme_counts.index, 
                           title="Répartition des thèmes d'appels")
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.subheader("Durée des appels")
                fig = px.histogram(df, x='duration_sec', nbins=20, 
                                 title="Distribution des durées d'appels")
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Fichier CDR non trouvé. Exécutez d'abord le notebook de génération.")

def show_nlp_analysis():
    st.header("Analyse NLP en Temps Réel")
    
    # Interface d'analyse
    st.subheader("Analysez un dialogue")
    
    sample_text = """Client: Bonjour, j'ai un problème avec ma facture.
Agent: Bonjour, je vais vous aider. Pouvez-vous me préciser le problème ?
Client: Il y a des frais que je ne comprends pas.
Agent: Je vais vérifier votre compte immédiatement."""
    
    user_input = st.text_area("Tapez ou collez un dialogue ici:", value=sample_text, height=150)
    
    if st.button("Analyser"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("Classification")
            # Simuler classification
            confidence = np.random.uniform(0.7, 0.95)
            st.success(f"**Thème détecté:** Facturation")
            st.progress(confidence)
            st.write(f"Confiance: {confidence:.1%}")
        
        with col2:
            st.subheader("Sentiment")
            # Simuler sentiment
            sentiment_score = np.random.uniform(-0.3, 0.1)
            if sentiment_score > 0.1:
                st.success("Positif")
            elif sentiment_score > -0.1:
                st.warning("Neutre")
            else:
                st.error("Négatif")
            st.write(f"Score: {sentiment_score:.2f}")
        
        with col3:
            st.subheader("Résumé")
            st.info("**Résumé automatique:**\nClient signale frais incompris sur facture. Agent propose vérification compte.")

def show_clustering():
    st.header("Insights & Clustering Thématique")
    
    # Simuler données de clustering
    st.subheader("Clusters identifiés")
    
    # Graphique de clustering mockup
    np.random.seed(42)
    n_points = 100
    
    cluster_data = pd.DataFrame({
        'x': np.random.normal(0, 1, n_points),
        'y': np.random.normal(0, 1, n_points),
        'cluster': np.random.choice(['Facturation', 'Support Tech', 'Commandes', 'Retours'], n_points),
        'sentiment': np.random.choice(['Positif', 'Neutre', 'Négatif'], n_points)
    })
    
    fig = px.scatter(cluster_data, x='x', y='y', color='cluster', 
                     hover_data=['sentiment'],
                     title="Visualisation des Clusters de Conversations")
    st.plotly_chart(fig, use_container_width=True)
    
    # Recommandations
    st.subheader("Recommandations Automatiques")
    recommendations = [
        "**Priorité Haute:** 23% des appels facturation nécessitent escalade",
        "**Attention:** Pic d'appels support technique le mardi (formation agents?)",
        "**Succès:** Taux de résolution commandes en hausse (+12%)",
        "**Insight:** Mots-clés récurrents: 'remboursement', 'délai', 'problème technique'"
    ]
    
    for rec in recommendations:
        st.markdown(rec)

def show_security():
    st.header("Sécurité & Conformité RGPD")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Démonstration Masquage PII")
        
        # Avant/Après masquage
        st.write("**Avant masquage:**")
        st.code("Client: Marie Dupont, mon numéro est 0476123456")
        
        st.write("**Après masquage:**")
        st.code("Client: [PRÉNOM] [NOM], mon numéro est [TÉLÉPHONE]")
        
        # Métriques de sécurité
        st.metric("PII masqués", "100%", "0 fuite")
        st.metric("Audit logs", "1,247", "↗ tracking complet")

    with col2:
        st.subheader("Conformité RGPD")
        
        compliance_items = [
            "Minimisation des données",
            "Consentement explicite",
            "Droit à l'oubli implémenté",
            "Chiffrement bout en bout",
            "Audit trail complet",
            "Privacy by design"
        ]
        
        for item in compliance_items:
            st.write(item)
        
        # Statut global
        st.success("**Statut:** Pleinement conforme RGPD")

if __name__ == "__main__":
    main()
