from django.db import models
from .models import models
from django.contrib.auth.models import User

# Create your models here.

class ExtraField(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15,blank=True, null=True)
    addresses = models.CharField(max_length=100,blank=True,null=True)
    birthdays = models.CharField(max_length=50,blank=True,null=True)
    def __str__(self):
         return self.user.username

class Categories(models.Model):
    title=models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='imgs/')
    class Meta:
        verbose_name_plural='categories'
    def __str__ (self):
        return self.title

class News(models.Model):
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='imgs/')
    detail=models.TextField()
    class Meta: 
        verbose_name_plural='news'
    def __str__(self):
        return self.title
    
class UsersFavoriteCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)
