# from rest_framework import routers
#from .views import CourseViewSet, filter_course_subject, filter_course_curriculum, course_teachers, get_curriculum_for_course
from .views import bidding_create_view, biddings_view, bidding_edit_view, bidding_view
from django.urls import path

urlpatterns = [
    path('all', biddings_view, name="biddings"),
    path('create', bidding_create_view, name="biddings_create"),
    path('<int:bidding_id>/edit',
         bidding_edit_view, name="bidding_edit"),
    path('view/<int:bidding_id>', bidding_view, name="bidding_view"),
    
]
