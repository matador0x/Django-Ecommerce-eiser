from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=15, null=True)
    image       = models.ImageField(upload_to="UserProfilePic/",null=True)
    city        = models.ForeignKey('UserCity', related_name='user_city', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.user)

class UserCity(models.Model):
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.name)

##### Create User Profile By Singnals ######

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)