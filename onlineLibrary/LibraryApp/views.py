from django.shortcuts import render, redirect, resolve_url
from .models import Book
from .forms import AddBookForm


# this function to show all books
def book_info(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, "library.html", context)


# this function to add books to database
def add_book(request):
    if request.method == "POST":
        form = AddBookForm(request.POST)
    else:
        form = AddBookForm()
    if request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(resolve_url("library:all_books"))
    form = AddBookForm()
    context = {"form": form}
    return render(request, "add-book.html", context)

    '''
    if request.method == 'POST':
        print('hellooooooo')
        addForm = AddBookForm(request.POST)

        if addForm.is_valid(): # the issue from here.some model fields are causing invalid
            addForm.save()
            return redirect(resolve_url("library:all_books"))

    form = AddBookForm()
    context = {"form": form}
    return render(request, "add-book.html", context)
    '''
