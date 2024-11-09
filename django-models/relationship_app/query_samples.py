from relationship_app.models import Author, Book, Library, Librarian

# Get all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books

    except Author.DoesNotExist:
        return "No such author"


# Get all books in a specific lib
def get_books_in_lib(library_name):
    try:
        books = Library.objects.get(name=library_name)
        return library.books.all()

    except Library.DoesNotExist:
        return "No such Library"


# Get librarian
def get_librarian(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.filter(library=library)
        return librarian

    except Library.DoesNotExist:
        return "No such Library"

    except Librarian.DoesNotExist:
        return "No such librarian"
