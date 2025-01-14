"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from UrbanDjango.task2.views import index, Index2
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', index),
#     path('index/', Index2.as_view())
# ]
"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from UrbanDjango.task2 import views as task2_views
from UrbanDjango.task3 import views as task3_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('class/', task2_views.class_template, name='class_template'),
    path('function/', task2_views.func_template, name='func_template'),
    path('platform/', task3_views.main_page, name='platform'),
    path('games/', task3_views.store_games, name='games'),
    path('cart/', task3_views.cart_page, name='cart')
]