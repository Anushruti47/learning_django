from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_view, name='home'),
    path('feedback/', views.feedback_form_view, name='feedback_form'),
]
