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

