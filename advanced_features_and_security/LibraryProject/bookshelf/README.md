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


# Usage

1.  **Creating Groups and Permissions:**
    Run 'create_groups' function to set them up:
	```python3
	from groups import create_groups
	create_groups()


# Creating Users and Superusers
	 python3 manage.py shell   # Start the Django shell

	 >>> from bookshelf.models import CustomUser # Import module

     >>> user = CustomUser.objects.create_user(username='Trinity985', password='12341234', date_of_birth='2000-02-01') # Create regular user
     >>> superuser = CustomUser.objects.create_superuser(username='Pluto', password='12341234') # Create super user