#Débutez avec le framework Django
##creer une env
    py  -m venv env
##activation
    source env/Scripts/activate
##sauvegarder les dependances
    pip freeze > requirements.txt
##Générez du code de base pour un projet Django
     django-admin startproject merchex
##lancer le serveur
    py manage.py runserver
#creer une appli
    py manage.py startapp listings