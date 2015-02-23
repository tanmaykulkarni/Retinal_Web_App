from django.http import HttpResponse
from django.views.generic import ListView 

from django.template import Context, loader 
from django.template import RequestContext
from django.shortcuts import render, render_to_response, RequestContext
from retinalwebapp.models import User
from .forms import SignUpForm

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

def home(request):

    form = SignUpForm(request.POST or None)	

    if form.is_valid():
      save_it = form.save(commit=False)
      save_it.save()

    return render_to_response("index.html",locals(), context_instance=RequestContext(request))



