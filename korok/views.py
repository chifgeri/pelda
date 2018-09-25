from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Hallgato, Kor

class HallgatoDetailView(DetailView):
    template = 'korok/hallgato_detail.html'

    queryset = Hallgato.objects.all()

class HallgatoListView(ListView):
    template = 'korok/hallgato_list.html'

    hallgato_list = Hallgato.objects.all()

    def get_queryset(self):
        return Hallgato.objects.all()

class KorListView(ListView):
    template = 'korok/kor_list.html'

    kor_list = Kor.objects.all()

    def get_queryset(self):
        return Kor.objects.all()
# Create your views here.
