from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
from django.conf import settings
from datetime import date, datetime
from .models import *
from django.contrib.auth.models import User

# Create your views here.

def home(request):

    job = PostJob.objects.all()
    city_search = PostJob.objects.values_list('location', flat=True)
    city = request.GET.get('city')
    jobSearch = PostJob.objects.filter(location=city)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            jobSearch = jobSearch.filter(location=city)

    context = {
        'job': job,
        'jobSearch': jobSearch,
        'city_search': city_search,
    }

    return render(request, 'home.html', context)

# Job Details
def jobDetails(request, pid):

    job = PostJob.objects.get(id=pid)

    context = {
        'job': job,
    }

    return render(request, 'jobDetails.html', context)

# Candidate Register
def candidateRegister(request):
    
    error = ""

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        location = request.POST['location']

        try:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=email, password=password)
            CandidateRegister.objects.create(user=user, phone=phone, location=location, type="candidate")
            error="no"

        except:
            error="yes"

    context = {
        'error': error
    }

    return render(request, 'candidateRegister.html', context)

# Employer Register
def employerRegister(request):

    error = ""

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=email, password=password)
            EmployerRegister.objects.create(user=user, phone=phone, type="employer", status="pending")
            error="no"

        except:
            error="yes"

    context = {
        'error': error
    }

    return render(request, 'employerRegister.html', context)

# Candidate Login
def candidateLogin(request):

    error = ""

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)

        if user:
            try:
                user1 = CandidateRegister.objects.get(user=user)
                if user1.type == "candidate":
                    login(request, user)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"

        else:
            error = "yes"

    context = {
        'error': error
    }
    
    return render(request, 'candidateLogin.html', context)

# Employer Login
def employerLogin(request):

    error = ""

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)

        if user:
            try:
                user1 = EmployerRegister.objects.get(user=user)
                if user1.type == "employer" and user1.status != "pending":
                    login(request, user)
                    error = "no"
                else:
                    error = "not"
            except:
                error = "yes"

        else:
            error = "yes"

    context = {
        'error': error
    }

    return render(request, 'employerLogin.html', context)

