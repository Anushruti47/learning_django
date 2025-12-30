from django.urls import path
from student_app import views

urlpatterns=[
    path("",views.add_student_view,name="add_student_view"),
    path("thank-you/",views.thank_you_view,name="thank_you"),
    path("student-list/",views.student_list_view,name="student_list"),
]