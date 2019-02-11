import json

from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .models import Message


@login_required
def index(request):

    return render(request, 'chatroom/index.html', {})


@login_required
def room(request, room_name):

    messages = Message.objects.retrieve(room_name)

    contents = [{'author': msg.username, 'message': msg.text} for msg in messages]

    context = {
        'room_name': mark_safe(room_name),
        'messages': contents
    }

    return render(request, 'chatroom/room.html', context)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
