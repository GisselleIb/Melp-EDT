from django.urls import path, register_converter
from . import views,converts

register_converter(converts.FloatUrlParameterConverter,'float')

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_restaurant, name='add_restaurant'),
    path('view/', views.view_restaurant, name='view_restaurant'),
    path('update/<str:pk>/',views.update_restaurant, name='update_restaurant'),
    path('delete/<str:pk>',views.delete_restaurant,name='delete_restaurant'),
    path('restaurants/statistics',views.statistics_restaurant,name='statistics_restaurant')
]
