from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def testpage(request):
    return render(request, 'test.html')