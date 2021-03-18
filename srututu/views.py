from django.forms import inlineformset_factory
from django.shortcuts import render

# Create your views here.
from django.views import View

from .forms import F
from .models import Koszyk, ZawartoscKoszyka


class Indekso(View):
    def get(self, request):
        form = F()
        zawartosc_form = inlineformset_factory(Koszyk, ZawartoscKoszyka, fields=['produkt', 'liczba'])
        return render(request, 'index.html', {'form': form, 'zawartosc_form':zawartosc_form})
