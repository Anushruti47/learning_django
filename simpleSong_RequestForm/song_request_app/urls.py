from django.urls import path
from song_request_app import views

urlpatterns=[
    path("",views.song_request_form_view,name="song_request_form_view"),
]