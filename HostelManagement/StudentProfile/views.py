from django.shortcuts import render,redirect, get_object_or_404, Http404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import Profile,AcademicDetails, Questions, Quiz, Personality
from rooms.models import Room
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .forms import ProfileForm, QuizForm, PersonalityForm, AcademicForm
from django.db.models import Q
import math
import itertools


# Create your views here.
def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user 
            user = form.get_user()
            login(request,user)
            return HttpResponseRedirect('/profile/')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def display_profile(request):
    student=Profile.objects.get(student=request.user)
    academics, created =AcademicDetails.objects.get_or_create(profile=student)
    if created:
        academics.profile=student
        academics.save()
    try:
        hostel =Room.objects.get(id=student.roomID_id)
    except:
        hostel = Room.objects.get(block="None")
    try:
        roommate = Profile.objects.get(id=student.roommate_id)
    except: 
        temp = User.objects.get(username="Dummy")
        roommate = Profile.objects.get(student=temp)
    for i in range(1,6):
        quiz, created= Quiz.objects.get_or_create(profile=student,qno=i)
        if created:
            quiz.profile=student
            quiz.qno=i
            quiz.ans=2

    context= {
        'student':student,
        'academics':academics,
        'hostel':hostel,
        'roommate': roommate,
    }
    return render(request,'accounts/profile.html',context)

def logout_view(request):
    logout(request)
    return redirect('/')

def update(request):
    instance = get_object_or_404(Profile, student=request.user)
    instance2=get_object_or_404(AcademicDetails,profile=instance)
    form=ProfileForm(request.POST or None, instance=instance)
    form2 =AcademicForm(request.POST or None,instance=instance2)
    if form.is_valid() and form2.is_valid():
        instance=form.save(commit=False)
        instance.save()
        instance2=form2.save(commit=False)
        instance2.save()
        return HttpResponseRedirect('..')
    context = {
		"form":form,
        "form2":form2,
	}
    return render(request, 'accounts/update.html', context)

def about(request,id):
    student= get_object_or_404(Profile,student=request.user)
    question = Questions.objects.get(qno=id)
    form=QuizForm(request.POST or None)
    if form.is_valid():
        quiz, created =Quiz.objects.get_or_create(profile=student,qno=id)
        if quiz: 
            quiz.ans=form.cleaned_data['ans']
            quiz.save()
        if created: 
            quiz.profile=student
            quiz.qno=question.qno
            quiz.ans=form.cleaned_data['ans']
            quiz.save()
        if (question.qno==5):
            return HttpResponseRedirect('..')
        return HttpResponseRedirect(quiz.get_absolute_url() + str(question.qno+1))
    context={
        'q': question,
        'form':form,
    }
    return render(request, 'accounts/about.html',context)



def hobbies_interests(request):
    student = Profile.objects.get(student=request.user)
    form = PersonalityForm(request.POST or None)
    if(form.is_valid()):
        personality, created = Personality.objects.get_or_create(profile=student)
        if created:
            personality.profile=student
        personality.hobbies = form.cleaned_data['hobbies']
        personality.likes = form.cleaned_data['likes']
        personality.dislikes = form.cleaned_data['dislikes']
        personality.save()
        return HttpResponseRedirect('/profile')
    context= {
        'form':form
    }
    return render(request,"accounts/about_form.html",context)

def roommate(request):
    return render(request, 'accounts/roommate.html')

def choose_roommate(request):
    query = request.GET.get("q")
    if query:
        students = User.objects.filter(first_name__icontains = query)
        context={
            'students':students
        }
    else:
        context={}
    return render(request,'accounts/choose.html',context)    

def select(request,stud):
    selected_user = User.objects.get(username=stud)
    student = Profile.objects.get(student=selected_user)
    try:
        personality = Personality.objects.get(profile=student)
    except:
        temp = User.objects.get(username="Dummy")
        temp1 =Profile.objects.get(student=temp)
        personality = Personality.objects.get(profile=temp1)
    try:
        hostel =Room.objects.get(id=student.roomID_id)
    except:
        hostel = Room.objects.get(block="None")
    if (request.method=='POST' and hostel.block=="None"):
        active_user = Profile.objects.get(student=request.user)
        room = Room.objects.get(profile=active_user)
        active_user.roommate=student
        active_user.save()
        student.roommate = active_user
        student.roomID = room
        student.save()
        return HttpResponseRedirect('/profile')
    context={
        'selected_user':selected_user,
        'student':student,
        'personality':personality,
        'hostel':hostel
    }
    return render(request,'accounts/display_details.html',context)

def custom_roommate(request):
    active_user = Profile.objects.get(student=request.user)
    students = Profile.objects.filter(~Q(student=request.user))
    students = students.filter(~Q(id=3))
    students= list(students.values_list('id',flat=True))
    for i in range(1,6):
        results=[]
        quiz1 = Quiz.objects.get(profile=active_user,qno=i)
        for s in students:
            s_profile = Profile.objects.get(id=s)
            quiz2 = Quiz.objects.filter(profile=s_profile,qno=i)
            quiz2 = list(quiz2.values_list('ans',flat=True))
            diff = int(abs(quiz1.ans-quiz2[0]))
            similarity_score=float(pow(2,-diff))
            results.append((s,similarity_score))
        results.sort(key=(lambda x:x[1]), reverse=True)
        if len(results)<=5:
            students=[x[0] for x in results[:len(results)]]
        else:
            students=[x[0] for x in results[:len(results)//2]]
    
    if(len(students)>=5):
        students =students[:5]
    
    candidates = Profile.objects.filter(id__in = students[:5])
    
    context ={
        'students':candidates
    }        
    return render(request,'accounts/custom.html',context)


def reset(request):
    student=Profile.objects.get(student=request.user)
    blank = Room.objects.get(block="None")
    academics, created =AcademicDetails.objects.get_or_create(profile=student)
    if created:
        academics.profile=student
        academics.save()
    hostel =Room.objects.get(id=student.roomID_id)
    hostel.availability=1
    hostel.save()
    student.roomID = blank
    temp = User.objects.get(username="Dummy")
    val = Profile.objects.get(student=temp)
    try:
        rm = Profile.objects.get(id=student.roommate_id)
        student.roommate = val
        rm.roommate = val
        rm.roomID=blank
        rm.save()
        student.save()
    except:
        student.roommate=val
        student.save()
    context = {
        'student':student,
        'academics':academics,
        'hostel':blank,
        'roommate': val,
    }
    return render(request,'accounts/profile.html',context)

            