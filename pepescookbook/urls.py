"""pepescookbook URL Configuration



The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'recipes', views.RecipeViewSet, basename='recipe')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
#
# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),
# ]
# path('users/', views.UserList.as_view(), name='user-list'),
# path('users/<int:pk>/', views.UserDetail.as_view()),
# path('recipes/', views.RecipeList.as_view(), name='recipe-list'),
# path('recipes/<int:pk>/', views.RecipeDetail.as_view()),
