from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']


class SearchForm(forms.Form):
    query = forms.CharField()


class CarDealershipForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'address', 'tel', 'city', 'thumbnail', 'car_count', 'body']
