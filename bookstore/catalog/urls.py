from django.urls import path
from catalog import views

urlpatterns=[
    path("",views.home,name="catalog_home"),
    path("author/<str:username>",views.author_page,name="catalog_author"),
    path("book/<int:book_id>",views.book_page,name="catalog_book"),
]