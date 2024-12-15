# Social Media API

This project is a RESTful API for a social media platform, allowing users to register, authenticate, follow/unfollow other users, and access a feed displaying posts from followed users.

## Features

1. **User Registration and Authentication**
   - Register a new user.
   - Obtain an authentication token for existing users.

2. **User Relationships**
   - Follow and unfollow other users.

3. **Dynamic Feed**
   - View posts from users you follow, sorted by creation date (most recent posts appear first).

---

## Models

### Changes to the `CustomUser` Model

The `CustomUser` model now includes a `following` field:


---

## Endpoints

### 1. **Follow/Unfollow a User**

#### **Follow a User**

**Endpoint:** `/accounts/follow/<int:user_id>/`

**Method:** `POST`

**Description:** Allows an authenticated user to follow another user.

**Example Request:**

```bash
curl -X POST http://127.0.0.1:8000/accounts/follow/2/ \
-H "Authorization: Token YOUR_AUTH_TOKEN" \
-H "Content-Type: application/json"
```

**Response:**

```json
{
    "message": "You are now following john_doe"
}
```

#### **Unfollow a User**

**Endpoint:** `/accounts/unfollow/<int:user_id>/`

**Method:** `POST`

**Description:** Allows an authenticated user to unfollow another user.

**Example Request:**

```bash
curl -X POST http://127.0.0.1:8000/accounts/unfollow/2/ \
-H "Authorization: Token YOUR_AUTH_TOKEN" \
-H "Content-Type: application/json"
```

**Response:**

```json
{
    "message": "You have unfollowed john_doe"
}
```

---

### 2. **Access the Feed**

#### **Feed Endpoint**

**Endpoint:** `/posts/feed/`

**Method:** `GET`

**Description:** Retrieves a feed of posts from users that the authenticated user follows. The posts are ordered by creation date, with the most recent posts appearing first.

**Example Request:**

```bash
curl -X GET http://127.0.0.1:8000/posts/feed/ \
-H "Authorization: Token YOUR_AUTH_TOKEN"
```

**Response:**

```json
[
    {
        "id": 1,
        "author": "john_doe",
        "content": "Hello, world!",
        "created_at": "2024-12-14T12:34:56Z"
    },
    {
        "id": 2,
        "author": "jane_smith",
        "content": "This is my first post!",
        "created_at": "2024-12-13T08:21:10Z"
    }
]
```

