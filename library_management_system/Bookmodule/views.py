from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Book, IssueBook
from loginmodule.models import Reader
from django.urls import reverse
from django.db.models import Q

def addBook(request):
    if request.session.get('superuser') == None:
        messages.error(request,'You are not authorize')
        return redirect(reverse("loginmodule:login"))
    else:
        if request.method == "POST":
            book_name = request.POST['book_name']
            author_name = request.POST['author_name']
            publish_year = request.POST['publish_year']
            if Book.objects.filter(book_name = book_name).exists() and Book.objects.filter(author_name = author_name).exists():
                messages.error(request,'book already exist')
                return render(request,'Bookmodule/addBook.html')
            else:
                book = Book(book_name = book_name , author_name = author_name , publish_year = publish_year)
                book.save()
                book_id = Book.objects.filter(book_name=book_name).first().book_id
                messages.success(request,f'successfully book added and id is {book_id}')
                return render(request,'Bookmodule/addBook.html')
        else:
             return render(request,'Bookmodule/addBook.html')
                

def returnBook(request):
    if request.session.get('username') == None:
        messages.error(request,'You are not authorize')
        return redirect(reverse("loginmodule:login"))
    else:
        username = request.session.get('username')
        issued_books = [ book.issue_id for book in IssueBook.objects.filter(reader_name=username) ]
        if request.method == "POST":
            book_id = request.POST['book_id']
            issued_book = IssueBook.objects.filter(issue_id=book_id)
            issued_book.delete()
            issued_books = [ book.issue_id for book in IssueBook.objects.filter(reader_name=username) ]
            return render(request,"Bookmodule/returnBook.html",{"books": issued_books})
        else:  
            return render(request,'Bookmodule/returnBook.html',{"books": issued_books})

def removeBook(request):
    if request.session.get('superuser') == None:
        messages.error(request,'You are not authorize')
        return redirect(reverse("loginmodule:login"))
    else:
        if request.method == "POST":
            book_id = request.POST['book_id']
            if Book.objects.filter(book_id = book_id).exists():
                    messages.error(request,'book is removed')
                    b = Book.objects.filter(book_id=book_id).first()
                    b.delete()
                    return render(request,'Bookmodule/removeBook.html')
            else:
                messages.error(request,'book not exists')
                return render(request,'Bookmodule/removeBook.html')
        else:
            return render(request,'Bookmodule/removeBook.html')

def issueBook(request):
    if request.session.get('username') == None:
        messages.error(request,'You are not authorize')
        return redirect(reverse("loginmodule:login"))
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
                        messages.error(request,'book already issued.')
                        books = Book.objects.all()
                        return render(request,"Bookmodule/issueBook.html",{'books':books})
                    else:
                        reader_object = Reader.objects.filter(username=username).first()
                        issued_book = IssueBook(issue_id=book_object,reader_name=reader_object)
                        issued_book.save()
                        messages.success(request,'successfully book issued')
                        books = Book.objects.all()
                        return render(request,"Bookmodule/issueBook.html",{'books':books})
                else:
                    messages.error(request,'book does not exists')
                    books = Book.objects.all()
                    return render(request,"Bookmodule/issueBook.html",{'books':books})
            else:
                messages.error(request,'yor have alredy taken 3 book')
                books = Book.objects.all()
                return render(request,"Bookmodule/issueBook.html",{'books':books})
        else:
            # return render(request,'Bookmodule/issueBook.html')
            if 'search' in request.GET:
                query = request.GET['search']
                search_category = request.GET['search_category']
                if search_category == "All":
                    books = Book.objects.all().filter(Q(book_id__icontains = query) | Q(book_name__icontains = query) | Q(author_name__icontains = query))
                elif search_category == "book_id":
                    books = Book.objects.all().filter(Q(book_id__icontains = query))
                elif search_category == "book_name":
                    books = Book.objects.all().filter(Q(book_name__icontains = query))
                elif search_category == "author_name":
                    books = Book.objects.all().filter(Q(book_author__icontains = query))
                else:
                    books = Book.objects.all().filter(Q(book_id__icontains = query) | Q(book_name__icontains = query) | Q(author_name__icontains = query))
                return render(request,"Bookmodule/issueBook.html",{'books':books})
            else:
                books = Book.objects.all()
                return render(request,"Bookmodule/issueBook.html",{'books':books})
