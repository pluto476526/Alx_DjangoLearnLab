# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book():
    context = {}
    return render(request, context)


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list():
    context = {}
    return render(request, context)


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book():
    context = {}
    return render(request, context)


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book():
    context = {}
    return render(request, context)
