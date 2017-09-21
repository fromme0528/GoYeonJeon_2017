from django import forms
from .models import Post, Score

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','text',)

class ScoreForm(forms.ModelForm):
	class Meta:
		model = Score
		fields = ('title','location','date','score_k','score_y')

