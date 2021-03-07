from django.db import models
from loginmodule.models import Reader
import datetime

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    publish_year = models.IntegerField()
    is_book_available = models.BooleanField(default=True)

class IssueBook(models.Model):
    issue_id = models.ForeignKey(Book, on_delete=models.CASCADE,null=True)
    reader_name= models.ForeignKey(Reader, on_delete=models.CASCADE,null=True)
    date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
    	return f"[{self.reader_name} => {self.issue_id.book_name}]"