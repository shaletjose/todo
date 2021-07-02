from django import forms
from .models import  todoapp
class todo_form(forms.ModelForm):
    class Meta:
        model=todoapp
        fields=['activity_name','priority','date1']
