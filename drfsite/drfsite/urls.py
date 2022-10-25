from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from article.routers import MyCustomRouter

from article.views import *

router = routers.SimpleRouter()
router2 = MyCustomRouter()

router.register(r'article', ArticleViewSet)
router2.register(r'article/cats', CatsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(router2.urls)),

    # path('api/v1/articlelist/', ArticleAPIList.as_view()),
    # path('api/v1/articlelist/<int:pk>', ArticleAPIUpdate.as_view()),
    # path('api/v1/articledetail/<int:pk>', ArticleAPIDetailView.as_view()),
]
