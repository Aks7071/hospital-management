from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from hospital.models import Department, Doctor,ChatMessage
from hospital.forms import MeetingRequestForm,ChatMessageForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def departments(request):
    departments = Department.objects.all()  # Fetch all departments
    return render(request, 'departments.html', {'departments': departments})

#def contact(request):
    #return render(request,'contact.html')

def patientservice(request):
    return render(request,'patientservice.html')

def department_detail(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    doctors = department.doctors.all()  # Get all doctors for this department
    form = MeetingRequestForm()

    if request.method == 'POST':
        form = MeetingRequestForm(request.POST)
        if form.is_valid():
            form.save()  # Save the meeting request
            return redirect('success')  # Redirect to a success page after saving

    return render(request, 'department_detail.html', {
        'department': department,
        'doctors': doctors,
        'form': form,
    })  

# views.py in your 'hospital' app
def contact_view(request):
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            form.save()  # Save chat message to the database
    else:
        form = ChatMessageForm()

    # Fetch all chat messages from the database
    chat_messages = ChatMessage.objects.all().order_by('-timestamp')

    return render(request, 'contact.html', {'form': form, 'chat_messages': chat_messages})
