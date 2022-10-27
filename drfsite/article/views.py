from _ast import Is

from django.forms import model_to_dict
from django.shortcuts import render
from django.views import generic
from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import *
from .permissions import *
from .serializers import *


class ArticleViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # @action(methods=['get'], detail=False)
    # def category(self, request):
    #     categories = Category.objects.all()
    #     return Response({'categories': [c.name for c in categories]})


class CatsViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CatsSerializer

class ArticleAPIListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100

class ArticleAPIList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = ArticleAPIListPagination


class ArticleAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = (IsOwnerOrReadOnly,)
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)


class ArticleAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (ISAdminOrReadOnly,)

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
