# from http://bit.ly/herokuDjangoChatSystem

import os
import channels.asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysitePetBook.settings")
channel_layer = channels.asgi.get_channel_layer()
