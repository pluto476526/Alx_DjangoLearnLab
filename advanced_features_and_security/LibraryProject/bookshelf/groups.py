from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book, CustomUser



def create_groups():
    groups_permissions = {
        'Viewers': ['can_view'],
        'Editors': ['can_view', 'can_create', 'can_edit'],
        'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
    }

    try:
        content_type = ContentType.objects.get_for_model(Book)
        print(f"ContentType for Book model: {content_type}")
    except ContentType.DoesNotExist:
        print("ContentType for Book model does not exist.")
        return

    for group_name, permissions in groups_permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        if created:
            print(f"Created group: {group_name}")
        else:
            print(f"Group already exists: {group_name}")

        for codename in permissions:
            permission, perm_created = Permission.objects.get_or_create(
                codename=codename,
                content_type=content_type,
                defaults={'name': f"Can {codename.split('_')[-1]} book"},
            )
            if perm_created:
                print(f"Created permission: {codename}")
            else:
                print(f"Permission already exists: {codename}")

            group.permissions.add(permission)
        print(f"Updated group '{group_name}' with permissions: {permissions}")



def create_test_users():
    # Create test users
    users = [
        {'username': 'viewer', 'password': 'viewer123', 'group': 'Viewers'},
        {'username': 'editor', 'password': 'editor123', 'group': 'Editors'},
        {'username': 'admin', 'password': 'admin123', 'group': 'Admins'},
    ]

    for user_data in users:
        user, created = CustomUser.objects.get_or_create(username=user_data['username'])
        if created:
            user.set_password(user_data['password'])
            user.save()
            print(f"Created user: {user_data['username']}")
        else:
            print(f"User already exists: {user_data['username']}")

        # Assign user to group
        try:
            group = Group.objects.get(name=user_data['group'])
            user.groups.add(group)
            print(f"Assigned {user.username} to group: {group.name}")
        except Group.DoesNotExist:
            print(f"Group {user_data['group']} does not exist. Please create groups first.")


if __name__ == "__main__":
    create_groups()
    create_test_users()
