from django.db import models
from loginmodule.models import Reader

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    publish_year = models.IntegerField()

class issueBook(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE,null=True)
    reader_name= models.ForeignKey(Reader, on_delete=models.CASCADE,null=True)