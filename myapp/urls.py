# new file which set about URL

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('foo', views.foo, name = 'foo'),
]