from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


def is_librarian(user):
    return user.groups.filter(name='Librarian').exists()

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')
