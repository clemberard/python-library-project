# Projet Librairie

Bienvenue dans le projet Librairie ! Ce projet est une application de gestion de bibliothèque qui permet aux utilisateurs de gérer les livres et leur catégories, les auteurs et les emprunts.

## Lancement du projet en local

Pour lancer le projet en local, suivez les étapes ci-dessous :

1. **Cloner le dépôt** :

   ```bash
   git clone git@github.com:clemberard/python-library-project.git
    cd python-library-project
    ```

2. **Créer un environnement virtuel** :

    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows utilisez `venv\Scripts\activate`
    ```

3. **Installer les dépendances** :

    ```bash
    pip install -r requirements.txt
    ```

4. **Configurer la base de données** :

    La bdd est SQLite par défaut. Vous pouvez modifier la configuration dans `settings.py` si nécessaire.
    Exécutez les migrations pour créer les tables nécessaires :

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Lancer le serveur de développement** :

    ```bash
    python manage.py runserver
    ```

6. **Accéder à l'application** :
    Ouvrez votre navigateur et allez à l'adresse [http://127.0.0.1:8000/] pour accéder à l'application.

## Fonctionnalités

- Gestion des livres : ajout, modification et consultation des livres.
- Gestion des catégories : ajout et consultation des catégories.
- Gestion des auteurs : ajout, modification et consultation des auteurs.
- Gestion des emprunts : ajout, modification, suppression, retour d'emprunt et consultation des emprunts.

## Liens des différentes parties de l'application

- Livres : [http://127.0.0.1:8000/books/](http://127.0.0.1:8000/books/)
- Catégories : [http://127.0.0.1:8000/categories/](http://127.0.0.1:8000/categories/)
- Auteurs : [http://127.0.0.1:8000/authors/](http://127.0.0.1:8000/authors/)
- Emprunts : [http://127.0.0.1:8000/loans/](http://127.0.0.1:8000/loans/)
