import json
import logging

from django.shortcuts import render, redirect
from django.contrib import auth
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic

from django.contrib.auth.models import User

from .models import Message, Profile

# Get an instance of a logger
logger = logging.getLogger(__name__)


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


def register(request):

    logger.info('Triggered: views.register')
    if request.method == 'GET':
        return render(request, 'chatroom/register.html')

    if request.method == 'POST':

        # It is safe to create the user
        # Get post values and pass them to user
        user = User.objects.create_user(
            username=request.POST.get('username', ''),
            email=request.POST.get('email', ''),
            first_name=request.POST.get('first_name', ''),
            last_name=request.POST.get('last_name', ''),
            password=request.POST.get('password', ''),
        )
        user.save()

        user = User.objects.get(username=request.POST.get('username'))
        context = {
            'username': user.username,
            'fullname': user.get_full_name(),
            'user': user,
            'bio': request.POST.get('bio', ''),
            'organization': request.POST.get('organization', '')
            # 'bio': user.profile.location,
            # 'organization': user.profile.description,
        }

        profile = Profile(**context)
        profile.save()

        auth.login(request, user)

        # return redirect(reverse('u-profile', args=[username]))

        return render(request, 'chatroom/profile.html', context)


def show_profile(request):
    if request.method == 'GET':
        # Load html with user info
        profile = Profile.objects.get(username=request.user.username)
        context = {
            'username': profile.username,
            'fullname': profile.user.get_full_name(),
            'organization': profile.organization,
            'bio': profile.bio,
        }
        return render(request, 'chatroom/profile.html', context)

    if request.method == 'POST':
        # An attempt to edit the profile was triggered
        return redirect(reverse('u-profile-edit', args=[username]))


"""class SignUp(generic.CreateView):

    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'"""
