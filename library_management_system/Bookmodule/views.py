from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Book

def addBook(request):
    if request.method == "POST":
        book_name = request.POST['bname']
        auther_name = request.POST['aname']
        publish_year = request.POST['pyear']
        if Book.objects.filter(book_name = book_name).exists() and Book.objects.filter(auther_name = auther_name).exists():
            messages.info(request,'book already exist')
            return render(request,'addBook.html')
        else:
            b = Book(book_name = book_name , auther_name = auther_name , publish_year = publish_year)
            b.save()
            messages.info(request,'successfully book added')
            return render(request,'addBook.html')
    else:
         return render(request,'addBook.html')
                
def issueBook(request):
    if request.method == "POST":
        # issue_book_id = request.POST['bid']
        issue_book_name = request.POST['bname']
        if issueBook.objects.filter(book_name = book_name).exists():
            messages.info(request,'successfully book issued')
            return render(request,'issueBook.html')
        else:
            messages.info(request,'book does not exists')
            return render(request,'issueBook.html')
    else:
        return render(request,'issueBook.html')

def returnBook(request):
    return render(request,'returnBook.html')


