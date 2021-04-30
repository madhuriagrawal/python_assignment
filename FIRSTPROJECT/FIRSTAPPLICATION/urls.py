from django.urls import path

from . import views

urlpatterns = [
    path('indexview', views.index, name='index'),
    path('customerview', views.CustomerView, name="form"),
    path('employeeview', views.EmployeeView, name="form"),
    path('bookview', views.BookView, name="form")
]