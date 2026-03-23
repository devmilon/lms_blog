from django.urls import path
from .views import home, course_list, course_detail ,create_course

urlpatterns = [

    path('', home, name='home'),

    path('courses/', course_list, name='course_list'),

    path('create-course/', create_course, name='create_course'),

    path('courses/<int:id>/', course_detail, name='course_detail'),

]