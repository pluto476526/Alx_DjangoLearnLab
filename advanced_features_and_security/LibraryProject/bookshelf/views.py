# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from bookshelf.forms import BookForm
from bookshelf.models import Book
from .forms import ExampleForm


# Create your views here.

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('create_book')

    context = {'form': form}
    return render(request, 'bookshelf/create_book.html', context)


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'bookshelf/book_list.html', context)


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, id=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('all_books')

    form = BookForm(instance=book)    
    context = {'form': form}
    return render(request,'bookshelf/edit_book.html', context)


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    
    if request.method == 'POST':
        book.delete()
        return redirect('all_books')

    context = {'book': book}
    return render(request, 'bookshelf/delete_book.html', context)



@permission_required('bookshelf.can_edit', raise_exception=True)
def form_example(request):
    form = ExampleForm()

    if request.method == 'POST':
        form = ExampleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('all_books')

    context = {'form': form}
    return render(request, 'bookshelf/form_example.html', context)









