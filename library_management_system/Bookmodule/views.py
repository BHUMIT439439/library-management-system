from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Book, IssueBook
from loginmodule.models import Reader

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
            if Book.objects.filter(book_name = book_name).exists() and Book.objects.filter(author_name = author_name).exists():
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
        username = request.session.get('username')
        if request.method == "POST":
            book_id = request.POST['book_id']
            reader_count = IssueBook.objects.filter(reader_name = username).count()
            if reader_count < 3:
                if Book.objects.filter(book_id = book_id).exists():
                    book_object = Book.objects.filter(book_id = book_id).first()
                    book_id_count = IssueBook.objects.filter(issue_id = book_id).count()
                    if book_id_count >= 1:
                        messages.info(request,'book already issued.')
                        return render(request,'Bookmodule/issueBook.html')
                    else:
                        reader_object = Reader.objects.filter(username=username).first()
                        issued_book = IssueBook(issue_id=book_object,reader_name=reader_object)
                        issued_book.save()
                        messages.info(request,'successfully book issued')
                        return render(request,'Bookmodule/issueBook.html')
                else:
                    messages.info(request,'book does not exists')
                    return render(request,'Bookmodule/issueBook.html')
            else:
                messages.info(request,'yor have alredy taken 3 book')
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