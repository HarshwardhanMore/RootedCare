from django.shortcuts import render

# Create your views here.


def owner(request):
    return render(request, 'owner.html')


def caretaker(request):
    return render(request, 'caretaker.html')
