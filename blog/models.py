from django.db import models


class Articles(models.Model):

    title = models.CharField(max_length=200)


    body = models.TextField()

    date = models.DateTimeField(auto_now_add=True)

    category = models.CharField(max_length=50)




    # Create your models here.
