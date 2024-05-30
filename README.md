# Chatbot OpenAI
## Introduction  Ce projet implémente un chatbot utilisant l'API OpenAI.

1. Installez les dépendances :

    `pip install -r requirements.txt`

## Utilisation

Pour utiliser le chatbot, exécutez le script principal dans le répertoire `src`.

Pour effectuer le test `python -m unittest discover -s tests`


## Structure du projet

Le projet est organisé comme suit :

`project/
├── src/
	└── chatbot_chat.py
├── tests/
	└── test_chatbot.py
├── data/
	├── .env
	├── .gitignore
├── requirements.txt
└── README.md`

- `src/` : Contient les scripts principaux pour différentes fonctionnalités du chatbot.
- `tests/` : Contient les tests unitaires pour le projet.
- `data/` : Répertoire pour les fichiers de données (s'il y en a).
- `.env` : Fichier pour les variables d'environnement.
- `.gitignore` : Fichier pour spécifier les fichiers et répertoires à ignorer par git.
- `requirements.txt` : Fichier listant les dépendances Python nécessaires pour le projet.
- `README.md` : Documentation du projet.

## Fonctionnalités

- Afficher des parfums de glace
- Fournir des recettes de cuisine
- Tenir des conversations interactives

## Contributions

Les contributions sont les bienvenues. Veuillez soumettre une pull request pour toute amélioration ou nouvelle fonctionnalité.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
