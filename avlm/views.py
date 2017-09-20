from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from ProjetoIntelivix.settings import HOSTNAME
from avlm.models import ShortURL
from .forms import ShortURLForm

# Create your views here.


def index(request):
    return render_to_response('avlm/index.html')


def redirect(request, param_hash):
    object_url = ShortURL.objects.filter(url_hash=param_hash).values('url_hash', 'url_redirect')

    for obj in object_url:
        return render(request, 'avlm/redirect.html', {'dados': obj['url_redirect']})


def sign_up(request):
    if request.user.is_authenticated:
        return render_to_response('avlm/shortener.html')
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)

            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/login')
            else:
                return render(request, 'avlm/sign_up.html', {'form': form})

        return render(request, 'avlm/sign_up.html', {'form': UserCreationForm()})


def sign_in(request):
    if request.user.is_authenticated:
        return render_to_response('avlm/shortener.html')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)

            if form.is_valid():
                login(request, form.get_user())
                return HttpResponseRedirect('/shortener')
            else:
                return render(request, 'avlm/sign_in.html', {'form': form})

        return render(request, 'avlm/sign_in.html', {'form': AuthenticationForm()})


def shortener(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ShortURLForm(request.POST)
            if form.is_valid():
                short_url = form.save(commit=False)
                short_url.id_user = request.user
                short_url.url_hash = short_url.get_hash()
                short_url.save()

                return render(request, 'avlm/shortener.html', {
                    'form': ShortURLForm(),
                    'success': True, 'short_url': 'http://avlm.pythonanywhere.com'+'/'+short_url.url_hash, 'url_hash': short_url.url_hash})
        else:
            form = ShortURLForm()

        return render(request, 'avlm/shortener.html', {'form': form})
    else:
        return HttpResponseRedirect('/login')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login')
