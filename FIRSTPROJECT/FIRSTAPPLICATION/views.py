from django.shortcuts import render, redirect
from .forms import CustomerForm, EmployeeForm, BookForm


def index(request):
    context = {"tag_var":"tag_var"}
    return render(request,'index.html',context)

def BookView(request):
    if request.method == "POST":

        form = BookForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = BookForm()
    context = {"form": form}
    return render(request, "bookpage.html", context)

def CustomerView(request):

    if request.method == "POST":

        form = CustomerForm(request.POST)
        if form.is_valid():

            form.save()

    else:
        form = CustomerForm()
    context = {"form":form}
    return render(request, "eventpage.html",context)

def EmployeeView(request):

    if request.method == "POST":

        form = EmployeeForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect("./employeeview")

    else:
        form = EmployeeForm()
    context = {"form":form}
    return render(request, "employeepage.html",context)