from django.shortcuts import render


# Create your views here.
def blog_post(request):
    post_data={
        'title':'My First Blog Post',
        'author':'John Doe',
        'content':'This is the content of my first blog post. Welcome to my blog!',
    }
    blog_topic={
        'title':'Technology',
        'description':'The blogs under this topic are related to the latest techological advancements.'
    }
    return render(request,'blog_app.html', {'data':post_data,'topic':blog_topic})