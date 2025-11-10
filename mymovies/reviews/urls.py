from django.urls import path
from reviews import views

urlpatterns=[
    path('',views.index,name="index"),
    path('inception/',views.inception_review,name="inception_review"),
    path('interstellar/',views.interstellar_review,name="interstellar_review"),
    path('thedarkknight/',views.the_dark_knight_review,name="the_dark_knight_review"),
]