from django.urls import path
from workshop_app import views

urlpatterns=[
    path("",views.create_workshop_view,name="create_workshop_view"),
    path("success/",views.success_message_view,name="success_message"),
]