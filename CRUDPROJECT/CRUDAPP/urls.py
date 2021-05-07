from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('eventpost', views.EventPost, name="form"),
    path('delete/<id>', views.DeleteView ),
    path('eventview', views.EventView),
    path('updateview/<id>', views.UpdateView, name="form"),
    path('detailview/<id>', views.DetailView, name='detail'),




]