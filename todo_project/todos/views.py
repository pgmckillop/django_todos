from django.shortcuts import render
from .models import List
from .forms import ListForm

# Home page index.html
def index(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            return render(request, 'todos/index.html', {'all_items': all_items})
    else:
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