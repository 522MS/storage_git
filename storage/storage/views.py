from django.shortcuts import render


def index(request):
    title = 'магазин'

    context = {
        'title': title,
    }

    return render(request, 'storage/index.html', context=context)