from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Author, Category, Article, Comments
class New_admin_form(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        ]

class Article_form(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'category',
            'image',
            'paragraph',
            'image_2',
            'paragraph_2',
        ]

class Comments_form(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            'name',
            'email',
            'comment'
        ]

class Create_category_form(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name'
        ]