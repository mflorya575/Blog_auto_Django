from django import forms
from .models import Comment, CarDealership


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']


class SearchForm(forms.Form):
    query = forms.CharField()


class CarDealershipForm(forms.ModelForm):
    class Meta:
        model = CarDealership
        fields = ['name', 'address', 'photo', 'car_count', 'description']
