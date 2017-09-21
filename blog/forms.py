from django import forms
from .models import Post, Message

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','date','location','location_howto','score_k','score_y',)

class MessageForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = ('title','text',)