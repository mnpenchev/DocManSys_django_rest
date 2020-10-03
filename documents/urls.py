from django.urls import path
from .views import document_list, document_detail, DocumentAPIView, DocumentDetails

urlpatterns = [
    # path('document/', document_list),
    path('document/', DocumentAPIView.as_view()),
    # path('document/<int:pk>/', document_detail),
    path('document/<int:id>/', DocumentDetails.as_view()),
]
