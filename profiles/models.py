from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageFile(default='default.jpg',upload_to='profile_pics')
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female'),
        (2, 'Unspecified'),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES)
    desc = models.TextField(max_length=100)

    
#for getting in the admin page of the website 
    def __str__(self):
        return self.user.username 

