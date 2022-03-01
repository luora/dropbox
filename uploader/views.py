from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import parsers
from uploader.models import DropBox
from uploader.serializers import DropBoxSerializer

# Create your views here.

class DropBoxViewSet(ModelViewSet):

    queryset = DropBox.objects.all()

    serializer_class = DropBoxSerializer

    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']