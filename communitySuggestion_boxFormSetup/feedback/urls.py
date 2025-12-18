from django.urls import path
from feedback import views

app_name='feedback'

urlpatterns=[
    path('',views.homepage,name="homepage"),
    path('home/',views.homepage,name="homepage"),
    path('suggest/',views.suggestion_form_view,name="suggestion_form_view"),
]