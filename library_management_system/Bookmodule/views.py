from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Book, IssueBook
from loginmodule.models import Reader
from django.urls import reverse
from django.db.models import Q
import datetime

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
        issued_books = [ (book.issue_id,book.issue_date + datetime.timedelta(days=10)) for book in IssueBook.objects.filter(reader_name=username)]
        if request.method == "POST":
            book_id = request.POST['book_id']
            issued_book = IssueBook.objects.filter(issue_id=book_id)
            issued_book.delete()
            book = Book.objects.filter(book_id=book_id).first()
            book.is_book_available = True
            book.save()
            issued_books = [(book.issue_id,book.issue_date + datetime.timedelta(days=10)) for book in IssueBook.objects.filter(reader_name=username)]
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
                    is_book_available = Book.objects.filter(book_id=book_id).first().is_book_available
                    if not is_book_available:
                        messages.error(request,'book already issued.')
                        books = Book.objects.filter(is_book_available=True)
                        return render(request,"Bookmodule/issueBook.html",{'books':books})
                    else:
                        reader_object = Reader.objects.filter(username=username).first()
                        issued_book = IssueBook(issue_id=book_object,reader_name=reader_object)
                        book = Book.objects.filter(book_id=book_id).first()
                        book.is_book_available = False
                        book.save()
                        issued_book.save()
                        messages.success(request,'successfully book issued')
                        books = Book.objects.filter(is_book_available=True)
                        return render(request,"Bookmodule/issueBook.html",{'books':books})
                else:
                    messages.error(request,'book does not exists')
                    books = Book.objects.filter(is_book_available=True)
                    return render(request,"Bookmodule/issueBook.html",{'books':books})
            else:
                messages.error(request,'you have alredy taken 3 book')
                books = Book.objects.filter(is_book_available=True)
                return render(request,"Bookmodule/issueBook.html",{'books':books})
        else:
            # return render(request,'Bookmodule/issueBook.html')
            if 'search' in request.GET:
                query = request.GET['search']
                search_category = request.GET['search_category']
                if search_category == "All":
                    books = Book.objects.all().filter(Q(book_id__icontains = query) | Q(book_name__icontains = query) | Q(author_name__icontains = query) & Q(is_book_available = True))
                elif search_category == "book_id":
                    books = Book.objects.all().filter(Q(book_id__icontains = query) & Q(is_book_available = True))
                elif search_category == "book_name":
                    books = Book.objects.all().filter(Q(book_name__icontains = query) & Q(is_book_available = True))
                elif search_category == "author_name":
                    books = Book.objects.all().filter(Q(book_author__icontains = query) & Q(is_book_available = True))
                else:
                    books = Book.objects.all().filter(Q(book_id__icontains = query) | Q(book_name__icontains = query) | Q(author_name__icontains = query) & Q(is_book_available = True))
                return render(request,"Bookmodule/issueBook.html",{'books':books})
            else:
                books = Book.objects.filter(is_book_available=True)
                return render(request,"Bookmodule/issueBook.html",{'books':books})

def showFine(request):
    if request.session.get('username') == None:
        messages.error(request,'You are not authorize')
        return redirect(reverse("loginmodule:login"))
    else:
        username = request.session.get("username")
        issued_books = IssueBook.objects.filter(reader_name=username)
        fine = 0
        for issued_book_object in issued_books:
            if (datetime.date.today().day) - ((issued_book_object.issue_date + datetime.timedelta(days=10)).day) > 0:
                fine += 10
        return render(request,"Bookmodule/showFine.html",{"fine": fine})

def profile(request):
    username = request.session.get("username")

    #create all session
    u = Reader.objects.filter(username=username).first()
    request.session['member_username'] = u.username
    request.session['member_password'] = u.password
    request.session['member_email'] = u.email
    request.session['member_fname'] = u.first_name
    request.session['member_lname'] = u.last_name
    
    if request.method=="POST":
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        user = Reader.objects.filter(username=username).first()
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        return render(request,"Bookmodule/profile.html")
    else:
        return render(request,"Bookmodule/profile.html")