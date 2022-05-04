=============================
PWN - 2015
=============================


Site web pour l'association PWN


Requirement
-----------
* Django : 3.10
* Django CMS : 3.10
pour plus de detail voir requirements.txt


Pré-requis :
------------
Python >= 3.8

Install
-------
#) Créer un dossier pour le projet
#) Cloner le depot (https://github.com/pwn-association/pwn-site) dans le dossier nouvellement créé
#) Se placer à la racine du projet et créer un virtualenv avec la commande (un dossier venv-pwn va etre créé):
[
    python -m venv venv-pwn
]

#) Activer le virtualenv :
[
    source venv-pwn/bin/activate
]
#) Si le virtualenv est correctement activé vous devez avoir le nom de l'env en parenthèse en début de ligne dans le terminal
#) Se placer dans le dossier de travail (pwn_v2) et installer les requirements :
[
    pip install -r requirements.txt
]
#) démarrer le serveur
[
    python manage.py runserver
]


Integration HTML
----------------
#) Tous les templates à modifier sont dans le dossier core/templates/
#) Les css, js etc doivent allés dans static/core/ ...


Gestion des gabarits de list event
----------------------------------
Pour ajouter un nouveau gabarit de "liste" ou "d'evenements à venir ou passés"
1 - aller dans core/settings/apps.py section "EVENTS"
2 - Ajouter le nouveau type de gabarit dans
ALDRYN_EVENTS_PLUGIN_STYLES  = [
        (_('pwn_list')),
        (_('pwn_list2'))
    ]

3 - Dans core/templates/aldryn_events/plugins/list et core/templates/aldryn_events/plugins/upcoming,
 dupliquer le dossier 'standard' et le renomer selon le nom donné dans la liste (par exple 'pwn_list2')


Gestion des tags
----------------
#) Page event_lists.html
    - j'ai modifié le template pour te donner un exemple de l'affichage des tags
    - tu peux choper le tag en cours d'utilisation avec : {{ event_tag }}

#) Page event_lists.html + event_detail.html
      Tu peux accéder à la liste de tous les tags en faisant :
      {% for tag in list_tag %}
        <a href="{% namespace_url "event-list-by-tag" tag.slug %}" >{{ tag.name }}</a>
      {% endfor %}

#) event_detail.html
    - exemple d'utilisation des tags de l'event en bas de page
    - exemple d'utilisation des intervenants de l'event en bas de page
