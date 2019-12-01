from django import forms
from django.forms import ModelForm, Textarea


from .models import (
    category ,
    post ,
    comment ,
)

class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields =('title' ,'content' ,'summary' , 'image' ,'category')

class CategoryForm(forms.ModelForm):
    class Meta:
        model =category
        fields =('category' ,)
class CommentForm(forms.ModelForm):
    class Meta:
        model =comment
        fields =('user','post' ,'txt')
        widgets = {
            'txt': Textarea(attrs={'cols': 60, 'rows': 1}),
            'post':forms.HiddenInput() ,
            'user':forms.HiddenInput() ,

        }
