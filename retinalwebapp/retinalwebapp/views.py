from django.http import HttpResponse
from django.views.generic import ListView 
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import Context, loader 
from django.template import RequestContext
from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.forms import UserCreationForm
from retinalwebapp.models import User
from .forms import SignUpForm, LoginForm


# list of mobile User Agents
mobile_uas = [
	"w3c ", "acs-", "alav", "alca", "amoi", "audi",
        "avan", "benq", "bird", "blac", "blaz", "brew",
        "cell", "cldc", "cmd-", "dang", "doco", "eric",
        "hipt", "inno", "ipaq", "java", "jigs", "kddi",
        "keji", "leno", "lg-c", "lg-d", "lg-g", "lge-",
        "maui", "maxo", "midp", "mits", "mmef", "mobi",
        "mot-", "moto", "mwbp", "nec-", "newt", "noki",
        "xda",  "palm", "pana", "pant", "phil", "play",
        "port", "prox", "qwap", "sage", "sams", "sany",
        "sch-", "sec-", "send", "seri", "sgh-", "shar",
        "sie-", "siem", "smal", "smar", "sony", "sph-",
        "symb", "t-mo", "teli", "tim-", "tosh", "tsm-",
        "upg1", "upsi", "vk-v", "voda", "wap-", "wapa",
        "wapi", "wapp", "wapr", "webc", "winw", "xda-",
	]
 
mobile_ua_hints = [ 'SymbianOS', 'Opera Mini', 'iPhone' ]







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
    
    # checking if the signup form is valid and saving it if so
    if form_signup.is_valid():
      save_it = form.save(commit=False)
      save_it.save()

    # check if the login credentials match...
    
    
    return render_to_response("index.html",locals(), context_instance=RequestContext(request))




def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("index.html", c)






def auth_views(request):
    # this has been modified from <>
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
       auth.login(request, user)
       return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')












def loggedin(request):
    return render_to_response('choose_activity.html',
           
                  {'full_name': request.user.username})






def invalid_login(request):
    return render_to_request('index.html')



def register_user(request):
    if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
          form.save()
          return HttpResponseRedirect('choose_activity.html')


    args = {}
    args.update(csrf(request))

    args['form'] = UserCreationForm()

    return render_to_response('index.html', args)







def mobileBrowser(request):
    ''' Super simple device detection, returns True for mobile devices '''
 
    mobile_browser = False
    ua = request.META.get('HTTP_USER_AGENT','').lower()[0:4]
 
    if (ua in mobile_uas):
        mobile_browser = True
    else:
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True
 
    return mobile_browser
 
 
def index(request):
    '''Render the index page'''
 
    if mobileBrowser(request):
        t = loader.get_template('m_index.html')
    else:
        t = loader.get_template('m_index.html')
 
    # c = Context( { }) # normally your page data would go here
    c = RequestContext({})
 
    return HttpResponse(t.render(c))

