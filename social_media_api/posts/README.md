# Posts and Comments API Documentation

## Overview
This API allows users to interact with posts and comments in a social media application. Users can create, view, update, and delete posts and comments. The API requires authentication for certain operations.

---

## Authentication
- **Token-Based Authentication**
- Include your token in the `Authorization` header as follows:

  ```
  Authorization: Token <your_token_here>
  ```

---

## Endpoints

### **Posts**
#### Base URL: `/posts/posts/`

#### **1. Create a Post**
- **Method:** `POST`
- **Headers:**
  ```
  Content-Type: application/json
  Authorization: Token <your_token_here>
  ```
- **Request Body:**
  ```json
  {
      "title": "My First Post",
      "content": "This is the content of my first post."
  }
  ```
- **cURL Command:**
  ```bash
  curl -X POST http://127.0.0.1:54000/posts/posts/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token <your_token_here>" \
  -d '{
      "title": "My First Post",
      "content": "This is the content of my first post."
  }'
  ```
- **Response Example:**
  ```json
  {
      "id": 1,
      "author": 1,
      "author_username": "john_doe",
      "title": "My First Post",
      "content": "This is the content of my first post.",
      "created_at": "2024-12-14T23:00:00Z",
      "updated_at": "2024-12-14T23:00:00Z",
      "comments": []
  }
  ```

#### **2. View All Posts**
- **Method:** `GET`
- **Headers:**
  ```
  Authorization: Token <your_token_here>
  ```
- **cURL Command:**
  ```bash
  curl -X GET http://127.0.0.1:54000/posts/posts/ \
  -H "Authorization: Token <your_token_here>"
  ```
- **Response Example:**
  ```json
  [
      {
          "id": 1,
          "author": 1,
          "author_username": "john_doe",
          "title": "My First Post",
          "content": "This is the content of my first post.",
          "created_at": "2024-12-14T23:00:00Z",
          "updated_at": "2024-12-14T23:00:00Z",
          "comments": []
      }
  ]
  ```

#### **3. View a Single Post**
- **Method:** `GET`
- **URL:** `/posts/posts/<post_id>/`
- **Headers:**
  ```
  Authorization: Token <your_token_here>
  ```
- **cURL Command:**
  ```bash
  curl -X GET http://127.0.0.1:54000/posts/posts/1/ \
  -H "Authorization: Token <your_token_here>"
  ```
- **Response Example:**
  ```json
  {
      "id": 1,
      "author": 1,
      "author_username": "john_doe",
      "title": "My First Post",
      "content": "This is the content of my first post.",
      "created_at": "2024-12-14T23:00:00Z",
      "updated_at": "2024-12-14T23:00:00Z",
      "comments": []
  }
  ```

#### **4. Update a Post**
- **Method:** `PUT`
- **URL:** `/posts/posts/<post_id>/`
- **Headers:**
  ```
  Content-Type: application/json
  Authorization: Token <your_token_here>
  ```
- **Request Body:**
  ```json
  {
      "title": "Updated Title",
      "content": "Updated content."
  }
  ```
- **cURL Command:**
  ```bash
  curl -X PUT http://127.0.0.1:54000/posts/posts/1/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token <your_token_here>" \
  -d '{
      "title": "Updated Title",
      "content": "Updated content."
  }'
  ```
- **Response Example:**
  ```json
  {
      "id": 1,
      "author": 1,
      "author_username": "john_doe",
      "title": "Updated Title",
      "content": "Updated content.",
      "created_at": "2024-12-14T23:00:00Z",
      "updated_at": "2024-12-15T00:00:00Z",
      "comments": []
  }
  ```

#### **5. Delete a Post**
- **Method:** `DELETE`
- **URL:** `/posts/posts/<post_id>/`
- **Headers:**
  ```
  Authorization: Token <your_token_here>
  ```
- **cURL Command:**
  ```bash
  curl -X DELETE http://127.0.0.1:54000/posts/posts/1/ \
  -H "Authorization: Token <your_token_here>"
  ```
- **Response Example:**
  ```
  HTTP 204 No Content
  ```

---

### **Comments**
#### Base URL: `/posts/comments/`

#### **1. Create a Comment**
- **Method:** `POST`
- **Headers:**
  ```
  Content-Type: application/json
  Authorization: Token <your_token_here>
  ```
- **Request Body:**
  ```json
  {
      "post": 1,
      "content": "This is a comment on post 1."
  }
  ```
- **cURL Command:**
  ```bash
  curl -X POST http://127.0.0.1:54000/posts/comments/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token <your_token_here>" \
  -d '{
      "post": 1,
      "content": "This is a comment on post 1."
  }'
  ```
- **Response Example:**
  ```json
  {
      "id": 1,
      "post": 1,
      "author": 1,
      "author_username": "john_doe",
      "content": "This is a comment on post 1.",
      "created_at": "2024-12-14T23:15:00Z",
      "updated_at": "2024-12-14T23:15:00Z"
  }
  ```

#### **2. View All Comments**
- **Method:** `GET`
- **Headers:**
  ```
  Authorization: Token <your_token_here>
  ```
- **cURL Command:**
  ```bash
  curl -X GET http://127.0.0.1:54000/posts/comments/ \
  -H "Authorization: Token <your_token_here>"
  ```
- **Response Example:**
  ```json
  [
      {
          "id": 1,
          "post": 1,
          "author": 1,
          "author_username": "john_doe",
          "content": "This is a comment on post 1.",
          "created_at": "2024-12-14T23:15:00Z",
          "updated_at": "2024-12-14T23:15:00Z"
      }
  ]
  ```

#### **3. Delete a Comment**
- **Method:** `DELETE`
- **URL:** `/posts/comments/<comment_id>/`
- **Headers:**
  ```
  Authorization: Token <your_token_here>
  ```
- **cURL Command:**
  ```bash
  curl -X DELETE http://127.0.0.1:54000/posts/comments/1/ \
  -H "Authorization: Token <your_token_here>"
  ```
- **Response Example:**
  ```
  HTTP 204 No Content
  ```

---
