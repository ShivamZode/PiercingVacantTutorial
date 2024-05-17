from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User #this is not the User model from models.py this contains username, password, email,etc.
from django.contrib.auth import authenticate,logout,login
from django.http import JsonResponse
import json
import html
from home.models import FaceData,Teacher,Presenty
from django.db import models
import math
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import TeacherLoginForm,TeacherRegistrationForm
from datetime import datetime ,timedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def euclidean_distance(descriptor1, descriptor2):
    sum_sq = 0
    for key in descriptor1:
        sum_sq += (descriptor1[key] - descriptor2.get(key, 0)) ** 2
    return math.sqrt(sum_sq)

def compare_face_descriptors(descriptor1, descriptor2):
    # Compute Euclidean distance between the descriptors
    distance = euclidean_distance(descriptor1, descriptor2)
    
    # Define a threshold for similarity
    threshold = 0.6  # Adjust as needed
    
    # Check if the distance is below the threshold
    return distance < threshold
        # The faces are considered dissimilar

# Create your views here.
# request.user.is_anonymous checks if the user is anonymous

def index(request):
  if request.user.is_anonymous:
    return redirect('/log')
  name = request.user.username

  try:
    teacher = Teacher.objects.get(name=name)
    if teacher.subject:
          return redirect ('/teacher_page')
  except Teacher.DoesNotExist: 
      pass
      
      
  return render(request, 'index.html')


def loginUser(request):
 if request.method == "POST":
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, password = password, username = email ) # these password user name are from inbuild User model and the one we defined

    if user is not None:
      login(request,user)
      return redirect('/')
    else:
      return render(request, 'login.html')

 return render(request, 'login.html')

@login_required(login_url='/log')
def logout_user(request):
  logout(request)
  return redirect('/log')

def sign(request):

      return render(request, 'sign.html')
  

def ajax(request):
    
  
    if request.method == 'POST':
        
        face_descriptor = request.POST.get('face_descriptor')
        name = request.POST.get('name')
        
                                  
        face_data = FaceData(
    face_descriptor=face_descriptor,
            name = name,
            
            
        )
      
        face_data.save()
        
      
        return redirect('/')
    else:
        # return JsonResponse({'error': 'Invalid request method'})
        return redirect('/urlGod')



def input(request):
    if request.method == "POST":
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User(username = name, email = email, password=password)
        user.save()
        return redirect('login')

@login_required(login_url='/log')
def urlGod(request):
  return render(request,'toGod.html')


@login_required(login_url='/log')
def php(request):
    name = request.user.username
    try:
        obj = FaceData.objects.get(name=name)
    except FaceData.DoesNotExist:
        messages.info(request, 'Please Set Your Facial Data To Mark Presenty')
        return redirect('/')
        
    return render(request,'scan.html')


def urlLord(request):
  faces = FaceData.objects.all()
  face_data_list = [{'name': face.name, 'descriptor': json.loads(face.face_descriptor)} for face in faces]
  return render(request, 'sus.html', {'face_data_list': json.dumps(face_data_list)})


@login_required(login_url='/log')
def get_number(request):
    subject = ''
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        descriptor = request.POST.get('descriptor')
        print(subject)
    
        try:
            obj = FaceData.objects.get(name=name) # this is the object whose name is equal to the name we sent in the request i.e it is pulling the object with similar name
            number = obj.face_descriptor
            compare = compare_face_descriptors(json.loads(descriptor), json.loads(number))
            print(compare)
            
        except FaceData.DoesNotExist:
            number = None
            compare = None
        return render(request, 'input1.html', {'name': name, 'number': number,'subject': subject , 'compare' : compare }) 
    else:
        return render(request, 'input1.html')




def base(request):
    return render (request,'base.html')



#creates user
def authview(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None) #filled form
        if form.is_valid():
          user = form.save()
          return redirect('/log')
    
    else:
        form = UserCreationForm() #serving form to fill
    
    return render(request, 'signup.html' , {'form':form})

