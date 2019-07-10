from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class product(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField()
    image_url = models.CharField(max_length=1000)
    url = models.CharField(max_length=500)
    likes = models.IntegerField(default=1)
    date = models.DateField()
    hunter = models.ForeignKey(User ,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    

    def pub_date(self):
        return self.date.strftime('%b %e , %Y')

