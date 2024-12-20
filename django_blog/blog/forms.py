from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Post, Comment
from taggit.forms import TagField, TagWidget


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class BlogPostsForm(forms.ModelForm):
    tags = TagField(widgets=TagWidget())

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')

        if not content.strip():
            raise forms.ValidationError('Please enter comment')

        return content
