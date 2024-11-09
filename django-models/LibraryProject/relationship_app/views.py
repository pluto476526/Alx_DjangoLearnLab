from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from . models import Book, Library

# Create your views here.

def book_list(request):
    books = Book.objects.select_related('author').all()
    context = {'books': books}
    return render(request, 'books_list.html', context)


class LibraryDetails(DetailView):
    model = Library
    template_name = 'library_books.html'
    context_name = 'library'

    def get_data(self):
        context = super().books_in_lib()
        context['books'] = Book.objects.filter(library=self.object)
        return context
