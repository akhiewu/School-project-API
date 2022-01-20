from django.urls import path
# from .views import teacher_list, teacher_detail 
from rest_framework.urlpatterns import format_suffix_patterns
from teacherapp import views


urlpatterns = [
    # path('teacher/', teacher_list),
    # path('teacherdetail/<int:pk>/',teacher_detail),
    
    path('teacher/', views.teacherList.as_view()),
    path('teacherdetail/<int:pk>/', views.teacherDetail.as_view()),
   
]

urlpatterns = format_suffix_patterns(urlpatterns)