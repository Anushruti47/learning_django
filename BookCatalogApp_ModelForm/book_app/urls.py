from django.urls import path
from book_app import views

urlpatterns=[
    path("",views.add_book_view,name="add_book_view"),
    path("thank-view/",views.thank_you_view,name="thank_you"),
    path("book-list/",views.book_list_view,name="book_list_view"),
]