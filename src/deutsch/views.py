from django.shortcuts import render

from .models import WordList


def index(request):
    word_lists = WordList.objects.all()
    context = {'word_lists': word_lists}
    return render(request, 'deutsch/index.html', context)


def wordlist(request, slug: str):
    word_list = WordList.objects.filter(slug=slug).first()
    context = {'word_list': word_list}
    return render(request, 'deutsch/wordlist.html', context)
