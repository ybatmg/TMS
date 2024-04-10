from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

    
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField('date of birth',null = True,blank= True)
    phone_number = models.IntegerField(null=True)
    avatar = models.ImageField("avatar",upload_to='avatars/', null=True,blank=True)

    # Address
    address_line_1 = models.CharField("address line 1", max_length=255, blank=True)
    address_line_2 = models.CharField("address line 2", max_length=255, blank=True)
    city = models.CharField("city", max_length=50, blank=True)
    state_province_region = models.CharField("state/province/region", max_length=100, blank=True)
    postal_zip_code = models.CharField("postal/zip code", max_length=12, blank=True)
    country = models.CharField("country", max_length=50, blank=True)
    
    # Professional
    company_name = models.CharField("company name", max_length=100, blank=True)
    position = models.CharField("position", max_length=100, blank=True)
    
    # Social
    website_url = models.URLField("website URL", max_length=200, blank=True)
    twitter_handle = models.URLField("Twitter handle", max_length=15, blank=True)
    facebook_profile = models.URLField("Facebook profile URL", max_length=200, blank=True)
    linkedin_profile = models.URLField("LinkedIn profile URL", max_length=200, blank=True)
    instagram_handle = models.CharField("Instagram handle", max_length=30, blank=True)
    
    # Preferences and settings
    preferences = models.JSONField("preferences", default=dict, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name'] 
    
    def __str__(self):
        return self.username
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Work(models.Model):
    title = models.CharField(max_length=50,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title