from django.urls import path
from movie import views

urlpatterns=[
    path("movie/<int:movie_id>/<slug:title>",views.movie_detail,name="movie_detail"),
]