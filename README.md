# 🧠 Analyse de Sentiment des Avis Clients (NLP)

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-yellow.svg)
![NLTK](https://img.shields.io/badge/NLTK-NLP-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red.svg)

## 📌 À propos du projet
La satisfaction client est la clé de voûte de toute entreprise. Ce projet de Data Science s'attaque au problème du traitement massif des retours clients (E-commerce). Au lieu de lire manuellement des milliers d'avis pour comprendre si un produit plaît, nous utilisons l'**Intelligence Artificielle (NLP - Traitement du Langage Naturel)** pour automatiser ce processus.

Le projet allie des techniques classiques de nettoyage de texte et des modèles de Deep Learning à l'état de l'art pour extraire les sentiments (Positif, Neutre, Négatif) et identifier les sujets d'insatisfaction majeurs.

## 🚀 Fonctionnalités
- **Génération de données** : Script Python simulant 700 véritables avis clients en français (Positifs, Neutres, Négatifs).
- **Nettoyage (Text Preprocessing)** : Utilisation de NLTK pour la suppression de la ponctuation, la mise en minuscules, le filtrage des "Stopwords" et la Tokenization.
- **Analyse des Sujets (WordClouds)** : Création de nuages de mots pour visualiser instantanément les "Pain Points" (livraison, casse, etc.).
- **Deep Learning (Hugging Face)** : Utilisation du modèle pré-entraîné `nlptown/bert-base-multilingual-uncased-sentiment` pour classer automatiquement les avis sans aucun entraînement manuel (Zero-Shot Inference).
- **Interface Web (Dashboard)** : Application Streamlit permettant à n'importe quel utilisateur de tester le modèle en direct avec ses propres phrases.

## 📂 Structure du Projet

```text
sentiment_analysis/
│
├── app/
│   └── app.py                  # L'application Web Streamlit de test en direct
│
├── data/
│   └── avis_clients.csv        # Le dataset de 700 avis générés en français
│
├── notebooks/
│   ├── 01_Nettoyage_Texte.ipynb # Notebook : NLP Classique et Nuages de mots
│   └── 02_Sentiment_Classification.ipynb # Notebook : Inférénce avec Hugging Face BERT
│
├── generate_reviews.py         # Script de génération du jeu de données
├── requirements.txt            # Dépendances du projet (PyTorch, Transformers...)
└── README.md                   # Ce fichier
```

## 💻 Installation et Utilisation en Local

### 1. Cloner le dépôt
```bash
git clone https://github.com/jovyberny-gif/Analyse-de-sentiment-des-avis-clients.git
cd Analyse-de-sentiment-des-avis-clients
```

### 2. Créer l'environnement virtuel (Recommandé)
```bash
python -m venv venv
# Sur Windows :
venv\Scripts\activate
# Sur Mac/Linux :
source venv/bin/activate
```

### 3. Installer les dépendances
*(Attention, l'installation de PyTorch et des modèles Hugging Face peut nécessiter un peu d'espace disque).*
```bash
pip install -r requirements.txt
```

### 4. Lancer l'Application Web
Naviguez dans le dossier `app/` et lancez l'application Streamlit :
```bash
cd app
python -m streamlit run app.py
```
L'application s'ouvrira automatiquement dans votre navigateur (généralement à l'adresse `http://localhost:8501`). Lors de la toute première exécution, le modèle BERT (~600 Mo) sera téléchargé et mis en cache.
