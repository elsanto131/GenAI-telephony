"""
Ce script sert à générer automatiquement les données synthétiques nécessaires au projet.

- Il crée un fichier CSV simulant les appels téléphoniques (CDR), avec des colonnes comme : identifiant d’appel, agent, durée, sujet, résolution, etc.
- Il génère des fichiers texte contenant des dialogues fictifs (transcriptions) pour chaque thème métier (facturation, support, commandes…).
- Il applique un masquage des données personnelles (PII) pour garantir la confidentialité.
- Il sauvegarde ces fichiers dans le dossier data/raw/ pour qu’ils soient utilisés dans l’analyse, l’entraînement du modèle et le système RAG.

Ce script est la première étape du pipeline : il crée l’environnement de données sécurisé et contrôlé sur lequel tout le projet va s’appuyer.
"""

# ----- Import libraries PEP 8 -----
# ----- Standard library -----
import os # Librairie pour les opérations système et gestion des chemins de fichiers (Créer des dossiers, manipule des fichiers, gére des chemin sur l'ordinateur, etc.)
import pandas as pd # Librairie qui sert à manipuler et analyser les métadonnées (tableau de donnéez, CSV, Excel, SQL, etc.)
import numpy as np # Librairie pour les calculs numériques et la génération de données aléatoires (mathématiques, statistiques, etc.) On l’utilise ici pour générer des nombres aléatoires (par exemple, pour simuler la durée des appels, choisir un agent ou un sujet au hasard)
import hashlib # Librairie pour le hachage et le masquage des données (sert à transformer une information comme un numéro de téléphone) en une suite de caractères incompréhensible (appelée ‘hash’))
from datetime import datetime, timedelta # Librairie pour manipuler les dates et heures (datetime pour la date et l'heure actuelles, timedelta pour faire des calculs avec les dates, comme ajouter ou soustraire des jours, heures, etc.)
# ----- Third party libraries -----
from dotenv import load_dotenv # Librairie qui sert à lire un fichier spécial (appelé .env) où on peut ranger des secrets ou des paramètres (comme un mot de passe, un salt, une clé API). load_dotenv() charge ces variables d'environnement pour qu'on puisse les utiliser dans le script.

# 1. Chargement du salt PII depuis .env
load_dotenv() # load_dotenv() charge les variables d'environnement depuis un fichier .env dans le répertoire courant.
salt_pii = os.getenv("SALT_PII", "changeme") # Récupère la variable d'environnement : SALT en cryptographie est une chaîne de caractères aléatoire ajoutée aux données avant le hachage pour renforcer la sécurité. PII (Personally Identifiable Information) désigne les informations permettant d'identifier une personne (nom, adresse, numéro de téléphone, etc.). Ici, on utilise un salt pour masquer les données personnelles dans les fichiers générés. changeme est une valeur par défaut à remplacer.

# 2. Dossiers de sortie
raw_directory = "data/raw" # variable qui va contenir le chemin du dossier où on va enregistrer les fichiers de données brutes (raw data)
transcripts_directory = os.path.join(raw_directory, "transcripts") # os.path.join() combine les parties de chemin de fichiers de manière sûre et compatible avec le système d'exploitation. Ici, on crée le chemin complet vers le dossier des transcriptions en combinant le dossier raw avec "transcripts".
os.makedirs(raw_directory, exist_ok=True) # os.makedirs() crée le dossier raw s'il n'existe pas déjà. exist_ok=True évite une erreur si le dossier existe déjà.
os.makedirs(transcripts_directory, exist_ok=True) # os.makedirs() crée le dossier transcripts s'il n'existe pas déjà. exist_ok=True évite une erreur si le dossier existe déjà.

# 3. Paramètres de génération
numbers_of_calls = 200 # Nombre d'appels à générer dans le CSV (on choisit 200 pour avoir un jeu de données réaliste)
numbers_of_transcripts = 18 # Nombre de fichiers de dialogues à générer (pour couvrir tous les thèmes)
agents = ["A", "B", "C", "D", "E"] # Liste des identifiants d'agents (5 agents fictifs pour simuler la réalité)
topics = ["billing", "tech_support", "orders", "returns", "other"] # Liste des thèmes d'appels (facturation, support, commandes, retours, autres)

