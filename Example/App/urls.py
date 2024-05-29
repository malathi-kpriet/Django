from .views import StudentView,SView,DeleteView
from django.urls import path

urlpatterns = [
    path('basic/', StudentView.as_view()),
    path('view/', SView.as_view()),
    path('delete/<int:id>',DeleteView.as_view()),
]