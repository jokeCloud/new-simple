from django.urls import path

from .views import blog, index, sobre

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('sobre/', sobre, name='sobre'),
]
