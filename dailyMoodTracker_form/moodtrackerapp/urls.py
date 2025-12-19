from django.urls import path
from moodtrackerapp import views

app_name="moodtrackerapp"

urlpatterns=[
    path('',views.homepage,name="homepage"),
    path('home/',views.homepage,name="homepage"),
    path('mood-track/',views.track_mood,name="track_mood"),
]