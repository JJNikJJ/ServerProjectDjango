from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html',data )
def about(request):
    return render(request, 'main/about.html')
def partners(request):
    return render(request, 'main/partners.html')
def profile(request):
    return render(request, 'main/profile.html')

