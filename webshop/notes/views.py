from django.shortcuts import render, redirect

from .forms import ArticlesForm
from .models import Artiles
# Create your views here.


def notes_home(request):
    # title = {'title': 'Notes home'}
    notes = Artiles.objects.order_by('title')
    return render(request, 'notes/notes_home.html', {'notes': notes})


def create(request):
    error_msg = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes_home')
        else:
            error_msg = 'Form filled invalid'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error_msg
    }
    return render(request, 'notes/create.html', data)

