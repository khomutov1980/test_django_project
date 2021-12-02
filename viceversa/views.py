from django.shortcuts import render


def main_page(request):
    return render(request, 'home.html')


def reverse(request):
    return render(request, 'reverse.html')
