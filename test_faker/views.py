from dataclasses import field
import imp
from typing import List
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

# Create your views here.
class PersonListAPIView(ListAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()