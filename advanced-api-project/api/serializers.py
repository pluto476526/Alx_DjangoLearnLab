from rest_framework import serializers
from . models import Book, Author
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        # Get current year
        current_year = datetime.now().year

        # Check if book was published in a future year
        if data['publication_year'] > current_year:

            # Raise validation error
            raise serializers.ValidationError('Book cannot be published in the future')

        return data



class AuthorSerializer(serializers.ModelSerializer):
    # Nestes serializer to retrieve books for current author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']


