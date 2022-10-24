from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from article.views import *

router = routers.SimpleRouter()
router.register(r'article', ArticleViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))

    # path('api/v1/articlelist/', ArticleAPIList.as_view()),
    # path('api/v1/articlelist/<int:pk>', ArticleAPIUpdate.as_view()),
    # path('api/v1/articledetail/<int:pk>', ArticleAPIDetailView.as_view()),
]
