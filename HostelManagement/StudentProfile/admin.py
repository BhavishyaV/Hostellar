from django.contrib import admin
from .models import Profile, AcademicDetails, Questions, Quiz, Personality
# Register your models here.

admin.site.register(Profile)
admin.site.register(AcademicDetails)
admin.site.register(Personality)
admin.site.register(Questions)
admin.site.register(Quiz)