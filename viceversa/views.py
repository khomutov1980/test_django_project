from django.shortcuts import render


def main_page(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['user_text']
    reversed_text = user_text[::-1]
    words_count = len(user_text.split())
    return render(request, 'reverse.html', {'usertext': user_text, 'reversedtext': reversed_text, 'wordscount': words_count})
