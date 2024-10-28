from bookshelf.models import Book
new_book = Book(title="1949", author="George Orwell", publication_year=1949)
new_book.save()
Book.objects.all() # <QuerySet [<Book: Book object (1)>]>
