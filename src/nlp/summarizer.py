"""
Module NLP : Résumé automatique des dialogues téléphoniques
"""

# ----- Import libraries PEP 8 -----
# ----- Standard library -----
from transformers import pipeline # Librairie pour le traitement du langage naturel (NLP)

class DialogueSummarizer: # Classe pour générer un résumé automatique, utilise un modèle extractif pré-entraîné

    def __init__(self):  # __init__() initialise le modèle

        self.summarizer = pipeline( #.summarizer est un pipeline de résumé
            "summarization", # Type de tâche NLP
            model="facebook/bart-large-cnn" # Modèle pré-entraîné (BART large CNN)
        )

    def summarize(self, text: str, min_length: int = 30, max_length: int = 120) -> str: # Méthode pour résumer le texte

        # Condition pour gérer le texte vide ou trop court
        if not text or len(text) < min_length: # Si le texte est vide ou trop court
            return "Texte trop court pour générer un résumé." # Retourne un message d'erreur
        result = self.summarizer(text[:1024], min_length=min_length, max_length=max_length) # .summarizer applique le modèle au texte tronqué à 1024 caractères
        return result[0]["summary_text"] # Retourne le résumé généré
