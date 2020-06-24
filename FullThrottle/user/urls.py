from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('insert/', views.insert, name='insert'),
    path('selectId/', views.selectId, name='selectId'),
    path('viewActivities/', views.viewActivities, name='viewActivities'),

]