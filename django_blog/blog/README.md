## Authentication Process
The core of the authentication system is the User model provided by django.contrib.auth.models. 

# User Registration
A user fills out a registration form with their details (username, password, email).
Upon submission, Django validates the data and creates a new User object if everything is correct.

# User Login
The user accesses a login page where they enter their credentials.
Upon submission, Django checks the credentials against the database.
If valid, Django creates a session for the user and redirects them to the homepage; otherwise, an error message is displayed.

# User Logout
The user can log out via a logout view that invalidates their session.
After logging out, they are redirected to the login page.


## Views
Class-based views (CBVs) handle CRUD (Create, Read, Update, Delete) operations for blog posts.
Each view is designed to manage specific functionalities related to blog posts.

# Overview
Django's class-based views allow for a more structured approach to handling web requests.
They encapsulate view logic within classes, enabling better organization and reuse of code.
The following views are implemented in the blog application:

    BlogPostListView: Displays a list of all blog posts.
    BlogPostDetailView: Shows the details of an individual blog post.
    BlogPostCreateView: Allows authenticated users to create new blog posts.
    BlogPostUpdateView: Enables authors to edit their existing blog posts.
    BlogPostDeleteView: Lets authors delete their blog posts.

## Mixins
# 1. LoginRequiredMixin
Purpose: This mixin ensures that only authenticated users can access certain views, such as creating, updating, or deleting blog posts.
Usage: It is used in BlogPostCreateView, BlogPostUpdateView, and BlogPostDeleteView to restrict access.

# 2. UserPassesTestMixin
Purpose: This mixin allows you to define custom test conditions for user access. It is useful for ensuring that only specific users (like the author of a post) can perform certain actions (like editing or deleting their posts).
Usage: It is used in BlogPostUpdateView and BlogPostDeleteView to check if the logged-in user is the author of the post.

