from rest_framework import serializers
from .models import Document

#
# class DocumentSerializer(serializers.Serializer):
#     class Meta:
#         model = Document
#         fields = ['id', 'address', 'title']

# , 'body', 'date', 'signed', 'status', 'author'


class DocumentSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    body = serializers.CharField(max_length=2000)
    date = serializers.DateField()
    # signature = serializers.ImageField()
    signed = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    # notes = serializers.CharField(max_length=400)

    def create(self, validated_data):
        return Document.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.address = validated_data.get('address', instance.address)
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.date = validated_data.get('date', instance.date)
        # instance.signature = validated_data.get('signature', instance.signature)
        instance.signed = validated_data.get('signed', instance.signed)
        instance.status = validated_data.get('status', instance.status)
        instance.author = validated_data.get('author', instance.author)
        # instance.notes = validated_data.get('notes', instance.notes)
        instance.save()
        return instance
