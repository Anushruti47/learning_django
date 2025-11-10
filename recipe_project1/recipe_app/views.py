from django.shortcuts import render

# Create your views here.
def recipe(request):
    recipe1={
        'title':
        'Spaghetti Carbonara',
        'ingredients':
        '''
            200g spaghetti,
            100g panchetta,
            2 large eggs,
            50g pecorino cheese,
            50g parmesan,
            Black pepper,
            Salt
        ''',
        'instructions':
        '''
            1.Cook the spaghetti,
            2.Fry the panchetta until crispy,
            3.Beat the eggs and mix with cheese,
            4.Combine everything and season with pepper
        '''
    }
    return render(request,'recipe_app.html',{'recipe':recipe1})