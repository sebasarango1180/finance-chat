import json

from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


@login_required
def index(request):

    return render(request, 'chatroom/index.html', {})


@login_required
def room(request, room_name):

    return render(request, 'chatroom/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
