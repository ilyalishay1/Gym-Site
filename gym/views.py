from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import *


def index(request):
    return render(request, 'gym/index.html')


def team(request):
    return render(request, 'gym/team.html')


def price(request):
    return render(request, 'gym/price.html')


def about_us(request):
    return render(request, 'gym/about_us.html')


def contacts(request):
    return render(request, 'gym/contacts.html')


def services(request):
    return render(request, 'gym/services.html')


def suplements(request):
    posts = Suplement.objects.all()
    context = {'posts': posts}
    return render(request, 'gym/suplements.html', context=context)


def protein(request):
    posts = Suplement.objects.filter(cat=1)
    context = {'posts': posts}
    return render(request, 'gym/protein.html', context=context)


def creatin(request):
    posts = Suplement.objects.filter(cat=2)
    context = {'posts': posts}
    return render(request, 'gym/creatin.html', context=context)


def bcaa(request):
    posts = Suplement.objects.filter(cat=3)
    context = {'posts': posts}
    return render(request, 'gym/bcaa.html', context=context)


def vitamins(request):
    posts = Suplement.objects.filter(cat=4)
    context = {'posts': posts}
    return render(request, 'gym/vitamins.html', context=context)


def preworkout(request):
    posts = Suplement.objects.filter(cat=5)
    context = {'posts': posts}
    return render(request, 'gym/preworkout.html', context=context)


def amins(request):
    posts = Suplement.objects.filter(cat=6)
    context = {'posts': posts}
    return render(request, 'gym/amins.html', context=context)


def boosters(request):
    posts = Suplement.objects.filter(cat=7)
    context = {'posts': posts}
    return render(request, 'gym/boosters.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h2>Страница не найдена</h2>')
