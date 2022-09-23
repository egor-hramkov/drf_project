from django.forms import model_to_dict
from django.shortcuts import render
from django.views import generic
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticleSerializer


class ArticleAPIView(APIView):

    def get(self, request):
        a = Article.objects.all()
        return Response({"articles": ArticleSerializer(a, many=True).data})

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        article_new = Article.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'article': ArticleSerializer(article_new).data})

