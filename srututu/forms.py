from django.forms import ModelForm

from .models import Koszyk


class F(ModelForm):
    class Meta:
        model = Koszyk
        fields = ['name']
