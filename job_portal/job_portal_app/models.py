from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CandidateRegister(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.user.first_name

class EmployerRegister(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class PostJob(models.Model):
    employer = models.ForeignKey(EmployerRegister, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    company_website = models.CharField(max_length=100)
    salary = models.FloatField(max_length=100)
    description = models.TextField()
    experience = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    creationdate = models.DateField()

class ContactUs(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
