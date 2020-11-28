from django.urls import path
from .views import DocumentAPIView, DocumentDetails

urlpatterns = [
    path('document/', DocumentAPIView.as_view()),
    path('document/<int:id>/', DocumentDetails.as_view()),
]

