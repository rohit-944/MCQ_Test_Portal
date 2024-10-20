from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from django.views import View
from django.http import HttpResponse
from Student.models import *
from Teacher.models import *

# In views.py (of your MCQ_Test app)
from django.shortcuts import render, get_object_or_404
from .models import Student  # Assuming Student model has email field
from .utils import send_mcq_result_email
 # Import the utility function

def test_submission_view(request, student_id):
    # Fetch the student from the database
    student = get_object_or_404(Student, id=student_id)
    
    # Calculate the student's test score
    score = calculate_student_score(student)  # Implement your score calculation logic here
    
    # Send the test result email
    send_mcq_result_email(student.email, student.name, score)
    
    # Render the result page or redirect as needed
    return render(request, 'test_result.html', {'student': student, 'score': score})
# In views.py
def calculate_student_score(student):
    # Implement logic to calculate score based on student answers
    return 85  # Dummy score, replace with actual logic


# Create your views here.

def home_page(request):
    return render(request,'MCQ_Test/home.html')

def contact_us(request):
    if request.POST:          
        uname=request.POST['uname']
        uemail=request.POST['uemail']
        umobile=request.POST['umobile']
        upass=request.POST['msg']
        obj=Contacts(name=uname,email=uemail,phone_no=umobile,massege=upass)
        obj.save()
        messages.success(request,'Massege send Successfully')

    return render(request,'MCQ_Test/contactus.html')

def admin_web(request):
    if request.POST:
        username=request.POST['username']
        upass=request.POST['upass']
        if (username =="root" and upass=="root12345"):
            return redirect('admindash')
        else:
            messages.warning(request,'Username Or Password not correct ')
    return render(request,'MCQ_Test/adminweb.html')


def admin_dash(request):
    return render(request,'MCQ_Test/admindash.html')

def admin_student(request):
    st=Student.objects.all()
    return render(request,'MCQ_Test/adminstudent.html',{'stu':st})

def admin_delete_student(request,id):
    if request.method=='POST':
        pi=Student.objects.get(pk=id)
        pi.delete()
    st=Student.objects.all()
    return render(request,'MCQ_Test/adminstudent.html',{'stu':st})

def admin_edit_student(request,id):
    stu=Student.objects.get(pk=id)
    if request.method=='POST':
        username=request.POST['username']          
        uname=request.POST['uname']
        uemail=request.POST['uemail']
        umobile=request.POST['umobile']
        upass=request.POST['upass']
        stu.username=username
        stu.name=uname
        stu.email=uemail
        stu.mobile=umobile
        stu.password=upass
        stu.save()
        return redirect('adminstudent')
    return render(request,'MCQ_Test/adminstudentedit.html',{'stu':stu})


def admin_teacher(request):
    te=Teacher.objects.all()
    return render(request,'MCQ_Test/adminteacher.html',{'tech':te})

def admin_edit_teacher(request,id):
    stu=Teacher.objects.get(pk=id)
    if request.method=='POST':
        username=request.POST['username']          
        uname=request.POST['uname']
        uemail=request.POST['uemail']
        umobile=request.POST['umobile']
        upass=request.POST['upass']
        stu.username=username
        stu.name=uname
        stu.email=uemail
        stu.mobile=umobile
        stu.password=upass
        stu.save()
        return redirect('adminteacher')
    return render(request,'MCQ_Test/adminteacheredit.html',{'stu':stu})

def admin_delete_teacher(request,id):
    if request.method=='POST':
        pi=Teacher.objects.get(pk=id)
        pi.delete()
    te=Teacher.objects.all()
    return render(request,'MCQ_Test/adminteacher.html',{'tech':te})

def admin_add_teacher(request):
    se=Subject.objects.all()
    if request.POST:
        username=request.POST['username']          
        uname=request.POST['uname']
        uemail=request.POST['uemail']
        usubject=request.POST['usubject']
        umobile=request.POST['umobile']
        upass=request.POST['upass']
        subject=Subject.objects.get(id=usubject)
        if Teacher.objects.filter(username=username).exists():
            messages.warning(request,'Username is already exists')
        else:    
            Teacher.objects.create(username=username,name=uname,email=uemail,subject=subject,mobile=umobile,password=upass)
            messages.success(request,'New Teacher has been Added Successfully')
        
    return render(request,'MCQ_Test/adminteacheradd.html',{'sub':se})

def admin_subject(request):
    sub=Subject.objects.all()
    return render(request,'MCQ_Test/adminsubject.html',{'sub':sub})

def admin_add_subject(request):
    if request.POST:
        sub=request.POST['subject'] 
        if Subject.objects.filter(subject=sub).exists():
            messages.warning(request,'Subject is already exists')
        else:
            obj=Subject(subject=sub)
            obj.save() 
            messages.success(request,'Subject add successful')

    return render(request,'MCQ_Test/adminsubjectadd.html')

def admin_contact(request):
    con=Contacts.objects.all()
    return render(request,'MCQ_Test/admincontact.html',{'cont':con})

def admin_delete_contact(request,id):
    if request.method=='POST':
        pi=Contacts.objects.get(pk=id)
        pi.delete()
    con=Contacts.objects.all()
    return render(request,'MCQ_Test/admincontact.html',{'cont':con})
