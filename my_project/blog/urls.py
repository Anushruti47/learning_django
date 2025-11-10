from django.urls import path
from blog import views

urlpatterns=[
    path('',views.home,name="home"),
    # path('home/',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('blog1/',views.blog1,name="blog1"),
    path('blog2/',views.blog2,name="blog2"),
    path('blog3/',views.blog3,name="blog3"),
    path('blog4/',views.blog4,name="blog4"),
]