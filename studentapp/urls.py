from django.urls import path
# from .views import student_list, student_detail 

from rest_framework.urlpatterns import format_suffix_patterns
from studentapp import views


urlpatterns = [
    # path('student/', student_list),
    # path('studentdetail/<int:pk>/', student_detail),
    path('student/', views.studentList.as_view()),
    path('studentdetail/<int:pk>/', views.studentDetail.as_view()),
   
]

urlpatterns = format_suffix_patterns(urlpatterns)