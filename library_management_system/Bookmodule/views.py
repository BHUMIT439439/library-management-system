from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Book

def addBook(request):
    if request.session.get('username') == None:
        messages.info(request,'You are not authorize please login here')
        return render(request,'loginmodule/login.html')
    else:
        if request.method == "POST":
            book_name = request.POST['book_name']
            author_name = request.POST['author_name']
            publish_year = request.POST['publish_year']
            super_pwd = request.POST['superpassword']
            if Book.objects.filter(book_name = book_name).exists() and Book.objects.filter(auther_name = auther_name).exists():
                messages.info(request,'book already exist')
                return render(request,'Bookmodule/addBook.html')
            else:
                if super_pwd == 'xyz':
                    b = Book(book_name = book_name , author_name = author_name , publish_year = publish_year)
                    b.save()
                    book_id = Book.objects.filter(book_name=book_name).first().book_id
                    messages.info(request,f'successfully book added and id is {book_id}')
                    return render(request,'Bookmodule/addBook.html')
                else:
                    messages.info(request,'superuser Password is invalid')
                    return render(request,'Bookmodule/addBook.html')
        else:
             return render(request,'Bookmodule/addBook.html')
                
def issueBook(request):
    if request.session.get('username') == None:
        messages.info(request,'You are not authorize please login here')
        return render(request,'loginmodule/login.html')
    else:
        if request.method == "POST":
            book_id = request.POST['book_id']
            if issueBook.objects.filter(book_name = book_name).exists():
                messages.info(request,'successfully book issued')
                return render(request,'Bookmodule/issueBook.html')
            else:
                messages.info(request,'book does not exists')
                return render(request,'Bookmodule/issueBook.html')
        else:
            return render(request,'Bookmodule/issueBook.html')

def returnBook(request):
    return render(request,'Bookmodule/returnBook.html')

def removeBook(request):
    if request.session.get('username') == None:
        messages.info(request,'You are not authorize please login here')
        return render(request,'loginmodule/login.html')
    else:
        if request.method == "POST":
            book_id = request.POST['book_id']
            super_pwd = request.POST['superpassword']
            if Book.objects.filter(book_id = book_id).exists():
                if super_pwd == 'xyz':
                    messages.info(request,'book is removed')
                    b = Book.objects.filter(book_id=book_id).first()
                    b.delete()
                    return render(request,'Bookmodule/removeBook.html')
                else:
                    messages.info(request,'invalid password')
                    return render(request,'Bookmodule/removeBook.html')
            else:
                messages.info(request,'book not exists')
                return render(request,'Bookmodule/removeBook.html')
        else:
            return render(request,'Bookmodule/removeBook.html')