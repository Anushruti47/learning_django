from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from .models import Student

# Create your views here.
def student_list(request):
    if not Student.objects.exists():
        sample_data=[
            {"name": "Alice", "email": "alice@example.com", "roll_number": "CS101", "course": "CS", "year": 1, "profile_url": "https://example.com/alice"},
            {"name": "Bob", "email": "bob@example.com", "roll_number": "EE202", "course": "EE", "year": 2, "profile_url": "https://example.com/bob"},
            {"name": "Charlie", "email": "charlie[at]example.com", "roll_number": "ME303", "course": "ME", "year": 3, "profile_url": "invalid-url"},
            {"name": "", "email": "duplicate@example.com", "roll_number": "CS101", "course": "CS", "year": 4, "profile_url": ""},
        ]

    messages=[]

    for data in sample_data:
        try:
            student=Student(**data)
            student.full_clean() #Run for validations
            student.save()
            messages.append(f"✅ Added {student.name}")

        except (ValidationError,IntegrityError) as e:
            messages.append(f"❌ Error adding student '{data.get('name','Unnamed')}' : {e} ")

    students=Student.objects.all()

    return render(request,'students.html',{'students':students,'messages':messages})


def home(request):
    return render(request,"home.html")

        