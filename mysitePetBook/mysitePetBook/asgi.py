# from http://bit.ly/herokuDjangoChatSystem

import os
import channels.asgi
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Chat.settings")
django.setup()

channel_layer = channels.asgi.get_channel_layer()
application = get_default_application()
