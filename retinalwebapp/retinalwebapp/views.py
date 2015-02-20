from django.http import HttpResponse
from django.views.generic import ListView 

from django.template import Context, loader 

from django.shortcuts import render
from retinalwebapp.models import User

# Create your views here.
def home(request):
    # template_name = "index.html"

    users = User.objects.all()

    template = loader.get_template('index.html')

    context = Context({
      'users_list' : users
    })

    return HttpResponse(template.render(context))

def login(request):
    return HttpResponse("I <3 iLabelIT")

def signup(request):
    return HttpResponse("I <3 iLabelIT")

