from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from . models import Book, Library

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, "relationship_app/list_books.html", context")


class LibraryDetails(DetailView):
    model = Library
    template_name = 'relationship_app/library_detailss.html'
    context_name = 'library'

    def get_data(self):
        context = super().books_in_lib()
        context['books'] = Book.objects.filter(library=self.object)
        return context
