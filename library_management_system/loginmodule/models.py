from django.db import models

class Reader(models.Model):
    username = models.CharField(primary_key=True,max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)


