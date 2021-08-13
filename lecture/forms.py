from django import forms
from .models import Lecture


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['class_name', 'content', 'level', 'period', 'subject', 'pre_ready', 'category', 'lecture_image']
