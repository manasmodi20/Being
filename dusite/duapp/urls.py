from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('duapp/',views.admissions,name = 'admissions'),
    path('studentapp/', views.student_details,name = 'student_details'),
    
]