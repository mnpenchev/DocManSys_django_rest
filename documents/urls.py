from django.urls import path
from .views import document_list

urlpatterns = [
    path('document/', document_list),
]