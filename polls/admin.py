from django.contrib import admin
from. import models
from.models import Student,Staff,voting
#from django.contrib.auth.models import User

admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(voting)
# Register your models here.
