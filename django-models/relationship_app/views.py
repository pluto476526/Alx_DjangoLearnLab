from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from .models import Book
from .models import Library


# Create your views here.

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, "relationship_app/list_books.html", context)


class LibraryDetails(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_name = 'library'

    def get_data(self):
        context = super().books_in_lib()
        context['books'] = Book.objects.filter(library=self.object)
        return context



def register(request):
    register_form = UserCreationForm()

    if request.method == "POST":
        register_form = UserCreationForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            return redirect('sign_in')

    return render(request, 'relationship_app/register.html', {'register_form': register_form})


def sign_in(request):
    login_form = AuthenticationForm()

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Invalid username or password')

    context = {'sign_in_form': login_form}
    return render(request, 'relationship_app.html', context)


def sign_out(request):
    logout(request)
    return redirect('/')


def is_admin(user):
    return user.groups.filter(name='Admin').exists()

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


def is_librarian(user):
    return user.groups.filter(name='Librarian').exists()

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


def is_member(user):
    return user.groups.filter(name='Member').exists()

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')




