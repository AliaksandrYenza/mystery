from django.shortcuts import render, redirect
from .forms import ArticlesForm
from .models import Artiles
from django.views.generic import DetailView, UpdateView


# Create your views here.


def notes_home(request):
    # title = {'title': 'Notes home'}
    notes = Artiles.objects.order_by('title')
    return render(request, 'notes/notes_home.html', {'notes': notes})


class NotesDetailView(DetailView):
    model = Artiles
    template_name = 'notes/detail_view.html'
    context_obj_name = 'artiles'  # the name of the key on which the key is passed inside


class NotesUpdateView(UpdateView):
    model = Artiles
    template_name = 'notes/create.html'
    form_class = ArticlesForm


class NotesDeleteView(DetailView):
    model = Artiles
    success_url = '/notes/'
    template_name = 'notes/notes_delete.html'


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
