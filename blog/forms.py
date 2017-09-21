from django import forms
from .models import Test, Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','date','location','location_howto','score_k','score_y',)

class TestForm(forms.ModelForm):
	class Meta:
		model = Test
		fields = ('title','text')



