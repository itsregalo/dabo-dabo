from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# imagekit
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


User = settings.AUTH_USER_MODEL
# Create your models here.



class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    phone_no = models.CharField(max_length=13, blank=True, null=True)
    ver_code = models.CharField(blank=True, null=True, max_length=10)
    profile_picture = models.ImageField(upload_to='images/doctors_profile/%Y/%m', 
                                        default='images/default-avatar.jpg',
                                        blank=True, null=True)
    profile_picture_thumbnail = ImageSpecField(source='profile_picture',
                                            processors=[ResizeToFill(100, 100)],
                                            format='JPEG',
                                            options={'quality': 60}
                                                )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    class Meta:
        verbose_name_plural = 'Users'
        db_table = 'users'
        

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

