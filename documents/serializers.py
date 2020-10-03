from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):      # Model Serializer
    class Meta:
        model = Document
        # fields = ['id', 'address', 'title', 'body', 'date', 'signed', 'status', 'author']
        fields = '__all__'
