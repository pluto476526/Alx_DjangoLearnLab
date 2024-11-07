# Create command
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Retrieve command
book = Book.objects.get(id=1)
print(book.title, book.author, book.publication_year)

# Update command
book.title = "Nineteen Eighty-Four"
book.save()

# Delete command
book.delete()
