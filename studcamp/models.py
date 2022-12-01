from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20) 
    email = models.EmailField()  
    phone = models.CharField(max_length=100)  
    desc = models.CharField(max_length=15)
    def _str_(self):
        return self.name

class Signup(models.Model):
    name = models.CharField(max_length=20) 
    email = models.EmailField()  
    phone = models.CharField(max_length=100)  
    qualification = models.CharField(max_length=15)
    course = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    cpassword = models.CharField(max_length=15) 
    
    def _str_(self):
        return self.name

class Course(models.Model):
    cid = models.IntegerField()
    cname = models.CharField(max_length=250) 
    duration = models.CharField(max_length=250)
    fee = models.IntegerField()
    def _str_(self):
        return self.name

class Staff(models.Model):
    sid = models.CharField(max_length=250)
    sname = models.CharField(max_length=20) 
    email = models.EmailField()  
    phone = models.CharField(max_length=100) 
    address = models.CharField(max_length=550) 
    qualification = models.CharField(max_length=15)
    subject = models.CharField(max_length=15)
    salary = models.CharField(max_length=15)
     
    
    def _str_(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=20) 
    email = models.EmailField()  
    desc = models.CharField(max_length=15)
    def _str_(self):
        return self.name

class Session(models.Model):
    session = models.CharField(max_length=20) 
    shr = models.CharField(max_length=20) 
    msg = models.CharField(max_length=600)
    def _str_(self):
        return self.name





