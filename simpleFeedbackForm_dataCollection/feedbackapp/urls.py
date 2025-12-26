from django.urls import path
from feedbackapp import views

urlpatterns=[
    path("",views.submit_feedback_form,name="feedback_form"),
    path("feedback-form/",views.submit_feedback_form,name="submit_feedback_form"),
]