from django.http import HttpResponse
from .models import Document
from .serializers import DocumentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication #, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class DocumentAPIView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication] #, TokenAuthentication
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DocumentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentDetails(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Document.objects.get(id=id)
        except Document.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        document = self.get_object(id)
        serializer = DocumentSerializer(document)
        return Response(serializer.data)

    def put(self, request, id):
        document = self.get_object(id)
        serializer = DocumentSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        document = self.get_object(id)
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
