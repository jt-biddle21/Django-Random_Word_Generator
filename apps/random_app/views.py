from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    return render(request, 'random_app/index.html')


def generator(request):
    try:
        request.session['count']
    except KeyError:
        request.session['count'] = 0
    if request.method == "POST":
        print "posting"
        random_word = get_random_string(length=15)
        request.session['rand'] = random_word
        request.session['count'] += 1
        return redirect('/')
