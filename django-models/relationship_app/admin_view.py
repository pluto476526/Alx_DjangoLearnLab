from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

@user_passes_test(is_admin)
def Admin(request):
    return render(request, 'relationship_app/admin_view.html')
