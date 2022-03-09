# from rest_framework import routers
#from .views import CourseViewSet, filter_course_subject, filter_course_curriculum, course_teachers, get_curriculum_for_course
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, account_edit_view

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user = True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('', account_edit_view, name='account'),
]