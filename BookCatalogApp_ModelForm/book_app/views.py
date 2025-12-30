from django.shortcuts import render,redirect
from .forms import BookForm
from .models import Book
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def add_book_view(request):
    if request.method =="POST":
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thank_you")
    else:
        form=BookForm()

    return render(request,"add_book.html",{'form':form})

def thank_you_view(request):
    return render(request,"thank_you.html")

def book_list_view(request):
    books=Book.objects.all()
    return render(request,"book_list.html",{'books':books})