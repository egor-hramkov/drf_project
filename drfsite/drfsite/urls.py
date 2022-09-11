from django.contrib import admin
from django.urls import path

from article.views import ArticleAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/articlelist/', ArticleAPIView.as_view()),
]
