FlaskBoilerPlate
================

A straight-forward flask application structure

# Installation

~~~
pip install flask
pip install SQLAlchemy
pip install flask-sqlalchemy
~~~

# Folder Definition

* Assets - This is where you store all your static files such as js,css and img. It also has vendors folder where you can install some bower dependencies. Dont know how to use bower? http://blog.teamtreehouse.com/getting-started-bower
* Controllers - Response and Request layer. Controllers are responsible for rendering response and receiving requests.
* Repository - Repositories doesnt know anything about controllers,views,etc. All it does is to provide data coming from the models.
* Models - The abstraction of your tables.
* Templates - Jinja Templates
* Validations - This is where you put all the classes that are use for validations.



For any suggestions and violent reactions please drop me a message.