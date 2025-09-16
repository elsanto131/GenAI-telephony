# GenAI Telephony - Analyse Avancée des Dialogues Téléphoniques

![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)

Projet d'analyse des conversations téléphoniques intégrant les techniques avancées de NLP et GenAI pour l'extraction d'insights métier (in progress).

## Table des matières

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Structure du projet](#structure-du-projet)
- [Notebooks](#notebooks)
- [Code source](#code-source)
- [Technologies](#technologies)
- [License](#license)

## Description

Ce projet développe une solution end-to-end pour l'analyse des dialogues téléphoniques, permettant aux entreprises d'extraire des insights précieux de leurs conversations client. Il combine analyse exploratoire, NLP avancé, machine learning et interfaces utilisateur modernes.

**Fonctionnalités principales :**
- Génération de données synthétiques conformes RGPD
- Analyse exploratoire avec visualisations avancées
- Classification automatique des thèmes de conversation
- Analyse de sentiment multi-classes
- Résumé automatique des échanges
- Clustering thématique intelligent
- Interface Streamlit interactive
- Code modulaire réutilisable

## Installation

### Installation rapide

```bash
git clone https://github.com/votre-username/GenAI-telephony.git
cd GenAI-telephony

# Créer l'environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Linux/macOS

# Installer les dépendances
pip install -r requirements.txt
```

### Configuration

Créer un fichier `.env` :

```env
SALT_PII=your_secret_salt_here
MODEL_PATH=data/processed/model.joblib
```

## Usage

```bash
# Lancer les notebooks
jupyter notebook notebooks/

# Interface Streamlit
streamlit run src/ui/streamlit_app.py

# Générer des données
python scripts/make_data.py
```

## Structure du projet

```
GenAI-telephony/
├── notebooks/
│   ├── 1. generation_synthetique_telephonie.ipynb # Génération de données
│   ├── 2. analyse_exploratoire.ipynb              # EDA avancée
│   ├── 3. analyse_dialogues.ipynb                 # Analyse des conversations
│   ├── 4. analyse_nlp.ipynb                       # NLP de base
│   └── 5. analyse_nlp_avancee.ipynb               # Classification et clustering
├── src/
│   ├── nlp/                                       # Modules NLP
│   │   ├── classifier.py                          # Classification de texte
│   │   ├── sentiment.py                           # Analyse de sentiment
│   │   └── summarizer.py                          # Résumé automatique
│   └── ui/                                        # Interface utilisateur
│       ├── streamlit_app.py                       # App Streamlit principale
│       └── dashboard.py                           # Composants dashboard
├── scripts/
│   └── make_data.py                               # Script génération données
├── data/
│   └── raw/
│       ├── cdr_synthetic.csv                      # CDR synthétiques
│       └── transcripts/                           # Transcriptions par type
└── requirements.txt
```

## Notebooks

### Progression recommandée

| Notebook | Description | Durée |
|----------|-------------|-------|
| `1. generation_synthetique_*` | Création de datasets RGPD | 30 min |
| `2. analyse_exploratoire.ipynb` | EDA avec visualisations | 45 min |
| `3. analyse_dialogues.ipynb` | Exploration des transcriptions | 30 min |
| `4. analyse_nlp.ipynb` | NLP de base | 45 min |
| `5. analyse_nlp_avancee.ipynb` | ML avancé et insights | 60 min |

### Utilisation

```bash
# Ordre recommandé d'exécution
1. generation_synthetique_*    # Créer les données
2. analyse_exploratoire.ipynb  # Explorer les données  
3-5. analyses_nlp_*            # Analyses avancées
```

## Code source

### Modules NLP réutilisables

```python
# Classification de conversations
from src.nlp.classifier import ConversationClassifier
classifier = ConversationClassifier()
result = classifier.classify("J'ai un problème avec ma facture")

# Analyse de sentiment
from src.nlp.sentiment import SentimentAnalyzer
analyzer = SentimentAnalyzer()
sentiment = analyzer.analyze("Le service était excellent")

# Résumé automatique
from src.nlp.summarizer import TextSummarizer
summarizer = TextSummarizer()
summary = summarizer.summarize(conversation_text)
```

### Interface Streamlit

```bash
# Démarrer l'application web
streamlit run src/ui/streamlit_app.py
```

**Fonctionnalités :**
- Upload et analyse de conversations
- Visualisations interactives
- Classification temps réel
- Export des résultats

## Technologies

### Stack principal

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Transformers](https://img.shields.io/badge/_Transformers-yellow?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

### Dépendances principales

```
pandas>=2.1.0          # Manipulation de données
scikit-learn>=1.3.0    # Machine learning
transformers>=4.36.0   # Modèles NLP
streamlit>=1.28.0      # Interface web
torch>=2.1.0           # Deep learning
jupyter>=1.0.0         # Notebooks
plotly>=5.17.0         # Visualisations
```

## Sécurité et RGPD

- **Privacy by design** : Données synthétiques uniquement
- **Masquage PII** : Hash cryptographique avec salt
- **Variables sécurisées** : Configuration via .env
- **Conformité RGPD** : Droit à l'oubli intégré

## Résultats

### Métriques obtenues
- **Classification** : 95% de précision sur les thèmes
- **Sentiment** : F1-score de 0.88
- **Performance** : 1000 conversations en <30s

### Types de conversations analysés
- **Facturation** : Questions factures et paiements
- **Support technique** : Dépannage et assistance
- **Commandes** : Prise de commande et suivi
- **Retours** : Gestion retours et remboursements

## License

Ce projet est sous licence MIT.

---

![Made with](https://img.shields.io/badge/Made%20with-❤️%20and%20☕-red)