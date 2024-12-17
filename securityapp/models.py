from django.db import models

# Create your models here.

class LoginTable(models.Model):
    Username = models.CharField(max_length=30, null=True, blank=True)
    Password = models.CharField(max_length=30, null=True, blank=True)
    TYPE =  models.CharField(max_length=30, null=True, blank=True)

class UserTable(models.Model):
    LOGIN =  models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Firstname =  models.CharField(max_length=30, null=True, blank=True)
    Lastname =   models.CharField(max_length=30, null=True, blank=True)
    Age =  models.IntegerField(null=True, blank=True)
    place =  models.CharField(max_length=30, null=True, blank=True)
    Post =  models.CharField(max_length=30, null=True, blank=True)
    Pin =  models.IntegerField(null=True, blank=True)
    Number =  models.BigIntegerField(null=True, blank=True)
    Email =  models.CharField(max_length=30, null=True, blank=True)

class FeedbackTable(models.Model):   
    USERNAME =  models.ForeignKey(UserTable, on_delete=models.CASCADE)
    Rating =  models.CharField(max_length=30, null=True, blank=True)
    Feedback = models.CharField(max_length=100, null=True, blank=True)
    Date = models.DateTimeField(null=True,blank=True)
    
    
class ComplaintTable(models.Model):
    USER =  models.ForeignKey(UserTable, on_delete=models.CASCADE)
    Complaint = models.CharField(max_length=100, null=True, blank=True)   
    Reply = models.CharField(max_length=100, null=True, blank=True)
    Date = models.DateTimeField(null=True,blank=True)
    
class FriendTable(models.Model):
     USER =  models.ForeignKey(UserTable, on_delete=models.CASCADE)
     FriendName = models.CharField(max_length=30,null=True,blank=True)
     Number = models.BigIntegerField(null=True,blank=True)
     EmergencyNumber = models.BigIntegerField(null=True,blank=True)