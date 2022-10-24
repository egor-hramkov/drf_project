from django.forms import model_to_dict
from django.shortcuts import render
from django.views import generic
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# class ArticleAPIList(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
# class ArticleAPIUpdate(generics.UpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
# class ArticleAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class ArticleAPIView(APIView):
#     def get(self, request):
#         a = Article.objects.all()
#         return Response({"articles": ArticleSerializer(a, many=True).data})
#
#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'article': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': "Method PUT not allowed"})
#         try:
#             instance = Article.objects.get(pk=pk)
#         except:
#             return Response({'error': "Object does not exists"})
#
#         serializer = ArticleSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'article': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': "Method DELETE not allowed"})
#         try:
#             instance = Article.objects.get(pk=pk)
#         except:
#             return Response({'error': "Object does not exists"})
#
#         instance.delete()
#
#         return Response({'article': "delete article" + str(pk)})