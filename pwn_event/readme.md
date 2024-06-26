PWN EVENT APP
-------------
todo : 
 - ajouter desciption du projet
 - admin custom
 - integration avec django cms
 - gestion de publication des event (via manager)
 - ajouter preview dans l'admin


Template tags
-------------
Il est possible d'afficher les x derniers events sur n'importe quelle page à l'aide du tag : *get_last_events*

**Utilisation :**

1. dans le template html charger les tags de l'app : **{% load i18n pwn_event %}**
2. **{% get_last_events X %}** ou **X** est un entier et est facultatif

Exemple dans *templates/pwn_event/home.html*


