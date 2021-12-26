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

Creamos el superusuario para poder entrar al admin
# python manage.py createsuperuser
Usuario: admin Contraseña: admin

Se crea el primer modelo Category en la app Store
- name
- slug

Se crea el segundo modelo Product en la app Stored
- Llave Foranea al modelo Category.
- la persona que creo el producto created_by, que es una llave foranea del USER
- nombre del producto name
- Descripcion del producto description
- Imagen del producto image
- slug
- Precio del Producto price
- Si se cuenta con Stock in_stock
- si la publicacion esta Activa is_active
- Fecha de Creacion de la Publicacion created
- Fecha de Actualizacion updated

Se instala Pillow en el ambiente para poder manejar imagenes
# pip install Pillow

Se realizan las migraciones a la base de datos

Se registra el modelo en el admin de la app Store