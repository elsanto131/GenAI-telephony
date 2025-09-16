# SÉCURITÉ - GenAI Telephony

## Protection des données personnelles

### Données sensibles identifiées
- Numéros de téléphone des clients
- Identifiants clients
- Contenu des conversations téléphoniques

### Mesures de protection mises en place

**Masquage des données sensibles :**
```python
import hashlib
import re

def mask_phone_number(text):
    """Remplace les numéros de téléphone par [PHONE]"""
    return re.sub(r'\b\d{2,4}[-.\s]?\d{2,4}[-.\s]?\d{2,4}\b', '[PHONE]', text)

def hash_customer_id(customer_id, salt):
    """Hash des identifiants clients avec salt"""
    return hashlib.sha256((customer_id + salt).encode()).hexdigest()
```

**Génération de données synthétiques :**
- Utilisation de données fictives pour l'analyse
- Aucune donnée client réelle utilisée
- Hash cryptographique des identifiants

## Conformité RGPD

### Principes respectés

**Minimisation des données :**
- Collecte uniquement des données nécessaires
- Anonymisation des transcriptions
- Pseudonymisation des identifiants

**Sécurisation du stockage :**
- Chiffrement des fichiers sensibles
- Séparation des données et des clés
- Accès contrôlé aux données

**Durée de conservation :**
- Données conservées 7 ans maximum
- Suppression automatique après expiration
- Logs de sécurité conservés 1 an

### Code pour la conformité RGPD

```python
class GDPRCompliance:
    def __init__(self, salt_key):
        self.salt = salt_key
        self.retention_days = 2555  # 7 ans
    
    def anonymize_transcript(self, text):
        """Anonymise une transcription"""
        # Masquer numéros
        text = re.sub(r'\b\d{10,}\b', '[PHONE]', text)
        # Masquer emails  
        text = re.sub(r'\S+@\S+', '[EMAIL]', text)
        return text
    
    def pseudonymize_id(self, customer_id):
        """Pseudonymise un ID client"""
        return hashlib.sha256((customer_id + self.salt).encode()).hexdigest()[:12]
```

## Sécurisation des API

### Authentification basique

```python
from fastapi import HTTPException, Depends
import os

API_KEY = os.getenv('API_KEY')

def verify_api_key(api_key: str):
    """Vérifie la clé API"""
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="API key invalide")
    return True

@app.post("/analyze")
def analyze_text(text: str, api_key: str = Depends(verify_api_key)):
    # Traitement sécurisé
    return {"result": "ok"}
```

### Validation des entrées

```python
def validate_input(text):
    """Valide et nettoie les entrées utilisateur"""
    if not text or len(text) > 10000:
        raise ValueError("Texte invalide ou trop long")
    
    # Supprime les caractères dangereux
    cleaned = re.sub(r'[<>"\']', '', text)
    return cleaned.strip()
```

## Gestion des logs

### Logs sécurisés

```python
import logging
from datetime import datetime

def setup_secure_logging():
    """Configure les logs sans données sensibles"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/app.log'),
            logging.StreamHandler()
        ]
    )

def log_api_access(endpoint, status):
    """Log d'accès API sans données sensibles"""
    logging.info(f"API access: {endpoint} - Status: {status}")
```

## Configuration sécurisée

### Variables d'environnement

```python
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration sécurisée
SECRET_KEY = os.getenv('SECRET_KEY', 'default-dev-key')
SALT_PII = os.getenv('SALT_PII', 'default-salt')
API_KEY = os.getenv('API_KEY', 'default-api-key')

# Vérification des variables critiques
if not all([SECRET_KEY, SALT_PII, API_KEY]):
    raise ValueError("Variables d'environnement manquantes")
```

## Chiffrement des données

### Chiffrement simple avec cryptography

```python
from cryptography.fernet import Fernet
import os

class DataEncryption:
    def __init__(self):
        self.key = os.getenv('ENCRYPTION_KEY', Fernet.generate_key())
        self.cipher = Fernet(self.key)
    
    def encrypt_data(self, data):
        """Chiffre des données"""
        return self.cipher.encrypt(data.encode()).decode()
    
    def decrypt_data(self, encrypted_data):
        """Déchiffre des données"""
        return self.cipher.decrypt(encrypted_data.encode()).decode()
```

## Audit et traçabilité

### Logs d'audit simples

```python
import json
from datetime import datetime

def log_data_access(action, resource):
    """Log d'audit sans données sensibles"""
    audit_entry = {
        'timestamp': datetime.utcnow().isoformat(),
        'action': action,
        'resource': resource
    }
    
    with open('logs/audit.log', 'a') as f:
        f.write(json.dumps(audit_entry) + '\n')
```

## Checklist de sécurité

### Vérifications avant déploiement
- [ ] Toutes les données sensibles sont masquées
- [ ] Les variables d'environnement sont configurées
- [ ] Les logs ne contiennent pas de PII
- [ ] L'authentification API est activée
- [ ] Les données sont chiffrées
- [ ] Les accès sont restreints

### Maintenance régulière
- [ ] Vérification des logs (hebdomadaire)
- [ ] Rotation des clés (tous les 3 mois)
- [ ] Mise à jour des dépendances (mensuel)
- [ ] Audit des permissions (mensuel)

## Contact

Pour signaler un problème de sécurité :
- Email : 
- En cas d'urgence : Contacter immédiatement l'équipe technique

---

Version du document : 1.0  
Dernière mise à jour : Décembre 2024