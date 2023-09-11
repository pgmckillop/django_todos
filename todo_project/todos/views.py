from django.shortcuts import render

# Home page index.html
def index(request):
    return render(request, 'todos/index.html', {})

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