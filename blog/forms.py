from django import forms
from .models import Post,Cheeringsongs

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title','text',)

class SongForm(forms.ModelForm):
	class Meta:
		model = Cheeringsongs
		fields = ('title','rylic','url')
