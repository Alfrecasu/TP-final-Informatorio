from django import forms
from .models import Comentario


class OpinionForm(forms.ModelForm):

    class Meta: 
        model = Comentario
        fields = ['texto']