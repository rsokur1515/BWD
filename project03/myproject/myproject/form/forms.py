from django import forms 
from form.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'surname', 'content', 'seat']
