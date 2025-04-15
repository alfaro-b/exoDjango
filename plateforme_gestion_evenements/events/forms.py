from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={'placeholder': 'JJ/MM/AAAA'})
    )
    class Meta:
        model = Event
        fields = ['titre', 'description', 'date', 'lieu','capacite']