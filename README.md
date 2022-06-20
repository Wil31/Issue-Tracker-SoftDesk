[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

# Issue-Tracker

Issue-Tracker est une application permettant de remonter et suivre des 
problèmes techniques (issue tracking system).

Projet consistant à créer une API Restful pour la société SoftDesk.
Cette entreprise veut créer une API afin de permettre aux différents
intervenants d'une équipe de développement, d'échanger sur les problèmes 
techniques qu'ils rencontrent.

La conception de cette API doit utiliser le langage Python et Django Rest
Framework.

L'API doit respecter les contraintes suivantes :

* L'utilisateur doit pouvoir créer un compte et se connecter.
* L'accès global à l'API requiert une authentification.
* Le créateur d'un projet est le seul à pouvoir effacer ou mettre à jour son
  projet, il est donc le seul à pouvoir ajouter des contributeurs.
* Les contributeurs d'un projet n'ont qu'un accès en lecture à celui-ci, ils
  peuvent cependant créer des problèmes et commenter les problèmes.
* Les problèmes et commentaires suivent la même logique que les projets, seul
  les créateurs
  peuvent les mettre à jour ou les effacer.

## Utilisation

### Prérequis

* Un terminal (par exemple Windows PowerShell)
* Python3 version >= 3.10 (vérifier avec `python -V`)

### 1 - Télécharger les fichiers

* Téléchargez depuis le lien:
  [https://github.com/.../main.zip](https://github.com/Wil31/Issue-Tracker-SoftDesk/archive/refs/heads/main.zip)
* Extraire le .zip

### 2 - Configurer l'environnement virtuel

* Ouvrez un terminal
* Naviguez vers le dossier extrait _([...]\Issue-Tracker-SoftDesk)_
* Créez un environnement virtuel avec la commande `python -m venv env`
* Activer l'environnement
  avec `.\env\Scripts\activate` (`source env/bin/activate` sur Linux)
* Installez les packages avec `pip install -r .\requirements.txt`

### 3 - Exécuter le code

* Lancez le serveur depuis le terminal avec la
  commande `py.exe manage.py runserver`
* Entrez l'adresse suivante dans un navigateur : [http:/127.0.0.1:8000/]()

### 4 - Tester l'API

**Veuillez consulter [la documentation de l'API](https://documenter.getpostman.com/view/19642426/Uz5AtKbq)
pour l'utilisation des différents endpoints.**

Créez de nouveaux utilisateurs ou utilisez les identifiants des comptes 
suivants pour essayer les endpoints de l'API.

**Compte standard :**  
Username : `user`  
MdP : `user`

**Compte superuser :**  
Username : `wil`  
MdP : `wil`

## Rapport flake8

Le repository contient un rapport flake8 dans le dossier _flake8_rapport_.
Il est possible de générer un nouveau rapport avec la commande :

```bash
flake8
```

Le fichier ```.flake8``` à la racine contient les paramètres concernant la
génération du rapport.
