# Gamer_market_colombia

Se va a realizar una pagina Web en Django para la empresa Gamer Market Colombia

Se inicia el proyecto usando el codigo para crear el proyecto Django en la misma carpeta creada
# django-admin startproject gamerMarketCol .

Se crea el ambiente virtual llamado virtualenv
# python -m venv virtualenv

Se inicia el ambiente virtual
# "c:/Users/Paula Andrea/Desktop/gamer_Market_Colombia/virtualenv/Scripts/Activate.ps1"
Se instala Django en el ambiente
# pip install django 

Comprobamos que nuestro servidor este funcionando correctamente
# python manage.py runserver

Revisamos las migraciones pendientes
# python manage.py showmigrations

Realizamos las migraciones pendientes
# python manage.py migrate

Iniciamos la primera app Store para manejar los productos
# python manage.py startapp store

Registramos la app store en gamerMarketColombia en el archivo settings
# 'store',