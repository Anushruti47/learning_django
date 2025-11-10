from django.shortcuts import render

# Create your views here.
def todo_list(request):
    tasks=[
        {'id':1,'title':'Buy groceries','completed':True},
        {'id':2,'title':'Clean the home','completed':False},
        {'id':3,'title':'Walk the dog','completed':False},
        {'id':4,'title':'Do laundry','completed':True},
        {'id':5,'title':'Pay bills','completed':False},
    ]
    return render(request,'todo_list_app.html',{'tasks':tasks})