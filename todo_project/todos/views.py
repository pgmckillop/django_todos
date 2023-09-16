from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Home page index.html
def index(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, 'Item has been added')
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


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been deleted!'))
    return redirect(index)

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('index')


def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('index')


def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been edited'))
            return redirect('index')
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'todos/edit.html', {'item': item})