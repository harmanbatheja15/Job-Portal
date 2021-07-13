"""job_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from job_portal_app.views import *

urlpatterns = [
    path('', home, name="home"),
    path('candidateRegister', candidateRegister, name='candidateRegister'),
    path('candidateLogin', candidateLogin, name='candidateLogin'),
    path('employerRegister', employerRegister, name='employerRegister'),
    path('employerLogin', employerLogin, name='employerLogin'),
    path('adminLogin', adminLogin, name='adminLogin'),
    path('candidateHome', candidateHome, name='candidateHome'),
    path('employerHome', employerHome, name='employerHome'),
    path('adminHome', adminHome, name='adminHome'),
    path('contact', contact, name="contact"),
    path('allEmployers', allEmployers, name="allEmployers"),
    path('allCandidates', allCandidates, name="allCandidates"),
    path('pendingEmployers', pendingEmployers, name="pendingEmployers"),
    path('acceptedEmployers', acceptedEmployers, name="acceptedEmployers"),
    path('rejectedEmployers', rejectedEmployers, name="rejectedEmployers"),
    path('JobPost', JobPost, name="JobPost"),
    path('allJobs', allJobs, name="allJobs"),
    path('findJobs', findJobs, name="findJobs"),
    path('editJobPost/<int:pid>', editJobPost, name='editJobPost'),
    path('jobDetails/<int:pid>', jobDetails, name='jobDetails'),
    path('deleteCandidate/<int:pid>', deleteCandidate, name='deleteCandidate'),
    path('deleteEmployer/<int:pid>', deleteEmployer, name='deleteEmployer'),
    path('deleteJobPost/<int:pid>', deleteJobPost, name='deleteJobPost'),
    path('change_status/<int:pid>', change_status, name='change_status'),
    path('Logout', Logout, name="Logout"),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)