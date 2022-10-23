from django.contrib import admin
from django.urls import path

from article.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/articlelist/', ArticleAPIList.as_view()),
    path('api/v1/articlelist/<int:pk>', ArticleAPIUpdate.as_view()),
    path('api/v1/articledetail/<int:pk>', ArticleAPIDetailView.as_view()),
]
