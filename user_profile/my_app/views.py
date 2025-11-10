from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"base.html")

def profile(request): 
    user_data = {
        'name': 'Anushruti Mahato',
        'bio': 'Frontend developer with a passion for open-source projects and coffee.',
        'interests': ['Coding', 'Travelling', 'Photography']
    }
    return render(request, 'profile.html', user_data)