from django.shortcuts import render, redirect
from .forms import StudentForm

def home(request):
    return render(request,'home.html')
def admissions(request):
    return render(request,'admissions.html') 

def student_details(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'home.html', {'form': form})