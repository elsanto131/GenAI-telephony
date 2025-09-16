"""
Module NLP : Classification thématique des dialogues téléphoniques
"""

# ----- Import libraries PEP 8 -----
# ----- Standard library -----
from transformers import pipeline # Librairie pour le traitement du langage naturel (NLP)


class DialogueClassifier: # Classe pour classifier le type de dialogue, utilise le zero-shot classification

    def __init__(self):  # __init__() initialise le modèle

        self.classifier = pipeline( # .classifier est un pipeline de classification
            "zero-shot-classification", # Type de tâche NLP
            model="MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli" # Modèle pré-entraîné (DeBERTa v3)
        )

        self.labels = [ #.labels prédéfinis pour la classification
            "facturation",
            "support technique",
            "commande",
            "réclamation",
            "retour",
            "autre"
        ]

    def classify(self, text: str, max_length: int = 512) -> dict: # Classe pour classifier le texte selon des thèmes prédéfinis
        
        # Condition pour gérer le texte vide
        if not text: # Si le texte est vide
            return {"label": "autre", "score": 0.0} # Retourne "autre" avec score 0
        result = self.classifier(text[:max_length], self.labels) # .classifier applique le modèle au texte tronqué, :max_length limite la taille, .labels sont les thèmes
        return {"label": result["labels"][0], "score": float(result["scores"][0])}  # Retourne le label et le score du thème le plus probable
