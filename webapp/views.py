# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import TodoListModel
from . serializer import TodoListSerializer

# Create your views here.
class TodoListView(APIView):

    def get(self, request):
        task1 = TodoListModel.objects.all()
        serializer = TodoListSerializer(task1, many=True)
        return Response(serializer.data)


    def post(self):
        pass