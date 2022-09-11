from django.shortcuts import render
from django.views import generic
from rest_framework import generics

from .models import Article
from .serializers import ArticleSerializer


class ArticleAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer