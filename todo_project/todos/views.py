from django.shortcuts import render
from .models import List

# Home page index.html
def index(request):
    all_items = List.objects.all
    return render(request, 'todos/index.html', {'all_items': all_items})

def about(request):
    wholename = "Paul McKillop"
    forename = "Paul"
    surname = "McKillop"
    organisation = "The Isle of Wight College"
    context = {
        'name': wholename,
        'organisation': organisation,
        'forename': forename,
        'surname': surname
    }
    return render(request, 'todos/about.html', context)