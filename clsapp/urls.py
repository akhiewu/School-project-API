from django.urls import path
# from .views import cls_list, cls_detail 
from rest_framework.urlpatterns import format_suffix_patterns
from clsapp import views

urlpatterns = [
    # path('cls/', cls_list),
    # path('clsdetail/<int:pk>/',cls_detail),
     path('cls/', views.clsList.as_view()),
    path('clsdetail/<int:pk>/', views.clsDetail.as_view()),
    
  
   
]

urlpatterns = format_suffix_patterns(urlpatterns)