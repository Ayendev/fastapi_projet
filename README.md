# Projet 3DVP : API REST pour la Gestion d'Items

Ce projet est une API RESTful développée avec FastAPI, un framework web moderne et performant pour construire des APIs avec Python. L'API permet de gérer des items (produits) et users (utilisateurs) dans une base de données.

## Fonctionnalités

L'API implémente les opérations CRUD (Create, Read, Update, Delete) pour les items & users :

* **Créer un item :** Ajouter un nouvel item à la base de données.
* **Lire les items :** Récupérer la liste de tous les items.
* **Lire un item :** Récupérer un item spécifique par son ID.
* **Mettre à jour un item :** Modifier les informations d'un item existant.
* **Supprimer un item :** Supprimer un item de la base de données.

* **Créer un user :** Ajouter un nouvel user à la base de données.
* **Lire les users :** Récupérer la liste de tous les users.
* **Lire un user :** Récupérer un user spécifique par son ID.
* **Mettre à jour un user :** Modifier les informations d'un user existant.
* **Supprimer un user :** Supprimer un user de la base de données.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

* **Python 3.9+**
* **pip & venv** (pour la gestion des dépendances et l'environnement virtuel)
* **Une base de données PostgreSQL** (locale ou en ligne)

## Installation

1.  **Cloner le dépôt :**

    ```bash
    git clone https://github.com/Ayendev/fastapi_projet.git
    cd fastapi_projet
    ```

2.  **Installer les dépendances avec pip :**

    ```bash
    pip install
    ```

3.  **Configurer les variables d'environnement :**

    * Créez un fichier `.env` à la racine du projet.
    * Ajoutez les variables d'environnement nécessaires pour la connexion à la base de données :

        ```
        PG_USER=<votre_nom_utilisateur_postgres>
        PG_PASSWORD=<votre_mot_de_passe_postgres>
        PG_HOST=<l'hôte_de_votre_base_de_données> (par exemple, localhost, une adresse IP, ou un nom d'hôte Render)
        PG_PORT=<le_port_de_votre_base_de_données> (par défaut, 5432)
        PG_DB=<le_nom_de_votre_base_de_données>
        ```
    * Remplacez les valeurs entre `<>` par les informations de votre propre base de données.

## Configuration de la base de données

* **Localement :** Si vous utilisez une base de données PostgreSQL locale, assurez-vous que le serveur est en cours d'exécution et que vous avez créé une base de données avec le nom spécifié dans la variable d'environnement `PG_DB`.
* **Render :** Si vous déployez sur Render, vous devrez créer un service de base de données PostgreSQL sur Render et configurer les variables d'environnement de votre service d'application avec les informations de connexion fournies par Render.

## Utilisation

1.  **Activer l'environnement virtuel :**

    ```bash
    env/Script/Activate.ps1
    ```

2.  **Exécuter l'application :**

    ```bash
    uvicorn main:app --reload
    ```

    ou

    
    ```bash
    fastapi dev main 
    ```

    L'API sera accessible à l'adresse [http://localhost:8000](http://localhost:8000).

## Tester l'API

Vous pouvez utiliser un client HTTP comme Postman, Insomnia, curl ou directement sur la docs de swagger pour tester les différents endpoints de l'API.

## Tests

Le projet inclut des tests d'intégration pour vérifier le bon fonctionnement de l'API.

1.  **Configurer la base de données de test :**
    * Il est **fortement recommandé** d'utiliser une base de données PostgreSQL distincte pour les tests.
    * Vous pouvez configurer une base de données de test locale ou utiliser un service de base de données en ligne (comme Render) pour les tests.
    * Définissez les variables d'environnement `TEST_PG_*` dans votre environnement de test (par exemple, dans GitHub Actions) pour la connexion à la base de données de test.

2.  **Exécuter les tests avec pytest :**

    ```bash
    pytest tests/
    ```

## Déploiement sur Render

Voici les étapes générales pour déployer cette API sur Render :

1.  **Créer un compte Render :** Si vous n'en avez pas déjà un, créez un compte sur [Render](https://render.com/).
2.  **Créer un service Web :** Créez un nouveau service Web à partir de votre dépôt GitHub.
3.  **Configurer les variables d'environnement :** Ajoutez les variables d'environnement `PG_*` (et `TEST_PG_*` si vous avez une base de données de test séparée) dans les paramètres de votre service Render. Ces variables doivent correspondre aux informations de connexion de votre base de données PostgreSQL hébergée sur Render.
4.  **Configurer la commande de démarrage :** `uvicorn main:app --host 0.0.0.0 --port 10000` (ou le port que vous préférez)
5.  **Déployer :** Déployez votre service. Render construira votre application et la déploiera.

## Structure du projet

projet_fastapi/├── main.py          # Le point d'entrée de l'application FastAPI├── models/        # Les modèles SQLModel (Item, etc.)│   └── items.py├── database.py      # La configuration de la base de données (SQLAlchemy)├── tests/         # Les tests d'intégration│   └── test_main.py├── .env           # Fichier pour les variables d'environnement (local)├── pyproject.toml   # Configuration de Poetry└── README.md        # Ce fichier
## Contributions

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence

Ce projet est sous licence [MIT](LICENSE).
