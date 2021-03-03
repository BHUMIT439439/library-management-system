from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Book

def addBook(request):
    if request.method == "POST":
        book_name = request.POST['bname']
        auther_name = request.POST['aname']
        publish_year = request.POST['pyear']
        super_pwd = request.POST['superpassword']
        if Book.objects.filter(book_name = book_name).exists() and Book.objects.filter(auther_name = auther_name).exists():
            messages.info(request,'book already exist')
            return render(request,'addBook.html')
        else:
            if super_pwd == 'xyz':
                b = Book(book_name = book_name , auther_name = auther_name , publish_year = publish_year)
                b.save()
                book_id = Book.objects.filter(book_name=book_name).first().book_id
                messages.info(request,f'successfully book added and id is {book_id}')
                return render(request,'addBook.html')
            else:
                messages.info(request,'superuser Password is invalid')
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

def removeBook(request):
    if request.method == "POST":
        book_id = request.POST['book_id']
        super_pwd = request.POST['superpassword']
        if Book.objects.filter(book_id = book_id).exists():
            if super_pwd == 'xyz':
                messages.info(request,'book is removed')
                b = Book.objects.filter(book_id=book_id).first()
                b.delete()
                return render(request,'removeBook.html')
            else:
                messages.info(request,'invalid password')
                return render(request,'removeBook.html')
        else:
            messages.info(request,'book not exists')
            return render(request,'removeBook.html')
    else:
        return render(request,'removeBook.html')