from django.shortcuts import render
from datetime import datetime
# Create your views here.

def blog_post(request):
    post = {
        'title': 'my first blog post',
        'content': 'This is the content of my very first blog post. It is not very long.',
        'author': 'john doe',
        'pub_date': datetime.now(),
    }
    return render(request, 'blog_app.html', {'post': post})