from django.shortcuts import render

from django.utils.safestring import mark_safe
import json
from django.http import JsonResponse


def index(request):
    return render(request, 'index.htm', {})

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
def test(request):
    return render(request,'test.html')
def listen_this(request,safe=False):
    username = ' succesful'
    data = {
        'hello':'jidnyesh',
    }
    
    return JsonResponse(data)
