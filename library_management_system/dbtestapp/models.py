from django.db import models
class Member(models.Model):
    member_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    address = models.TextField()
    password = models.CharField(max_length=20)

