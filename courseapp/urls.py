from django.urls import path
#from .views import course_list, course_detail 
from rest_framework.urlpatterns import format_suffix_patterns
from courseapp import views

urlpatterns = [
    # path('course/', course_list),
    # path('coursedetail/<int:pk>/', course_detail),
    path('course/', views.courseList.as_view()),
    path('coursedetail/<int:pk>/', views.courseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)