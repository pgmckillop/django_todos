from django.shortcuts import render

# Home page index.html
def index(request):
    return render(request, 'todos/index.html', {})

def about(request):
    return render(request, 'todos/about.html', {})