from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm
from .models import Event


def index(request):
    context = {"tag_var":"tag_var"}
    return render(request,'index.html',context)

def EventPost(request):
    if request.method == "POST":

        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/CRUDAPP/eventview')

    else:
        form = EventForm()
    context = {"form": form}
    return render(request, "eventpage.html", context)


def EventView(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Event.objects.all()

    return render(request, "event_view.html", context)

def DeleteView(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Event, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return redirect('/CRUDAPP/eventview')

    return render(request, "delete_view.html", context)


def DetailView(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = Event.objects.get(id=id)

    return render(request, "detail_view.html", context)


def UpdateView(request, id):
    event = Event.objects.get(id=id)
    form = EventForm(request.POST, instance=event)
    if form.is_valid():
        form.save()
        return redirect('/CRUDAPP/eventview')
    return render(request, 'update_view.html', {'event': event})



