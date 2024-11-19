# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import book

# Create a model serializer


class bookSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = book
        fields = ('title', 'description')
