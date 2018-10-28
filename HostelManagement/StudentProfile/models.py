from django.db import models
from django.contrib.auth.models import User
from rooms.models import Room

# Create your models here.
class Profile(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    birth_date = models.DateField(null=True, blank=True)
    roll_no = models.CharField(max_length=10)
    sex = models.CharField(max_length=6)
    branch = models.CharField(max_length=50)
    permanent_addr = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    current_semester = models.PositiveSmallIntegerField()
    doj = models.DateField(null=True,blank=True)
    dog = models.DateField(null=True,blank=True)
    roomID = models.ForeignKey(Room,on_delete=models.SET_NULL,null=True,blank=True)
    roommate = models.ForeignKey("Profile",on_delete=models.SET_NULL,null=True,blank=True)
    image = models.FileField(upload_to='assets/', null=True)
    def __str__(self):
        return self.student.username
    def get_absolute_url(self):
        return "/profile/"

class AcademicDetails(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    grade12 = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    GPA = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    class Meta:
        verbose_name_plural = 'Academic Details'    
    def __str__(self):
        return self.profile.student.username

class Questions(models.Model):
    qno = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=200)
    ans1 = models.CharField(max_length=200, null=True)
    ans2 = models.CharField(max_length=200, null=True)
    ans3 = models.CharField(max_length=200, null=True)
    ans4 = models.CharField(max_length=200, null=True)
    def __str__(self):
        return str(self.qno)

class Quiz(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    qno = models.IntegerField(null=True,blank=True)
    ans = models.IntegerField(default=2)
    class Meta:
        unique_together = (("profile", "qno"),)
    def __str__(self):
        return self.profile.student.username + " Q" +str(self.qno)

    def get_absolute_url(self):
        return "/profile/about/"
    

class Personality(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    hobbies = models.CharField(max_length=200,null=True,blank=True)
    likes = models.CharField(max_length=200,null=True,blank=True)
    dislikes = models.CharField(max_length=200,null=True,blank=True)
    class Meta:
        verbose_name_plural = 'Personality'    
    def __str__(self):
        return self.profile.student.username
