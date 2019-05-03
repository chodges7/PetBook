# from channels tutorials chat/views.py

import json
from django.shortcuts import render
from django.utils.safestring import mark_safe

def index(request):
    return render(request, 'chat/index.html', {'title':"New chat room"})

def room(request, room_name):
    title = room_name + " Chat room"
    context = {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': request.user,
        'title': title,
    }
    return render(request, 'chat/room.html', context=context)
