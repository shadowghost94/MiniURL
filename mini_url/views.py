from django.shortcuts import render, redirect, get_object_or_404
from mini_url.models import MiniURL
from mini_url.forms import MiniUrlForm

# Create your views here.
def liste(request):
    """ Affichage des redirections """
    minis = MiniURL.objects.order_by('-nb_acces')

    return render(request, 'mini_url/liste.html', locals())

def nouveau(request):
    """ Ajout d'une redirection """
    if request.method == "POST":
        form = MiniUrlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(liste)
    else:
        form = MiniUrlForm()

    return render(request, 'mini_url/nouveau.html', locals(), {'form': form})

def redirection(request, code):
    """ Redirection vers l'url enregistrée """
    mini = get_object_or_404(MiniURL, code=code)
    mini.nb_acces +=1
    mini.save()

    return redirect(mini.url, permanent=True)