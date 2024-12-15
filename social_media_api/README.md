# https://trin985.pythonanywhere.com/api/feed/

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








# Social Media API: Likes and Notifications System

This documentation explains the functionality and endpoints for the likes and notifications systems in the Social Media API. These features enhance user engagement by allowing users to interact with posts and stay updated on activities related to their content and profile.

---

## Features Overview

1. **Like System**:
   - Enables users to like and unlike posts.
   - Prevents duplicate likes by the same user.

2. **Notifications System**:
   - Notifies users when:
     - They gain a new follower.
     - Someone likes their post.
     - Someone comments on their post.
   - Provides an endpoint to fetch notifications.

---

## Like Functionality

### Endpoints

#### **1. Like a Post**

- **URL**: `/posts/<int:pk>/like/`
- **Method**: `POST`
- **Authentication**: Required

**Description**: Allows authenticated users to like a specific post. If the post is already liked, an error is returned.

**Example Request**:
```bash
curl -X POST http://127.0.0.1:8000/posts/1/like/ \
-H "Authorization: Token YOUR_AUTH_TOKEN"
```

**Response (Success)**:
```json
{
    "message": "Post liked"
}
```

**Response (Already Liked)**:
```json
{
    "error": "You already liked this post"
}
```

**Response (Post Not Found)**:
```json
{
    "detail": "Not found."
}
```

---

#### **2. Unlike a Post**

- **URL**: `/posts/<int:pk>/unlike/`
- **Method**: `POST`
- **Authentication**: Required

**Description**: Allows authenticated users to unlike a specific post. If the post is not liked, an error is returned.

**Example Request**:
```bash
curl -X POST http://127.0.0.1:8000/posts/1/unlike/ \
-H "Authorization: Token YOUR_AUTH_TOKEN"
```

**Response (Success)**:
```json
{
    "message": "Post unliked"
}
```

**Response (Not Liked)**:
```json
{
    "error": "You have not liked this post"
}
```

**Response (Post Not Found)**:
```json
{
    "detail": "Not found."
}
```

---

## Notifications System

### Endpoints

#### **1. Fetch Notifications**

- **URL**: `/notifications/`
- **Method**: `GET`
- **Authentication**: Required

**Description**: Retrieves a list of notifications for the authenticated user. Unread notifications are prominently displayed.

**Example Request**:
```bash
curl -X GET http://127.0.0.1:8000/notifications/ \
-H "Authorization: Token YOUR_AUTH_TOKEN"
```

**Response**:
```json
[
    {
        "id": 1,
        "recipient": "john_doe",
        "actor": "jane_smith",
        "verb": "liked your post",
        "target": "Hello, world!",
        "timestamp": "2024-12-14T12:34:56Z",
        "unread": true
    },
    {
        "id": 2,
        "recipient": "john_doe",
        "actor": "mike_brown",
        "verb": "followed you",
        "timestamp": "2024-12-13T15:21:10Z",
        "unread": false
    }
]
```

**Response Fields**:
- `id`: Unique identifier for the notification.
- `recipient`: The user receiving the notification.
- `actor`: The user performing the action.
- `verb`: Description of the action.
- `target`: The object related to the action (e.g., post content).
- `timestamp`: When the notification was created.
- `unread`: Indicates if the notification is unread.


