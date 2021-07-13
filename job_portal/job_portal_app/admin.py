from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(CandidateRegister)
admin.site.register(EmployerRegister)
admin.site.register(PostJob)
admin.site.register(ContactUs)