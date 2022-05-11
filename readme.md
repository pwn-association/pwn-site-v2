=============================
PWN - 2015
=============================


Site web pour l'association PWN


Requirement
-----------
* Django : 3.2 *(https://docs.djangoproject.com/en/4.0/releases/3.2/)*
* Django CMS : 3.10
pour plus de detail voir requirements.txt


Pré-requis :
------------
* Python >= 3.8
* PostgreSQL >= 9.6 *(https://docs.djangoproject.com/en/4.0/releases/3.2/#dropped-support-for-postgresql-9-5)*


Install
-------
1. Créer un dossier pour le projet
2. Cloner le depot (https://github.com/pwn-association/pwn-site) dans le dossier nouvellement créé
3. Se placer à la racine du projet et créer un virtualenv avec la commande (un dossier venv-pwn va être créé):
    ```
    python -m venv venv-pwn
    ```

4. Activer le virtualenv :
    ```
    source venv-pwn/bin/activate
    ```

5. Si le virtualenv est correctement activé vous devez avoir le nom de l'env en parenthèse en début de ligne dans le terminal
6. Se placer dans le dossier de travail (pwn_v2) et installer les requirements :
    ```
    pip install -r requirements.txt
    ```

7. Copier le fichier **core/settings/local_dev.py** et le coller dans le même repertoire, sous le nom **local.py** et y inscrire, après les *"imports"* **SITE_ID=1**

8. Démarrer le serveur
    ```
    python manage.py runserver
    ```
   
Utilisation
-----------
Une fois le projet installé, vous pouvez le relancer :

1. Activer le virtualenv :
    ```
    source path_vers_votre_venv/bin/activate
    ```
   
2. Dans le repertoire de travail (où se trouve le fichier manage.py)
    ```
    python manage.py runserver
    ```