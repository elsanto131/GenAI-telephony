"""
Module NLP : Analyse de sentiment pour dialogues téléphoniques
"""

# ----- Import libraries PEP 8 -----
# ----- Standard library -----
from transformers import pipeline # Librairie pour le traitement du langage naturel (NLP)


class SentimentAnalyzer: # Classe pour l'analyse de sentiment, utilise un modèle pré-entraîné

    def __init__(self): # Initialisation du modèle
        
        self.analyzer = pipeline( # .analyzer est un pipeline d'analyse de sentiment
            "sentiment-analysis", # Type de tâche NLP
            model="nlptown/bert-base-multilingual-uncased-sentiment" # Modèle pré-entraîné (BERT multilingue)
        )

    def analyze(self, text: str, max_length: int = 512) -> dict: # Méthode pour analyser le sentiment d'un texte
        """
        Analyse le sentiment d'un texte.
        Args:
            text (str): Texte à analyser
            max_length (int): Longueur maximale du texte
        Returns:
            dict: Résultat du modèle (label et score)
        """
        # Condition pour gérer le texte vide
        if not text: # Si le texte est vide
            return {"label": "NEUTRAL", "score": 0.0} # Retourne "NEUTRAL" avec score 0
        result = self.analyzer(text[:max_length]) # .analyzer applique le modèle au texte tronqué, :max_length limite la taille
        if isinstance(result, list): # Si le résultat est une liste
            result = result[0] # Prend le premier élément de la liste
        return {"label": result["label"], "score": float(result["score"])} # Retourne le label et le score du sentiment
