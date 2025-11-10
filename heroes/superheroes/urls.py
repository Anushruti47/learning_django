from django.urls import path 
from superheroes import views

urlpatterns=[
    path("",views.superheroes_home,name="superheroes_home"),
    path("spiderman/",views.spiderman_review,name="spiderman_review"),
    path("ironman/",views.ironman_review,name="ironman_review"),
    path("wonderwoman/",views.wonderwoman_review,name="wonderwoman_review"),
]