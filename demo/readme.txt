To run the server:

    python manage.py runserver

By default this will make the server available at http://localhost:8000

You can also specify a different port; e.g.

    python manage.py runserver 8300

will make the server available at http://localhost:8300

A REST-like API for cells is available at http://localhost:8000/api/cells
(It's not really RESTful because there should be something at /api/ that indicates that cells is a valid choice.)

You will need to have installed django and sqlparse. If you're using anaconda, it's:

    conda install django
    conda install sqlparse
