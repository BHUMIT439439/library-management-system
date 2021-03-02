from django.db import models
from loginmodule.models import Reader

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100)
    auther_name = models.CharField(max_length=100)
    publish_year = models.IntegerField(max_length=4)

class issueBook(models.Model):
    issue_book_id = models.IntegerField()
    issue_book_name = models.CharField(max_length=100)
    reader_name= models.ForeignKey(Reader, on_delete=models.CASCADE)