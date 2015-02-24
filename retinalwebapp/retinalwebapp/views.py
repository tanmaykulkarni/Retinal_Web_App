from django.http import HttpResponse
from django.views.generic import ListView 
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import Context, loader 
from django.template import RequestContext
from django.shortcuts import render, render_to_response, RequestContext
from retinalwebapp.models import User
from .forms import SignUpForm, LoginForm

# Create your views here.
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


# this is the home view which incorporates the form for logging in as well as signing up
def home(request):

    form_signup = SignUpForm(request.POST or None)	
    form_login = LoginForm(request.POST or None)

    if form_signup.is_valid():
      save_it = form.save(commit=False)
      save_it.save()

    return render_to_response("index.html",locals(), context_instance=RequestContext(request))




def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("index.html", c)






def auth_views(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
       auth.login(request, user)
       return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpsResponseRedirect('/accounts/invalid')












def loggedin(request):
    return render_to_response('choose_activity.html',
           
                  {'full_name': request.user.username})






def invalid_login(request):
    return render_to_request('index.html')
