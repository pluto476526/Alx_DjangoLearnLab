# API Docs

## Endpoints

### 1. List Books
- **URL**: `/books/`
- **Method**: `GET`
- **Perms**: Public

### 2. Book Details
- **URL**: `/books/<id>/`
- **Method**: `GET`
- **Perms**: Public

### 3. Create New Book
- **URL**: `/books/create/`
- **Method**: `POST`
- **Perms**: Authenticated users

### 4. Update Book
- **URL**: `/books/<id>/update/`
- **Method**: `PUT`
- **Perms**: Authenticated users

### 5. Delete Book
- **URL**: `/books/<id>/delete/`
- **Method**: `DELETE`
- **Perms**: Authenticated users


# Features

## Filtering, Searching, and Ordering

### Fields
-- `title`, `author`, or `publication_year`.




# Testing API Endpoints

## Overview
This test suite verifies the functionality and security of the API endpoints, ensuring correct behavior under various conditions.

## Test Cases
1. **List Books**: Ensure the list endpoint returns all books.
2. **Retrieve a Book**: Verify that individual books can be retrieved by ID.
3. **Create a Book**: Check that only authenticated users can create books.
4. **Update a Book**: Ensure updates are allowed only for authenticated users.
5. **Delete a Book**: Verify deletion works and is restricted to authenticated users.
6. **Filtering, Searching, Ordering**:
   - Filter books by fields like `author`.
   - Search books by keywords.
   - Order books by fields like `publication_year`.

## Running Tests
1. Use the following command to run the tests:
   ```bash
   python manage.py test api