#logins user
def logview(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to a success page or homepage
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def teacher_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to a success page or homepage
            return redirect('/teacher_page')
    else:
        form = AuthenticationForm()
    return render(request, 'teacher_login.html', {'form': form})

def teacher_registration(request):
    pass

def teacherPage(request):
    name = request.user.username
    try:
        obj = Teacher.objects.get(name=name)
    except Teacher.DoesNotExist:
        return redirect('/')
    #so that students do not visit the teacher_page
    # if Teacher.DoesNotExist:
    #     return redirect('/')
    return render(request , 'teacher_page.html')
    
@login_required(login_url='/teacherLog')
def qr_generate(request):
    return render(request, "QR.html")

def send_subject(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        try:
            obj = Teacher.objects.get(name=name) # this is the object whose name is equal to the name we sent in the request i.e it is pulling the object with similar name
            subject = obj.subject
            

        except Teacher.DoesNotExist:
            subject = None
        return render(request, 'QR.html', {'name': name, 'subject': subject})
    else:
        return render(request, 'teacher_page.html')

def presenty(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')

        
        decoded_data = subject.replace("&amp;quot;", '"')

        # Parse the string into a Python dictionary
        try:
            parsed_data = json.loads(decoded_data)
        except json.JSONDecodeError:
            return HttpResponse("It Looks Like you have Scanned a Wrong QR Code")
        # Convert the dictionary into a JSON array
        json_array = json.dumps([parsed_data])
        sub = parsed_data['subject']
        
        dateTime = parsed_data['dateTime']
        print(dateTime +''+ 'this is the subject')
        dateTimeConv = datetime.strptime(dateTime, '%Y-%m-%d %H:%M:%S')
        time_difference = datetime.now() - dateTimeConv
        time_difference_seconds = time_difference.total_seconds()
        print(time_difference_seconds )

        if time_difference_seconds > 30:
            return HttpResponse('OOPS!! QR exprired')
        
        try:
            teacher = Teacher.objects.get(subject=sub)

        except Teacher.DoesNotExist:
            return HttpResponse("It Looks Like you have Scanneed a Wrong QR Code")
            
        
        try:
            presenty = Presenty(name = name, subject = sub,date = datetime.now() )
            presenty.save()
            messages.success(request, "you've been marked present.")
        except:
            return HttpResponse("you've already marked present")
        return redirect('/')

def send_qr(request):
    subject = ''
    if request.method == 'POST':
        subject = request.POST.get('subject')
        
    return render(request, 'input1.html', {'subject': subject})


# def student_list(request):
#     date = datetime.today().date()
#     subject = 'Mathematics'
#     students = User.objects.exclude(username__in=Teacher.objects.values('name'))
#     presenty = Presenty.objects.filter(date=date, subject=subject)

#     presenty_name = set(p.name for p in presenty)  # Using set for faster lookup
#     student_usernames_with_status = []
#     for student in students:
#         if student.username in presenty_name:
#             status = 'P'
#         else:
#             status = 'A'
#         student_usernames_with_status.append({'username': student.username, 'status': status})

#         print(student_usernames_with_status)

#     return render(request, 'data.html', {'student_usernames_with_status': student_usernames_with_status})



def student_list(request):
    if request.method == 'POST':
        # Get subject and date from POST data
        subject = request.POST.get('subject')
        date = request.POST.get('date')
        # Convert date string to datetime object
        date = datetime.strptime(date, '%Y-%m-%d').date()
    else:
        # If no POST data is provided, default to today's date and a default subject
        date = datetime.today().date()
        subject = 'Mathematics'

    students = User.objects.exclude(username__in=Teacher.objects.values('name'))
    presenty = Presenty.objects.filter(date=date, subject=subject)

    presenty_name = set(p.name for p in presenty)  # Using set for faster lookup
    student_usernames_with_status = []
    for student in students:
        if student.username in presenty_name:
            status = 'P'
        else:
            status = 'A'
        student_usernames_with_status.append({'username': student.username, 'status': status})

    return render(request, 'data.html', {'student_usernames_with_status': student_usernames_with_status,'subject':subject,'date':date})
    

def option(request):
    return render(request, 'option.html')
def get(request):
   if request.method == 'POST':
        date = request.POST.get('date')
        subject = request.POST.get('subject')
        
   return HttpResponse (date + 'this is the date' + subject + 'this is the subject')
