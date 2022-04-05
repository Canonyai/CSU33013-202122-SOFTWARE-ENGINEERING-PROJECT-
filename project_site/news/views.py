from django.shortcuts import render


def home(request):
    return render(request, 'news/index.html', {'title': 'Home'})

def entertainment(request):
    return render(request, 'news/entertainment.html', {'title': 'Entertainment'})

def health(request):
    return render(request, 'news/health.html', {'title': 'Health'})

def science(request):
    return render(request, 'news/index.html', {'title': 'Science'})

def sports(request):
    return render(request, 'news/entertainment.html', {'title': 'Sports'})

def technology(request):
    return render(request, 'news/entertainment.html', {'title': 'Technology'})
