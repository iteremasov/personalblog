from django.db import models


class Articles(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    body = models.CharField(max_length=5000)

    date = models.DateTimeField()

    category = models.CharField(max_length=50)




    # Create your models here.