# Contact
def contact(request):
    if(request.method == "POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = ContactUs(name=name, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()
        # messages.success(request, f'Thanks {name} for your feedback!')
        return redirect('contact')

    return render(request, 'contact.html')

# Admin Login
def adminLogin(request):

    error = ""

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"

    context = {
        'error': error
    }

    return render(request, 'adminLogin.html', context)

# Admin Home Page
def adminHome(request):

    if not request.user.is_authenticated:
        return redirect('adminRegister')

    candidate = CandidateRegister.objects.all().count()
    employer = EmployerRegister.objects.all().count()
    job = PostJob.objects.all().count()

    context  = {
        'candidate': candidate,
        'employer': employer,
        'job': job,
    }

    return render(request, 'adminHome.html', context)

# Candidate Home Page
def candidateHome(request):

    if not request.user.is_authenticated:
        return redirect('candidateRegister')

    user = request.user
    candidate = CandidateRegister.objects.get(user=user)

    error = ""

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        location = request.POST['location']

        candidate.user.first_name = first_name
        candidate.user.last_name = last_name
        candidate.phone = phone
        candidate.location = location

        try:
            candidate.save()
            candidate.user.save()
            error="no"

        except:
            error="yes"

    context = {
        'candidate': candidate,
        'error': error,
    }

    return render(request, 'candidateHome.html', context)

# Employer Home Page
def employerHome(request):

    if not request.user.is_authenticated:
        return redirect('employerRegister')

    user = request.user
    employer = EmployerRegister.objects.get(user=user)

    error = ""

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']

        employer.user.first_name = first_name
        employer.user.last_name = last_name
        employer.phone = phone

        try:
            employer.save()
            employer.user.save()
            error="no"

        except:
            error="yes"

    context = {
        'employer': employer,
        'error': error,
    }

    return render(request, 'employerHome.html', context)

# Pending Employers
def pendingEmployers(request):
    
    if not request.user.is_authenticated:
        return redirect('adminLogin')

    data = EmployerRegister.objects.filter(status="pending")

    context = {
        'data': data
    }

    return render(request, 'pendingEmployers.html', context)

# Accepted Employers
def acceptedEmployers(request):
    
    if not request.user.is_authenticated:
        return redirect('adminLogin')

    data = EmployerRegister.objects.filter(status="Accept")

    context = {
        'data': data
    }

    return render(request, 'acceptedEmployers.html', context)

# Rejected Employers
def rejectedEmployers(request):
    
    if not request.user.is_authenticated:
        return redirect('adminLogin')

    data = EmployerRegister.objects.filter(status="Reject")

    context = {
        'data': data
    }

    return render(request, 'rejectedEmployers.html', context)

# All Employers
def allEmployers(request):

    if not request.user.is_authenticated:
        return redirect('adminLogin')

    data = EmployerRegister.objects.all()

    context = {
        'data': data
    }

    return render(request, 'allEmployers.html', context)

# All Candidates
def allCandidates(request):
    
    if not request.user.is_authenticated:
        return redirect('adminLogin')

    data = CandidateRegister.objects.all()

    context = {
        'data': data
    }

    return render(request, 'allCandidates.html', context)

# Delete Candidate
def deleteCandidate(request, pid):

    if not request.user.is_authenticated:
        return redirect('adminLogin')

    candidate = User.objects.get(id=pid)
    candidate.delete()
    return redirect('allCandidates')

# Delete Employer
def deleteEmployer(request, pid):

    if not request.user.is_authenticated:
        return redirect('adminLogin')

    employer = User.objects.get(id=pid)
    employer.delete()
    return redirect('allEmployers')

# Delete Job Post
def deleteJobPost(request, pid):

    if not request.user.is_authenticated:
        return redirect('adminLogin')

    job = PostJob.objects.get(id=pid)
    job.delete()
    return redirect('allJobs')

# Change Status
def change_status(request, pid):

    if not request.user.is_authenticated:
        return redirect('adminLogin')
    
    error = ""

    employer = EmployerRegister.objects.get(id=pid)

    if request.method == "POST":
        s = request.POST['status']
        employer.status = s

        try:
            employer.save()
            error = "no"
        except:
            error = "yes"

    context = {
        'employer': employer,
        'error': error
    }

    return render(request, 'change_status.html', context)

# Post a Job
def JobPost(request):

    if not request.user.is_authenticated:
        return redirect('employerLogin')

    error = ""

    if request.method == "POST":
        jobtitle = request.POST['jobtitle']
        companyname = request.POST['companyname']
        companywebsite = request.POST['companywebsite']
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        salary = request.POST['salary']
        experience = request.POST['experience']
        location = request.POST['location']
        skills = request.POST['skills']
        description = request.POST['description']
        user = request.user

        employer = EmployerRegister.objects.get(user=user)

        try:
            PostJob.objects.create(employer=employer, start_date=startdate, end_date=enddate, title=jobtitle, company_name=companyname, company_website=companywebsite, salary=salary, description=description, experience=experience, location=location, skills=skills, creationdate=date.today())
            error="no"

        except:
            error="yes"

    context = {
        'error': error
    }

    return render(request, 'JobPost.html', context)

def allJobs(request):

    if not request.user.is_authenticated:
        return redirect('employerLogin')

    user = request.user
    employer = EmployerRegister.objects.get(user=user)
    job = PostJob.objects.filter(employer=employer)

    context = {
        'job': job
    }

    return render(request, 'allJobs.html', context)

def editJobPost(request, pid):

    if not request.user.is_authenticated:
        return redirect('employerLogin')

    error = ""

    job = PostJob.objects.get(id=pid)

    if request.method == "POST":
        jobtitle = request.POST['jobtitle']
        companyname = request.POST['companyname']
        companywebsite = request.POST['companywebsite']
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        salary = request.POST['salary']
        experience = request.POST['experience']
        location = request.POST['location']
        skills = request.POST['skills']
        description = request.POST['description']

        job.title = jobtitle
        job.company_name = companyname
        job.company_website = companywebsite
        job.salary = salary
        job.experience = experience
        job.location = location
        job.skills = skills
        job.description = description

        try:
            job.save()
            error="no"

        except:
            error="yes"

        if startdate:
            try:
                job.start_date = startdate
                job.save()
            except:
                pass
        else:
            pass

        if enddate:
            try:
                job.end_date = enddate
                job.save()
            except:
                pass
        else:
            pass

    context = {
        'error': error,
        'job': job
    }

    return render(request, 'editJobPost.html', context)

def findJobs(request):

    if not request.user.is_authenticated:
        return redirect('employerLogin')

    job = PostJob.objects.all()

    context = {
        'job': job
    }

    return render(request, 'findJobs.html', context)

# Logout
def Logout(request):
    logout(request)
    return redirect("home")