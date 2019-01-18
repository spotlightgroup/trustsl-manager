"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from main.ThreadedServer import ThreadedServer
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")


while True:
    port_num = input("TCP Port? ")
    try:
        port_num = int(port_num)
        break
    except ValueError:
        pass
# run the tcp socket server
ThreadedServer('', port_num).listen()

# run http server
application = get_wsgi_application()
