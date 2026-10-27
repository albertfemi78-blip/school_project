from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    age = forms.IntegerField(min_value=1)
    class Meta:
        model = Student
        fields = ["name", "age", "course"]
        