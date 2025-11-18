from django.shortcuts import render
from .models import BlogPost
from datetime import date

# Create your views here.
def home(request):
    return render(request,"home.html")

def blog_list(request):
    if not BlogPost.objects.exists():
        BlogPost.objects.create(title="Django Tips", content="Useful tips on Django.", expiration_date=date(2023, 5, 10))
        BlogPost.objects.create(title="Learning Python", content="Python basics for beginners.", expiration_date=date(2025, 12, 31))
        BlogPost.objects.create(title="Web Security", content="Secure your Django app.", expiration_date=date(2023, 8, 15))
        BlogPost.objects.create(title="New Features", content="Latest Django updates.", expiration_date=date(2026, 1, 1))

    posts=BlogPost.objects.all()

    return render(request,"posts.html",{'posts':posts})

def delete_expired_posts(request):
    BlogPost.objects.filter(expiration_date__lt=date.today()).delete()

    posts=BlogPost.objects.all()

    return render(request,"posts.html",{'posts':posts})
