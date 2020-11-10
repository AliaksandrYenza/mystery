
from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, forms


class ArticlesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'intro', 'description', 'date', 'document']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                "placeholder" : "Notes name"
            }),
            'intro': TextInput(attrs={
                "class": "form-control",
                "placeholder" : "Intro"
            }),
            'description': Textarea(attrs={
                "class": "form-control",
                "placeholder":"Description: "
            }),
            'date': DateTimeInput(attrs={
                "class": "form-control",
                'placeholder': "Date"
            })
        }