def mask_pii(caller_number: str, salt: str = salt_pii) -> str: # Fonction qui prend en entrée un numéro de téléphone fictif (caller_number) et un salt (chaîne aléatoire pour renforcer la sécurité). Elle retourne le hash SHA-256 du numéro combiné avec le salt, ce qui masque le numéro original.
    """Hash le numéro fictif avec un salt pour masquer la PII."""
    return hashlib.sha256((salt + caller_number).encode()).hexdigest() #On utilise la boîte à outils hashlib pour : Prendre le sel et le numéro, les coller ensemble, Les transformer en une suite de caractères incompréhensible (le hash), Retourner ce hash comme résultat

# 4. Génération des appels (CDR) dans un CSV (CDR = Call Detail Record (Enregistrement de détail d'Appel))
np.random.seed(42) # Fixation de la graine aléatoire pour que les résultats soient reproductibles (toujours les mêmes données générées)
start_date = datetime.now() - timedelta(days=30) # On choisit une date de départ : il y a 30 jours
cdr_rows = [] # Préparation d'une liste vide pour stocker chaque appel généré

for i in range(numbers_of_calls): # boucle qui répète l'opération 200 fois (numbers_of_calls), pour créer chaque appel
    call_id = f"CALL_{i+1:04d}" # Création d'un identifiant unique pour chaque appel, sous la forme CALL_0001, CALL_0002, etc.
    caller_number = f"04{np.random.randint(2000000,3999999)}" # On génère un numéro de téléphone fictif de l'appelant, qui commence par 04 et se termine par 7 chiffres aléatoires
    caller_id = mask_pii(caller_number) # Variable qui va contenir le numéro masqué (hashé) de l'appelant, en utilisant la fonction mask_pii définie plus haut
    agent_id = np.random.choice(agents) # Variable qui va contenir l'identifiant d'un agent choisi au hasard parmi la liste agents (.np.random.choice())
    start_timestamp = start_date + timedelta(minutes=np.random.randint(0, 43200))  # Variable qui va contenir une date et heure de début d'appel, répartie sur les 30 derniers jours (43200 minutes = 30 jours) : np.random.randint(0, 43200) tire au hasard un nombre de minutes entre 0 et 43200 (soit 30 jours × 24h × 60min). timedelta(minutes=...) ajoute ce nombre de minutes à la date de départ pour obtenir une date et heure répartie sur le dernier mois.
    call_duration_seconds = np.random.randint(30, 1800) # Variable qui va contenir une durée d'appel aléatoire entre 30 secondes et 1800 secondes (soit 30 minutes max)
    topic = np.random.choice(topics) # Variable qui va contenir un sujet d'appel choisi au hasard parmi la liste topics

    # Résolution de l'appel corrélée faiblement à la durée et au topic
    resolved = int( # Décide si l'appel est résolu (1) ou non (0), en fonction de la durée, du sujet, et d'un peu de hasard
        (call_duration_seconds < 900 and topic != "tech_support") or np.random.rand() > 0.3 # Si l'appel dure moins de 15 min (900 sec) et que le sujet n'est pas "tech_support ", il y a des chances qu'il soit résolu. Sinon, c'est un peu aléatoire (70% de chances de ne pas être résolu -> np.random.rand() > 0.3)
    )

    cdr_rows.append({ # .append() ajoute l'appel généré à la liste cdr_rows sous forme de dictionnaire avec les clés et valeurs correspondantes
        "call_id": call_id, # Identifiant unique de l'appel
        "caller_id": caller_id, # Numéro masqué de l'appelant
        "agent_id": agent_id, # Identifiant de l'agent
        "start_ts": start_timestamp.isoformat(), # Date et heure de début de l'appel
        "duration_sec": call_duration_seconds, # Durée de l'appel en secondes
        "topic": topic, # Sujet de l'appel
        "resolved": resolved # Indique si l'appel a été résolu (1) ou non (0)
    })

