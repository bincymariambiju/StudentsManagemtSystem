from django import forms
from studcamp.models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"