# hola01
Test VERCEL with a simple project django

# CREATING A NEW PROJECT WITH A VIRTUAL ENVIROMENT

1. Check installed version PYTHON: python --version
2. Install Virtual Environment DEPENDENCY (if doesn't installed): pip install virtualenv
3. Create VIRTUAL ENVIRONMENT: python -m virtualenv [python#] "VENV name" (Usually "name" is "venv").
4. Activate VENV:
    2.1. From VSC: View/Command Palette/"Python: Select Interpreter". Choose the interpreter on current folder.
    2.2. From CMD: On the proyect folder execute: venv\scripts\activate.
5. Install DJANGO: pip install django
6. Update PIP (If suggested after Django install): python -m pip install --upgrade pip
7. Verify Django VERSION (optional):python -m django --version
8. Create PROJECT: python -m django startproject "project name" (The dot ".", avoid doble folder creation).
9. Verify TEMPLATE PROJECT CREATION (Optional): python manage.py runserver.
10. Create INITIAL APP: python manage.py startapp home (For the other APPs just change the "home" name).


## SOURCE
- Clase 01 - Entorno Django en VSCode y crea tu primer proyecto (https://youtu.be/ZmtktIlOErk).
