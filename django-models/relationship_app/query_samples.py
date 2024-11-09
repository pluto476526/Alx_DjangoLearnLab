from relationship_app.models import Author, Book, Library, Librarian

# Get all books by a specific author
def get_books_by_author(author_name):
    try:
        book_author = Author.objects.get(name=author_name)
        book = Book.objects.filter(author=author_name)
        return book_author.books.all()

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
        librarian = Library.objects.get(name=library_name)
        return Library.librarian

    except Library.DoesNotExist:
        return "No such Library"

    except Librarian.DoesNotExist:
        return "No such librarian"
