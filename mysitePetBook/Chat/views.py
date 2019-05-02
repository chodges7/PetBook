# from channels tutorials chat/views.py

from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'chat/index.html', { 'title':"New chat room" })

def room(request, room_name):
    title = room_name + " Chat room"
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)), 
        'username':request.user,
        'title':title,
        })
