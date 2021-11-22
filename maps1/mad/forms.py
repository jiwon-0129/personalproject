from django import forms
from django.db.models.query import QuerySet
from django.forms import fields
from .models import *

class RestaurantForm(forms.ModelForm):
    class Meta:
        model=Restaurant
        fields=['name','latitude','longitude','choice','signature_menu','image',]


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('point', 'author_name', 'comment_text', 'photo',)

class FilterForm(forms.ModelForm):
    class Meta:
        model=Filter
        fields='__all__'

class PostSearchForm(forms.Form):
    search_word=forms.CharField(label='Search Word')