from django import forms

from .models import Certification, Topic


class TopicForm(forms.ModelForm):
    """docstring for ContactForm"""
    class Meta:
        model = Topic
        fields = '__all__'