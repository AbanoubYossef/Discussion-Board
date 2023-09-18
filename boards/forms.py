from django import forms
from .models import Topic,Post
class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
        attrs={ 'raws':5,'placeholder':'What is in your mind'}
        ), max_length=4000,
    help_text='the max length is 4000 letters')
    class Meta:
        model = Topic
        fields =['subject', 'message']     

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields=['message']