Features

This application manages books with specific access control based on user roles and permissions. Users can perform actions like viewing, creating, editing, or deleting books based on the permissions assigned to their groups.



# Permissions

Custom permissions included in the Book model:

|     Permission Code       |      Description              |
|-----------------------------------------------------------|
|     'can_view'            |      Allows Viewing Books     |
|     'can_create'          |      Allows Creating Books    |
|     'can_edit'            |      Allows Editing Books     |
|     'can_delete'          |      Allows Deleting Books    |



# Groups

Custom groups

|    Group Name             |      Permissions              |
|-----------------------------------------------------------|
|    'Viewers'              |      can_view                 |
|    'Editors'              |      can_view,_create,_edit   |
|    'Admins'               |      can_view,_create,_edit,_delete




1.  **Create Groups and Assign Permissions**
	The application uses predefined user groups (Viewers, Editors, and Admins) with different permissions for accessing books.

	To create the groups and assign the appropriate permissions, run the following script:

	python manage.py shell
	>>> from bookshelf.groups import create_groups
	>>> create_groups()



2.  **Create Test Users**
	To create test users and assign them to the respective groups, run the following:

	python manage.py shell
	>>> from bookshelf.groups import create_test_users
	>>> create_test_users()

	This will create three test users:

	viewer (assigned to Viewers group)
	editor (assigned to Editors group)
	admin (assigned to Admins group)



3.  **Permissions in Views**
	Permissions are applied using Django's @permission_required decorator. Each view is decorated to check if the user has the required permission before allowing access.

	Example in views.py:

	@permission_required('bookshelf.can_create', raise_exception=True)
	def create_book(request):
    	context = {}
    	return render(request, context)

	@permission_required('bookshelf.can_create'): Ensures that only users with the can_create permission can access the create_book view.
	raise_exception=True: Automatically raises a 403 Forbidden error if the user doesn't have the required permission.



4.  **Custom User Model**
	The project uses a custom user model (CustomUser) that extends AbstractUser and includes additional fields:

	date_of_birth: User's date of birth.
	profile_photo: User's profile photo.
