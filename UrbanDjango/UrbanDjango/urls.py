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
# from django.contrib import admin
# from django.urls import path
# from task2 import views as task2_views
# from task4 import views as task4_views

#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('/ /', task4_views.main_page, name='menu'),
#     path('class/', TemplateView.as_view(template_name='class_template.html')),
#     path('function/', task2_views.func_template, name='func_template'),
#     path('platform/', task4_views.main_page, name='platform'),
#     path('games/', task4_views.store_games, name='games'),
#     path('cart/', task4_views.cart_page, name='cart')
# ]
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path
from task2.views import func_template
from task4.views import platform, games, cart
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('func', func_template),
    # path('class/', TemplateView.as_view(template_name='class_template.html')),
    # path('class/', ClassTemplate.as_view()),
    # path('main', task4.views.main_page),
    # path('games/', task4.views.store_games),
    # path('cart/', task4.views.cart_page),
    # path('platform/', platform),
    # path('platform/games/', games),
    # path('platform/cart/', cart),
    path('admin/', admin.site.urls),
    path('registration/', include('task5.urls')),
    path('', include('task5.urls')),
]
