from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')
def about(request):
    return render(request, 'main/about.html')
def partners(request):
    return render(request, 'main/partners.html')
def profile(request):
    return render(request, 'main/profile.html')

