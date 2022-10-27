import djoser
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

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
    path('api/v1/auth/', include('rest_framework.urls')), #Авторизация по сессии
    path('api/v1/articlelist/', ArticleAPIList.as_view()),
    path('api/v1/articlelist/<int:pk>', ArticleAPIUpdate.as_view()),
    path('api/v1/articledelete/<int:pk>', ArticleAPIDestroy.as_view()),
    path('api/v1/auth-djoser/', include('djoser.urls')), #Авторизация по токенам
    re_path(r'^auth/', include('djoser.urls.authtoken')), #Авторизация по токенам
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #Авторизация по JWT-токенам
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #Авторизация по JWT-токенам
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'), #Авторизация по JWT-токенам
]
