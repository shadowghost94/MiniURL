from django import forms
from mini_url.models import MiniURL

class MiniUrlForm(forms.ModelForm):
    class Meta:
        model = MiniURL
        fields = ('urlLongue', 'pseudo')