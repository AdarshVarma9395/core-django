from django.db import models

class student(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField(upload_to='student_images/', default='default_image.jpg')
    file = models.FileField()


class product(models.Model):
    pass
# Create your models here.
