# from http://bit.ly/herokuDjangoChatSystem

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Chat.settings")
channel_layer = channels.asgi.get_channel_layer()
