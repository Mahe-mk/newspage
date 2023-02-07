from django.db import models
from .models import models

# Create your models here.


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
