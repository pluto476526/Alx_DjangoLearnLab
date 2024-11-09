from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_member(user):
    return user.groups.filter(name='Member').exists()

@user_passes_test(is_member)
def Member(request):
    return render(request, 'member_view.html')