cdr_df = pd.DataFrame(cdr_rows) # Variable qui va contenir un tableau de données (DataFrame) créé à partir de la liste cdr_rows. Chaque dictionnaire dans cdr_rows devient une ligne dans le tableau, avec les clés comme colonnes.
cdr_df.to_csv(os.path.join(raw_directory, "cdr_synthetic.csv"), index=False) # Export et enregistrement(.to_csv()) du tableau cdr_df dans un fichier CSV nommé cdr_synthetic.csv dans le dossier raw_directory. index=False signifie qu'on ne veut pas inclure l'index des lignes dans le fichier CSV.
print(f"Fichier CDR généré: {os.path.join(raw_directory, 'cdr_synthetic.csv')}") # Affiche un message pour indiquer où le fichier CSV a été enregistré

# 5. Génération des transcripts synthétiques : Les dialogues sont créés à partir de templates simples pour chaque sujet
dialogue_templates = { # Dictionnaire qui contient des templates de dialogues pour chaque sujet. Chaque sujet (clé) a une liste de lignes de dialogue (valeur) entre un client et un agent.
    "billing": [ # ---> Clé du dictionnaire pour le sujet "billing" (facturation)
        "Client: Bonjour, j'ai une question sur ma facture.", # ---> élément de la liste de dialogues
        "Agent: Bien sûr, pouvez-vous préciser votre demande ?",
        "Client: Il y a un montant que je ne comprends pas.",
        "Agent: Je vérifie cela pour vous."
    ],
    "tech_support": [
        "Client: Mon internet ne fonctionne plus.",
        "Agent: Avez-vous essayé de redémarrer votre box ?",
        "Client: Oui, mais ça ne marche toujours pas.",
        "Agent: Je vais lancer un diagnostic."
    ],
    "orders": [
        "Client: Je souhaite suivre ma commande.",
        "Agent: Pouvez-vous me donner votre numéro de commande ?",
        "Client: C'est le 12345.",
        "Agent: Elle est en cours de livraison."
    ],
    "returns": [
        "Client: Je veux retourner un produit.",
        "Agent: Quelle est la raison du retour ?",
        "Client: Il ne correspond pas à ma commande.",
        "Agent: Je lance la procédure de retour."
    ],
    "other": [
        "Client: J'ai une question générale.",
        "Agent: Je vous écoute.",
        "Client: Quels sont vos horaires d'ouverture ?",
        "Agent: Nous sommes ouverts de 8h à 18h."
    ]
}

# 6. Génération des fichiers de dialogues

for i in range(numbers_of_transcripts): # boucle qui va générer 18 fichiers de dialogues (numbers_of_transcripts)
    topic = np.random.choice(topics) # np.random.choice() choisi aléatoirement un sujet parmi la liste topics
    dialogue = dialogue_templates[topic] # récupère la liste de dialogues correspondant au sujet choisi
    
    # Ajout d'une variation simple
    dialogue = [line.replace("Client", f"Client_{i+1}") for line in dialogue] # line.replace() remplace "Client" par "Client_1", "Client_2", etc. pour chaque ligne du dialogue, afin d'ajouter une variation simple et rendre chaque fichier unique.
    transcript_path = os.path.join(transcripts_directory, f"{topic}_{i+1:02d}.txt") # .path.join() crée le chemin complet vers le fichier de transcription en combinant le dossier transcripts avec un nom de fichier basé sur le sujet et un numéro séquentiel (par exemple, billing_01.txt, tech_support_02.txt, etc.)
    
    with open(transcript_path, "w", encoding="utf-8") as f: # open() ouvre le fichier en mode écriture ("w") avec l'encodage UTF-8 pour supporter les caractères spéciaux. as f crée un objet fichier (f) pour écrire dedans.
        f.write("\n".join(dialogue)) # .write() écrit le dialogue dans le fichier, en joignant les lignes avec des sauts de ligne ("\n".join(dialogue))
    print(f"Transcript généré: {transcript_path}") # Affiche un message pour indiquer où le fichier de transcription a été enregistré

print("Données synthétiques générées avec succès.") # Message final pour indiquer que tout s'est bien passé