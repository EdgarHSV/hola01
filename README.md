# CREATING A NEW PROJECT WITH A VIRTUAL ENVIROMENT

## Basic steps.
- Check installed version PYTHON: python --version
- Install Virtual Environment DEPENDENCY (if doesn't installed): pip install virtualenv
- Create VIRTUAL ENVIRONMENT: python -m virtualenv [python#] "VENV name" (Usually "name" is "venv").
- Activate VENV:
    + From VSC: View/Command Palette/"Python: Select Interpreter". Choose the interpreter on current folder.
    + From CMD: On the proyect folder execute: venv\scripts\activate.
- Install DJANGO: pip install django
- Update PIP (If suggested after Django install): python -m pip install --upgrade pip
- Verify Django VERSION (optional):python -m django --version
- Create PROJECT: python -m django startproject "project name" (The dot ".", avoid doble folder creation).
- Verify TEMPLATE PROJECT CREATION (Optional): python manage.py runserver.
- Create INITIAL APP: python manage.py startapp home (For the other APPs just change the "home" name).
- (Optional) To deploy on Pythonanywhere add URL web page generated by Pythonanywhere: 
    + Copy URL web page Pythonanywhere: [app_name_Pythonanuywhere].pythonanywhere.com
    + Add that URL in [project_folder_name]/settings.py within tag "".

## Deploying on PythonAnyWhere
- Create locally the "requirenments.txt" file to generate the virtual environment in Pythonanywhere.
- Create account by each project to deploy on Pythonanywhere. Use a temporal email (see SOURCES).
- Follow the steps in the deployment in Pytonanywhere help (see SOURCES section). 
- Code section. Important settings in the configuration:
    + Source code:              /home/[my_usernameor_site_name] (/home/test001es).
    + Working directory:        /home/[my_username_or_site_name]/[my_site] (/home/test001es/hola01).
    + WSGI configuration file:  The system ignores then project's WSGI file because it uses its own WSGI file.
        * Open link "/var/www/test001es_pythonanywhere_com_wsgi.py" to edit system's WSGI file.
        * Configure my site (django project in this WSGI file):
            ```
            # +++++++++++ DJANGO +++++++++++
            # To use your own django app use code like this:
            import os
            import sys
            #
            ## assuming your django settings file is at '/home/test001es/hola01/core/settings.py'
            ## and your manage.py is is at '/home/test001es/hola01/manage.py'
            path = '/home/test001es/hola01/core'
            if path not in sys.path:
                sys.path.append(path)
                #####sys.path.insert(0,path)
                os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
            from django.core.wsgi import get_wsgi_application
            application = get_wsgi_application()
            ```
            note: Pending to add "static files"
    + Python version: Normally is the suggested by Pythonanywhere
- Virtualenv section. Important settings in the configuration:
    + Generate locally "requirenments.txt" file: pip freeze > requirenments.txt
    + Export local "requirenments.txt" file to the repository: git add|commit|push
    + Import "requirenments.txt" file from repository GITHUB to repository Pythonanywhere.
    + Generate the pakages instalation with "requirenments.txt" file: pip install - r requirenments.txt
- Static files section: Configurate static files as instructed in the help.
- Security section: Initially enable "Force HTTPS".

# SOURCES:
- Clase 01 - Entorno Django en VSCode y crea tu primer proyecto (https://youtu.be/ZmtktIlOErk).
- Temporal emails site (https://temp-mail.org/en/).
- Pythonanywhere site (https://www.pythonanywhere.com/login/).
- Deploying on Pytonanywhere help (https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/).

