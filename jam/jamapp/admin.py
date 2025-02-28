from django.contrib import admin
from . models import Login,JobSeeker,Employer,Enquiry,Jobs

# Register your models here.
admin.site.register(Login)
admin.site.register(JobSeeker)
admin.site.register(Employer)
admin.site.register(Enquiry)
admin.site.register(Jobs)