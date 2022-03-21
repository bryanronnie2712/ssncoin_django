from django.db import models
from django.contrib.auth.models import User
'''class User(models.Model):
    User=models.OneToOneField(User, null=True, blank=True,on_delete=models.CASCADE)
    name= models.CharField(max_length=200,unique=True)
    password=models.CharField(max_length=20)
    id=models.IntegerField(primary_key=True)
    mail=models.EmailField()
    activation_key = models.CharField(max_length=255, default=1)
    email_validated = models.BooleanField(default=False)
    is_active= models.BooleanField(default=False)
    pubkey=models.CharField(max_length=5000,unique=True)
    privkey=models.CharField(max_length=5000,unique=True)'''
# Create your models here.
class Staff(models.Model):
    choice=(("professor","proffessor"),
    ("assistant_professor","asst_professor"))
    staff= models.OneToOneField(User, on_delete=models.CASCADE)
    staffid=models.IntegerField()
    department=models.CharField(max_length=15)
    category=models.TextField(max_length=200,choices=choice)
    activation_key = models.CharField(max_length=255, default=1)
    email_validated = models.BooleanField(default=False)
    #is_active= models.BooleanField(default=False)
    pubkey=models.CharField(max_length=5000,default=0)
    privkey=models.CharField(max_length=5000,default=0)
class Student(models.Model):
    student= models.OneToOneField(User, on_delete=models.CASCADE)
    department=models.CharField(max_length=20)
    rollno=models.IntegerField()
    #achievements=models.TextField(max_length=200)
    activation_key = models.CharField(max_length=255, default=1)
    email_validated = models.BooleanField(default=False)
    #is_active= models.BooleanField(default=False)
    pubkey=models.CharField(max_length=5000,unique=True,default=0)
    privkey=models.CharField(max_length=5000,unique=True,default=0)
class voting(models.Model):
    voter=models.OneToOneField(User,on_delete=models.CASCADE)
    candidate= models.ForeignKey(Student, on_delete=models.CASCADE)
    achievement=models.TextField(max_length=200)
    is_voted= models.BooleanField(default=False)
    votes=models.IntegerField()

# Create your models here.