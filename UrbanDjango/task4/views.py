# Create your views here.
from django.shortcuts import render

# Create your views here.

def platform(request):
    text = 'купить'
    context = {
        'text': text,
    }

    return render(request, 'platform.html', context)


def games(request):
    text = 'купить'
    text1 = 'Attomic Heart '
    text2 = 'Cyberpunc 2077 '
    text3 = 'PayDay2 '
    mydict = {'games': ["Atomic Heart", "Cyberpunk 2077"]}
    context = {
        'mydict': mydict,
    }

    return render(request, 'games.html', context)


def cart(request):
    text = 'купить'
    context = {
        'text': text,
    }

    return render(request, 'cart.html', context)




# Create your views here.