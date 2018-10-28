from django import forms
from django.forms import ModelForm, Select
from .models import Profile,AcademicDetails,Quiz,Personality
from rooms.models import Room

class ProfileForm(forms.ModelForm):
     class Meta:
        model=Profile
        fields=[
            "phone_number",
            "permanent_addr",
        ]

class AcademicForm(forms.ModelForm):
    class Meta:
        model=AcademicDetails
        fields=[
            "grade12",
            "GPA",
        ]

class PersonalityForm(forms.ModelForm):
    class Meta:
        model=Personality
        fields=[
            "hobbies",
            "likes",
            "dislikes",
        ]

OPTIONS= [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    ]


class QuizForm(forms.ModelForm):
    class Meta:
        model=Quiz
        fields=[
            "ans"
        ]
        widgets = {
            'ans': forms.Select(choices=OPTIONS),
        }

     
