from django.http import HttpResponse
from django.views.generic import ListView 

from django.template import Context, loader 

from django.shortcuts import render
from retinalwebapp.models import User

# Create your views here.
def home(request):
    users = User.objects.all()

    template = loader.get_template('index.html')

    context = Context({
      'users_list' : users
    })

    return HttpResponse(template.render(context))

def signup(request):
    users = User.objects.all()

    template = loader.get_template('register.html')

    context = Context({
      'users_list' : users
    })

    return HttpResponse(template.render(context))

def choose_activity(request):
    users = User.objects.all()

    template = loader.get_template('choose_activity.html')

    context = Context({
      'users_list' : users
})
    return HttpResponse(template.render(context))

def annotation(request):
    users = User.objects.all()

    template = loader.get_template('annotation.html')

    context = Context({
      'users_list' : users
})

    return HttpResponse(template.render(context))


