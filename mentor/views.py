from django.shortcuts import render


def login(request):
    return render(request, 'login.html', {'next': request.GET.get('next', '/')})
