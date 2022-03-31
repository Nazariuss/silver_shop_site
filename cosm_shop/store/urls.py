from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.store, name='store'),
    path('order/', views.order, name='order'),
    path('login/', LoginUser.as_view(), name='login'),
    path('post/<id_product>', views.post, name='post'),
    path('update_item/', views.update_item, name='update_item'),
    path('register/', views.register, name='register'),
    path('process_order/', views.processOrder, name='process_order'),
    path('categories/', views.show_category, name='category'),
]