from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#=================Custom ==========================

class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=11)
    description=models.TextField()


    def __str__(self):
        return self.email

#==============

class Enrollment(models.Model):
    FullName=models.CharField(max_length=25)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    Email=models.EmailField()
    Gender=models.CharField(max_length=25)
    PhoneNumber=models.CharField(max_length=11)
    DOB=models.CharField(max_length=25)
    SelectMembershipplan=models.CharField(max_length=200)
    SelectTrainer=models.CharField(max_length=55)
    Reference=models.CharField(max_length=55)
    Address=models.TextField()
    PaymetStatus=models.CharField(max_length=55,blank=True,null=True)
    Price=models.IntegerField(blank=True,null=True)
    DueDate=models.DateField(blank=True,null=True)
    TimeStamp=models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.FullName

#=======================

class Trainer(models.Model):
    Name=models.CharField(max_length=55)
    Gender=models.CharField(max_length=25)
    Phone=models.CharField(max_length=25)
    Salary=models.IntegerField()
    TimeStamp=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    def __str__(self):
        return self.Name

#============================

class MembershipPlan(models.Model):
    Plan=models.CharField(max_length=185)
    Price=models.IntegerField()

    def __int__(self):
        return self.id
    

class Gallery(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to='gallery')
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __int__(self):
        return self.id


class Attendance(models.Model):
    Selectdate=models.DateTimeField(auto_now_add=True)
    Login=models.CharField(max_length=200)
    Logout=models.CharField(max_length=200)
    Selectworkout=models.CharField(max_length=200)
    Trained_By=models.CharField(max_length=200)

    def __int__(self):
        return self.id